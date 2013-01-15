import re
import os
import sys
import functools
import numpy 
import time
import math
import platform
import functools
from PyQt4 import QtCore
from PyQt4 import QtGui
from expresso.libs.expresso_serial import ExpressoSerial
from expresso_gui_ui import Ui_MainWindow 
from hdf5_logger import HDF5_Logger
from subprocess import Popen,PIPE
from serial.tools import list_ports
from mcwidget import McWidget

# Constants
TIMER_SINGLE_INTERVAL_MS =  333 
TIMER_MULTI_INTERVAL_MS =  250 
LOWPASS_FREQ_CUTOFF = 0.5 
MM2NL = 5.0e3/54.8
PIXEL2MM = 63.5e-3
AIN_MAX_VOLT= 3.3
MAX_PIXEL = 768
PIXEL_TO_VOLT = AIN_MAX_VOLT/float(255)
NUM_CHANNELS = 5
ARRAY_SZ = 768
CAPILLARY_VOLUME = PIXEL2MM*MM2NL*ARRAY_SZ
LOG_FILE_EXT = '.hdf5'
DEFAULT_LOG_FILE = 'expresso_default_log{0}'.format(LOG_FILE_EXT)
MAPLE_VENDOR_ID = '1eaf'

class ExpressoMainWindow(QtGui.QMainWindow,Ui_MainWindow):

    def __init__(self,parent=None):
        super(ExpressoMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.initialize()
        self.connectActions()
        self.setupTimers()

    def initialize(self):
        self.devs = {'portList':[],'idList':[],'connected':False,'devices':{}}

        self.channelRadioButton_1.setChecked(True)
        self.statusbar.showMessage('Not Connected')

        # Set progressbar ranges 
        self.setAllProgressBarFont()
        self.setAllProgressBarRange()
        self.clearAllProgressBar()

        # Initialize plot and array for sensor data
        self.initializePlot()
        self.pixelPosArray = numpy.arange(0,ARRAY_SZ)
            
        # Set Enabled state of widgets for startup.
        self.setWidgetEnabledOnDisconnect()

        # Setup log file information
        self.userHome = os.getenv('USERPROFILE')
        if self.userHome is None: 
            self.userHome = os.getenv('HOME') 
        self.defaultLogPath = os.path.join(self.userHome, DEFAULT_LOG_FILE) 
        self.logPath = self.defaultLogPath 
        self.logFileLabel.setText(self.logPath)
        self.lastLogDir = self.userHome
        self.logger = None
        self.tStart = None
        self.multiChannelState = 'cmd' 

    def main(self):
        self.show()

    def closeEvent(self,event):
        if not (self.devs['connected'] == False):
            self.cleanUpAndCloseDevices()
        event.accept()

    def cleanUpAndCloseDevices(self):
        for devId in self.devs['devices']:
            dev = self.devs['devices'][devId]
            dev.setModeStopped()
            dev.setChannel(0)
            dev.close()
        self.devs['devices'] = {} 
        self.devs['connected'] = False

    def connectActions(self):
        # Actions for widgets on the single channel tab
        for chan in range(1,NUM_CHANNELS+1):
            radioButton = getattr(self,'channelRadioButton_{0}'.format(chan))
            radioButton.clicked.connect(self.channelRadioButtonClicked_Callback)
        self.singleChannelStart.clicked.connect(self.singleChannelStart_Callback)
        self.clearNormalizationPushButton.clicked.connect(self.clearNormalization_Callback)
        self.setNormalizationPushButton.clicked.connect(self.setNormalization_Callback)
        self.saveNormalizationPushButton.clicked.connect(self.saveNormalization_Callback)
        self.loadNormalizationPushButton.clicked.connect(self.loadNormalization_Callback)

        # Actions for widgets on the multi channel mode tab
        self.multiChannelStart.clicked.connect(self.multiChannelStart_Callback)
        self.setLogFileToolButton.clicked.connect(self.setLogFile_Callback)
        self.scanPushButton.pressed.connect(self.scanPressedDev_Callback)
        self.scanPushButton.clicked.connect(self.scanClickedDev_Callback)

        self.connectPushButton.clicked.connect(self.connectClicked_Callback)
        self.connectPushButton.pressed.connect(self.connectPressed_Callback)

    def scanPressedDev_Callback(self):
        # Allows hotplugging a device
        self.devs = {'portList':[],'idList':[],'connected':False,'devices':{}}
        self.depopulateDevices()

    def scanClickedDev_Callback(self):
        osType = platform.system()
        # Linux
        if osType == 'Linux': 
            # Sample output
            # ('/dev/ttyACM2', 'ttyACM2', 'USB VId:PId=1eaf:0004')
            for port in list_ports.comports():
                if (re.search(MAPLE_VENDOR_ID,port[2])):
                    # This try:except wraps the initialization of the Serial object.  Another 
                    # try-except within in the actual initialization method wraps the attempt 
                    # to communicate with the Serial device.
                    try:
                        with ExpressoSerial(port[0]) as dev:
                            if(dev.isExpressoDevice):
                                self.devs['portList'].append(port[0]);
                                self.devs['idList'].append(dev.devId);
                    # If a device with a MAPLE_VENDOR_ID doesn't respond something is funky.
                    except Exception, e:
                        QtGui.QMessageBox.critical(self,'Error', str(e))
        # Windows
        else: 
            pass

        if len(self.devs['portList'])>0:
            self.populateDevWidgetContainer()
            self.devWidgetContainer.setEnabled(True)
        else:
            QtGui.QMessageBox.critical(self,'Error', 'No expresso devices found in the system.')

    def populateDevWidgetContainer(self):
        for port,devId in zip(self.devs['portList'],self.devs['idList']):
            container = QtGui.QWidget(self.deviceTab)
            container.setObjectName("widget-"+devId)
            spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
            self.devWidgetVLay.addWidget(container)
            label = QtGui.QLabel(container)
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            label.setFont(font)
            label.setText(QtGui.QApplication.translate("MainWindow", "Port", None, QtGui.QApplication.UnicodeUTF8))
            label.setObjectName("label-"+devId)
            horLayout = QtGui.QHBoxLayout(container)
            horLayout.setMargin(0)
            horLayout.setObjectName("horizontalLayout-"+devId)
            horLayout.addItem(spacerItem)
            horLayout.addWidget(label)
            lineEdit = QtGui.QLineEdit(container)
            sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(lineEdit.sizePolicy().hasHeightForWidth())
            lineEdit.setSizePolicy(sizePolicy)
            lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
            lineEdit.setObjectName("portLineEdit-"+devId)
            lineEdit.setText(port)
            lineEdit.setReadOnly(True)
            horLayout.addWidget(lineEdit)
            horLayout.addItem(spacerItem)
            label = QtGui.QLabel(container)
            label.setFont(font)
            label.setText(QtGui.QApplication.translate("MainWindow", "Device Id", None, QtGui.QApplication.UnicodeUTF8))
            label.setObjectName("label-"+devId)
            horLayout.addWidget(label)
            lineEdit = QtGui.QLineEdit(container)
            lineEdit.setSizePolicy(sizePolicy)
            lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
            lineEdit.setObjectName("devIdLineEdit-"+devId)
            lineEdit.setText(devId)
            lineEdit.setReadOnly(True)
            horLayout.addWidget(lineEdit)
            horLayout.addItem(spacerItem)

            cb = QtGui.QCheckBox(self.singleChannelStartWidget)
            cb.setText(QtGui.QApplication.translate("MainWindow", "", None, QtGui.QApplication.UnicodeUTF8))
            cb.setObjectName("cb_"+devId)
            cb.setChecked(True)
            horLayout.addWidget(cb)
            horLayout.addItem(spacerItem)

    def depopulateDevices(self):
        while(self.devWidgetVLay.itemAt(0)):
            self.devWidgetVLay.removeItem(self.devWidgetVLay.itemAt(0))
            self.singleChannelDeviceComboBox.removeItem(0)
        self.devWidgetContainer.setEnabled(False)

    def initializePlot(self):
        self.pixelPlot, = self.mpl.canvas.ax.plot([],[],'b',linewidth=2)
        self.levelPlot, = self.mpl.canvas.ax.plot([0],[0],'or')
        self.pixelPlot.set_visible(False)
        self.levelPlot.set_visible(False)
        self.mpl.canvas.ax.set_autoscale_on(False)
        self.mpl.canvas.ax.set_position([.125,.15,.8,.75])
        self.mpl.canvas.ax.grid('on')
        self.mpl.canvas.ax.set_xlim(0,ARRAY_SZ)
        self.mpl.canvas.ax.set_ylim(0,AIN_MAX_VOLT)
        self.mpl.canvas.ax.set_xlabel('pixel')
        self.mpl.canvas.ax.set_ylabel('intensity (V)')

    def portLineEditFinished_Callback(self):
        self.port = str(self.portLineEdit.text())

    def connectPressed_Callback(self):
        if not self.devs['connected']:
            self.devWidget.setEnabled(False)
            self.scanPushButton.setEnabled(False)
            self.connectPushButton.setText('Disconnect')
            self.statusbar.showMessage('Connecting... ')

    def populateDeviceTabs(self):
        # Rename the first, pre-existing multi channel tab
        self.multiChannelDeviceTabs.setTabText(self.multiChannelDeviceTabs.indexOf(self.mc_tab1), self.devs['devices'].keys()[0])
        # If more than one device is connected, create additional tabs
        if len(self.devs['devices'])>=2:
            c = 2
            for devId in self.devs['devices'].keys()[1:]:
                tmpTab = QtGui.QWidget()
                tmpTab.setObjectName("mc_tab"+str(c))
                mcwidget = McWidget(tmpTab)
                mcwidget.setGeometry(QtCore.QRect(9, 9, 594, 382))
                sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(mcwidget.sizePolicy().hasHeightForWidth())
                mcwidget.setSizePolicy(sizePolicy)
                mcwidget.setMinimumSize(QtCore.QSize(200, 200))
                mcwidget.setObjectName("mc_"+str(c))
                self.multiChannelDeviceTabs.insertTab(1,tmpTab,devId)
                c+=1

    def connectClicked_Callback(self,port):
        if not self.devs['connected']:
            widget_idx = 0
            for port,devId in zip(self.devs['portList'],self.devs['idList']):
                # Hacky way of retrieving dynamically created checkboxes
                cb = self.devWidgetVLay.itemAt(widget_idx).widget().layout().itemAt(7).widget()
                widget_idx+=1
                if cb.isChecked():
                    try:
                        self.devs['devices'][devId] = ExpressoSerial(port)
                        self.singleChannelDeviceComboBox.addItem(devId)
                    except Exception, e:
                        QtGui.QMessageBox.critical(self,'Error', str(e))
            if len(self.devs['devices'])>0:
                self.devs['connected']=True
                self.populateDeviceTabs()
                self.setWidgetEnabledOnConnect()
            else:
                self.devs['connected']=False
        else:
            self.connectPushButton.setText('Connect')
            try:
                self.cleanUpAndCloseDevices()
                self.depopulateDevices()
                self.setWidgetEnabledOnDisconnect()
            except Exception, e:
                QtGui.QMessageBox.critical(self,'Error', str(e))
            self.devs['connected']=False

    def setWidgetEnabledOnDisconnect(self): 
        self.scanPushButton.setEnabled(True)
        self.devWidget.setEnabled(True)
        self.deviceTab.setEnabled(True)
        self.singleChannelTab.setEnabled(False)
        self.multiChannelTab.setEnabled(False)
        self.singleChannelTab.setEnabled(False)
        self.multiChannelTab.setEnabled(False)
        self.singleChannelStartWidget.setEnabled(False)
        self.singleChannelPixelWidget.setEnabled(False)
        self.singleChannelLevelWidget.setEnabled(False)
        self.multiChannelDeviceTabs.setEnabled(False)
        self.multiChannelStartWidget.setEnabled(False)
        self.statusbar.showMessage('Not Connected')

    def setWidgetEnabledOnConnect(self):
        self.singleChannelTab.setEnabled(True)
        self.multiChannelTab.setEnabled(True)
        self.singleChannelStartWidget.setEnabled(True)
        self.multiChannelStartWidget.setEnabled(True)
        self.multiChannelDeviceTabs.setEnabled(True)
        self.statusbar.showMessage('Connected, Mode = Stopped')

    def clearNormalization_Callback(self):
        chan = self.getCheckedChannelRadioButton()
        devId = str(self.singleChannelDeviceComboBox.currentText())
        dev = self.devs['devices'][devId]
        dev.unSetNormConst(chan-1)

    def setNormalization_Callback(self):
        chan = self.getCheckedChannelRadioButton()
        devId = str(self.singleChannelDeviceComboBox.currentText())
        dev = self.devs['devices'][devId]
        dev.setNormConstFromBuffer(chan-1)

    def saveNormalization_Callback(self):
        chan = self.getCheckedChannelRadioButton()
        devId = str(self.singleChannelDeviceComboBox.currentText())
        dev = self.devs['devices'][devId]
        dev.saveNormConstToFlash(chan-1)

    def loadNormalization_Callback(self):
        chan = self.getCheckedChannelRadioButton()
        devId = str(self.singleChannelDeviceComboBox.currentText())
        dev = self.devs['devices'][devId]
        dev.setNormConstFromFlash(chan-1)

    def getCheckedChannelRadioButton(self):
        for chan in range(1,NUM_CHANNELS+1):
            rb = getattr(self,'channelRadioButton_{0}'.format(chan))
            if rb.isChecked():
                break
        return chan 

    def channelRadioButtonClicked_Callback(self):
        chan = self.getCheckedChannelRadioButton()
        devId = str(self.singleChannelDeviceComboBox.currentText())
        dev = self.devs['devices'][devId]
        dev.setChannel(chan-1)
        self.tLast = None

    def singleChannelStart_Callback(self):
        if self.timerSingleChannel.isActive():
            # Stop single channel mode. 
            self.timerSingleChannel.stop()
            self.singleChannelPixelWidget.setEnabled(False)
            self.singleChannelLevelWidget.setEnabled(False)
            self.singleChannelDeviceComboBox.setEnabled(True)
            self.multiChannelTab.setEnabled(True)
            self.deviceTab.setEnabled(True)
            self.singleChannelStart.setText('Start')
            self.clearSingleChanProgressBar()
            self.statusbar.showMessage('Connected, Mode = Stopped')
            self.pixelPlot.set_visible(False)
            self.levelPlot.set_visible(False)
            self.mpl.canvas.fig.canvas.draw()
            devId = str(self.singleChannelDeviceComboBox.currentText())
            dev = self.devs['devices'][devId]
            dev.setModeStopped()
        else:
            # Start single channel mode - stream in level and pixel data
            # from single sensor

            # Current Expresso Id
            devId = str(self.singleChannelDeviceComboBox.currentText())
            dev = self.devs['devices'][devId]
            dev.setModeSingleChannel()
            chan = self.getCheckedChannelRadioButton()
            self.tLast = None
            self.singleChannelPixelWidget.setEnabled(True)
            self.singleChannelLevelWidget.setEnabled(True)
            self.singleChannelDeviceComboBox.setEnabled(False)
            self.multiChannelTab.setEnabled(False)
            self.deviceTab.setEnabled(False)
            self.singleChannelStart.setText('Stop')
            self.statusbar.showMessage('Connected, Mode = Single Channel')
            self.pixelPlot.set_visible(True)
            self.levelPlot.set_visible(True)
            self.timerSingleChannel.start()

    def setupTimers(self):
        """
        Setup timer object
        """
        # Timer for single channel mode
        self.timerSingleChannel = QtCore.QTimer()
        self.timerSingleChannel.setInterval(TIMER_SINGLE_INTERVAL_MS)
        self.timerSingleChannel.timeout.connect(self.timerSingleChannel_Callback)

        # Timer for multi channel mode
        self.timerMultiChannel = QtCore.QTimer()
        self.timerMultiChannel.setInterval(TIMER_MULTI_INTERVAL_MS)
        self.timerMultiChannel.timeout.connect(self.timerMultiChannel_Callback)

    def timerSingleChannel_Callback(self):
        """
        Note, we might want to make this a command and response type callback
        like the multiChannel callback.  This is because we occasionally catch
        the microcontroller when it is busy and it take a little while 200ms
        for it to respond. Not a high priority at the moment as it works well
        enought to suit its purpose.
        """
        # Get fluid level and pixel data
        try:
            devId = str(self.singleChannelDeviceComboBox.currentText())
            dev = self.devs['devices'][devId]
            pixelLevel, data = dev.getPixelData()
        except AttributeError, e:
            return
        fluidLevel = self.pixelToFluidLevel(pixelLevel)
        data = self.analogInputToVolt(data)

        # Fluid level
        chan = self.getCheckedChannelRadioButton()

        # Plot pixel data
        self.pixelPlot.set_data(self.pixelPosArray,data)

        # Plot level data and set progress bar value
        if pixelLevel >= 0:
            pixelLevel = int(pixelLevel)
            fluidLevel = int(fluidLevel)
            self.levelPlot.set_xdata([pixelLevel])
            self.levelPlot.set_ydata([data[pixelLevel]])
            self.levelPlot.set_visible(True)
            self.setSingleChanProgressBar(fluidLevel)
        else:
            self.levelPlot.set_visible(False)
            self.clearSingleChanProgressBar()
        self.mpl.canvas.fig.canvas.draw()

    def multiChannelStart_Callback(self):

        if self.timerMultiChannel.isActive():
            devId = str(self.singleChannelDeviceComboBox.currentText())
            dev = self.devs['devices'][devId]
            # Multi channel mode stop
            self.timerMultiChannel.stop()
            if self.multiChannelState == 'rsp':
                dev.getLevels_Rsp()
            self.multiChannelStart.setText('Start')
            self.statusbar.showMessage('Connected, Mode = Stopped')
            self.clearAllMultiChanProgressBar()
            self.deviceTab.setEnabled(True)
            self.singleChannelTab.setEnabled(True)
            self.logFileWidget.setEnabled(True)
            self.loggingCheckBox.setEnabled(True)
            dev.setModeStopped()
            self.multiChannelTimeLabel.setText('____ s')
            self.tStart = None
            if self.loggingCheckBox.isChecked():
                del self.logger
                self.logger = None
        else:
            # If logging is turned on create log file
            if self.loggingCheckBox.isChecked():
                if not self.createLogFile():
                    return
            # Multi channel mode start
            devId = str(self.singleChannelDeviceComboBox.currentText())
            dev = self.devs['devices'][devId]
            dev.setModeMultiChannel()
            self.deviceTab.setEnabled(False)
            self.singleChannelTab.setEnabled(False)
            self.logFileWidget.setEnabled(False)
            self.loggingCheckBox.setEnabled(False)
            self.multiChannelStart.setText('Stop')
            self.statusbar.showMessage('Connected, Mode = Multi Channel')
            self.multiChannelState = 'cmd'
            self.tStart = time.time()
            self.timerMultiChannel.start()

    def createLogFile(self):
        if  os.path.exists(self.logPath):
            # Check if log path is a regular file - if not error and exit
            if not os.path.isfile(self.logPath):
                errMsgTitle = 'Log File Error'
                errMsg = ['Unable to create log file.']
                errMsg.append('Path, {0}, exists and is not file.'.format(self.logPath))
                errMsg = '\n'.join(errMsg)
                QtGui.QMessageBox.critical(self,errMsgTitle, errMsg)
                return False

            # Log path is a regular file - check if user wants to overwrite
            qstMsgTitle = 'Log File Exists'
            qstMsg = 'Log file, {0}, already exists.'.format(self.logPath)
            buttonDict = {'Overwrite': 0, 'Cancel': 1}
            answer = QtGui.QMessageBox.question(self,qstMsgTitle,qstMsg,'Overwrite', 'Cancel')
            if answer == buttonDict['Cancel']:
                return

        # User is Ok overwriting log file or it doesn't exist yet. 
        self.logger = HDF5_Logger(self.logPath,mode='w')
        self.logger.add_datetime('/','datetime')
        self.logger.add_dataset('/sample_t',(1,))
        self.logger.add_attribute('/sample_t', 'unit', 's')
        deviceName = 'device_1'
        self.logger.add_group('/{0}'.format(deviceName))
        for i in range(1,NUM_CHANNELS+1):
            datasetName = '/{0}/channel_{1}'.format(deviceName, i)
            self.logger.add_dataset(datasetName, (1,))
            self.logger.add_attribute(datasetName, 'unit', 'nl')
        return True

    def timerMultiChannel_Callback(self): 
        """
        Note, the multi channel callback consists of two alternating states,
        cmd and rsp. In the cmd state a request for the fluid levels is sent to
        the devices. In the rsp state the fluid level response is read from the
        device.
        """
        # Get time information
        t = time.time()
        tRun = t - self.tStart
        self.multiChannelTimeLabel.setText('{0} s'.format(int(math.floor(tRun))))
        self.multiChannelTimeLabel.repaint()

        # Get fluid level from sensors
        devId = str(self.singleChannelDeviceComboBox.currentText())
        dev = self.devs['devices'][devId]
        if self.multiChannelState == 'cmd':
            try:
                dev.getLevels_Cmd()
            except AttributeError, e:
                return
            self.multiChannelState = 'rsp'
        else:
            try:
                #pixelLevelList = self.dev.getLevels()
                pixelLevelList = dev.getLevels_Rsp()
            except AttributeError, e:
                return
            self.multiChannelState = 'cmd'

            fluidLevelList = []
            for pixelLevel in pixelLevelList:
                if pixelLevel>=0:
                    fluidLevel = self.pixelToFluidLevel(pixelLevel)
                else:
                    fluidLevel = pixelLevel
                fluidLevelList.append(fluidLevel)

            if len(fluidLevelList) == 0:
                fluidLevelList = [-1 for i in range(NUM_CHANNELS)]
            for i, fluidLevel in enumerate(fluidLevelList):
                if fluidLevel >= 0: 
                    self.setMultiChanProgressBar(i+1,fluidLevel)
                else: 
                    self.clearMultiChanProgressBar(i+1)

            # Log data
            deviceName = 'device_1'
            if self.loggingCheckBox.isChecked():
                self.logger.add_dataset_value('/sample_t',tRun) 
                for i, level in enumerate(fluidLevelList):
                    #if level < 0:
                        #level = numpy.nan
                    dsetName = '/{0}/channel_{1}'.format(deviceName,i+1)
                    self.logger.add_dataset_value(dsetName,level)

    def setLogFile_Callback(self):
        # Get log file
        filename = QtGui.QFileDialog.getSaveFileName(
                None,
                'Select log file',
                self.lastLogDir,
                options = QtGui.QFileDialog.DontConfirmOverwrite,
                )
        filename = str(filename)

        if filename:
            # Ensure the the log file has the standard file extension
            basename, ext = os.path.splitext(filename)
            if ext != LOG_FILE_EXT:
                filename = '{0}{1}'.format(basename,LOG_FILE_EXT)

            # Set new log file
            self.logPath = filename
            self.lastLogDir =  os.path.split(filename)[0]
            self.logFileLabel.setText('{0}'.format(self.logPath))


    def pixelToFluidLevel(self,pixelLevel):
        """
        Converts the level from pixel position to fluid level in nl.
        """
        return (MAX_PIXEL-pixelLevel)*MM2NL*PIXEL2MM

    def analogInputToVolt(self,data):
        """
        Converts raw analog input values to voltages.
        """
        return data*PIXEL_TO_VOLT

    def getMultiChanProgressBar(self,num,widget):
            return getattr(widget, 'multiChannelProgressBar_{0}'.format(num+5))

    def clearProgressBar(self,progressBar):
        msg = 'no data'
        progressBar.setFormat(msg)
        progressBar.setValue(0)

    def clearMultiChanProgressBar(self,num,widget):
        progressBar = self.getMultiChanProgressBar(num,widget)
        self.clearProgressBar(progressBar)

    def clearAllMultiChanProgressBar(self):
        widgets = self.getMultiChanWidgets()
        for widget in widgets:
            for i in range(1,NUM_CHANNELS+1):
                self.clearMultiChanProgressBar(i,widget)

    def clearSingleChanProgressBar(self):
        self.clearProgressBar(self.singleChannelProgressBar)

    def clearAllProgressBar(self):
        self.clearSingleChanProgressBar()
        self.clearAllMultiChanProgressBar()

    def setProgressBar(self,progressBar, value): 
        valueStr = '{0:04d} nl'.format(int(value))
        progressBar.setFormat(valueStr)
        progressBar.setValue(value)

    def setMultiChanProgressBar(self, num, value, widget):
        progressBar = self.getMultiChanProgressBar(num, widget)
        self.setProgressBar(progressBar, value)

    def setSingleChanProgressBar(self,value):
        self.setProgressBar(self.singleChannelProgressBar,value)

    def setProgressBarRange(self,progressBar):
        progressBar.setRange(0,CAPILLARY_VOLUME)

    def setSingleChanProgressBarRange(self):
        self.setProgressBarRange(self.singleChannelProgressBar)

    def setMultiChanProgressBarRange(self,i,widget): 
        progressBar = self.getMultiChanProgressBar(i,widget)
        self.setProgressBarRange(progressBar)

    def setAllMultiChanProgressBarRange(self):
        widgets = self.getMultiChanWidgets()
        for widget in widgets:
            for i in range(1,NUM_CHANNELS+1):
                self.setMultiChanProgressBarRange(i,widget)

    def setAllProgressBarRange(self):
        self.setAllMultiChanProgressBarRange()
        self.setSingleChanProgressBarRange()

    def setMultiChanProgressBarFont(self,i,widget):
        progressBar = self.getMultiChanProgressBar(i,widget)
        self.setProgressBarFont(progressBar)
    
    def getMultiChanWidgets(self):
        if len(self.devs['devices'])==0:
            return [self.mc_1]

    def setAllMultiChanProgressBarFont(self):
        widgets = self.getMultiChanWidgets()
        for widget in widgets:
            for i in range(1,NUM_CHANNELS+1):
                self.setMultiChanProgressBarFont(i,widget)

    def setSingleChanProgressBarFont(self):
        self.setProgressBarFont(self.singleChannelProgressBar)

    def setAllProgressBarFont(self):
        self.setSingleChanProgressBarFont()
        self.setAllMultiChanProgressBarFont()

    def setProgressBarFont(self, progressBar):
        # Only on windows .... can leave this the same on linux.  Or could move
        # to separate text box.
        font = QtGui.QFont("monospace")
        font.setStyleHint(QtGui.QFont.TypeWriter)
        font.setBold(True)
        progressBar.setFont(font)


def expressoMain():
    app = QtGui.QApplication(sys.argv)
    mainWindow = ExpressoMainWindow()
    mainWindow.main()
    app.exec_()

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    expressoMain()
