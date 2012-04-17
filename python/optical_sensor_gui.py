from __future__ import print_function
import os
import sys
import functools
import numpy 
import time
import math
import platform
import array_reader
from PyQt4 import QtCore
from PyQt4 import QtGui
from optical_sensor_gui_ui import Ui_MainWindow 
from lowpass_filter import LowpassFilter
from hdf5_logger import HDF5_Logger

# Constants
TIMER_SINGLE_INTERVAL_MS =  300 
TIMER_MULTI_INTERVAL_MS =  250 
LOWPASS_FREQ_CUTOFF = 0.5 
MM2NL = 5.0e3/54.8
PIXEL2MM = 63.5e-3
AIN_MAX_VOLT= 3.3
PIXEL_TO_VOLT = AIN_MAX_VOLT/float(255)
CAPILLARY_VOLUME = PIXEL2MM*MM2NL*array_reader.ARRAY_SZ
LOG_FILE_EXT = '.hdf5'
DEFAULT_LOG_FILE = 'expresso_default_log{0}'.format(LOG_FILE_EXT)
LEVEL_MSG_LEN = 7

class OpticalSensorMainWindow(QtGui.QMainWindow,Ui_MainWindow):

    def __init__(self,parent=None):
        super(OpticalSensorMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
        self.initialize()
        self.setupTimers()

    def main(self):
        self.show()

    def closeEvent(self,event):
        if self.dev is not None:
            self.cleanUpAndCloseDevice()
        event.accept()

    def cleanUpAndCloseDevice(self):
        self.dev.setModeStopped()
        self.dev.setChannel(0)
        self.dev.close()
        self.dev = None
        
    def connectActions(self):
        # Device Manager tab
        self.portLineEdit.editingFinished.connect(self.portLineEditFinished_Callback)
        self.connectPushButton.pressed.connect(self.connectPressed_Callback)
        self.connectPushButton.clicked.connect(self.connectClicked_Callback)

        # Actions for widgets on the single channel tab
        for chan in range(1,array_reader.NUM_CHANNELS+1):
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

    def initialize(self):
        self.dev = None
        # Set default com port
        osType = platform.system()
        if osType == 'Linux': 
            self.port = '/dev/ttyACM0' 
        else: 
            self.port = 'com1'
        self.portLineEdit.setText(self.port)
        self.statusbar.showMessage('Not Connected')

        self.singleChannelDeviceComboBox.addItem('Device 1')
        self.channelRadioButton_1.setChecked(True)

        # Set progressbar ranges 
        self.setAllProgressBarFont()
        self.setAllProgressBarRange()
        self.clearAllProgressBar()

        # Initialize plot and array for sensor data
        self.initializePlot()
        self.pixelPosArray = numpy.arange(0,array_reader.ARRAY_SZ)
            
        # Set Enabled state of widgets for startup.
        self.setWidgetEnabledOnDisconnect()

        # Setup lowpass filters
        self.lowpassFilter = []
        for chan in range(array_reader.NUM_CHANNELS):
            self.lowpassFilter.append(LowpassFilter(LOWPASS_FREQ_CUTOFF))
        self.tLast = None

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

    def initializePlot(self):
        self.pixelPlot, = self.mpl.canvas.ax.plot([],[],'b',linewidth=2)
        self.levelPlot, = self.mpl.canvas.ax.plot([0],[0],'or')
        self.pixelPlot.set_visible(False)
        self.levelPlot.set_visible(False)
        self.mpl.canvas.ax.set_autoscale_on(False)
        self.mpl.canvas.ax.set_position([.125,.15,.8,.75])
        self.mpl.canvas.ax.grid('on')
        self.mpl.canvas.ax.set_xlim(0,array_reader.ARRAY_SZ)
        self.mpl.canvas.ax.set_ylim(0,AIN_MAX_VOLT)
        self.mpl.canvas.ax.set_xlabel('pixel')
        self.mpl.canvas.ax.set_ylabel('intensity (V)')

    def portLineEditFinished_Callback(self):
        self.port = str(self.portLineEdit.text())

    def connectPressed_Callback(self):
        if self.dev == None:
            self.connectPushButton.setText('Disconnect')
            self.portLineEdit.setEnabled(False)
            self.statusbar.showMessage('Connecting ... ')

    def connectClicked_Callback(self):
        if self.dev == None:
            try:
                self.dev = array_reader.ArrayReader(self.port)
                connected = True
            except Exception, e:
                QtGui.QMessageBox.critical(self,'Error', str(e))
                self.connectPushButton.setText('Connect')
                self.statusbar.showMessage('Not Connected')
                self.portLineEdit.setEnabled(True)
                connected = False
        else:
            self.connectPushButton.setText('Connect')
            try:
                self.cleanUpAndCloseDevice()
            except Exception, e:
                QtGui.QMessageBox.critical(self,'Error', str(e))
            connected = False

        if connected:
            chan = self.getCheckedChannelRadioButton()
            self.dev.setChannel(chan-1)
            self.setWidgetEnabledOnConnect()
        else:
            self.setWidgetEnabledOnDisconnect()

    def setWidgetEnabledOnDisconnect(self): 
        self.deviceTab.setEnabled(True)
        self.portLineEdit.setEnabled(True)
        self.singleChannelTab.setEnabled(False)
        self.multiChannelTab.setEnabled(False)
        self.singleChannelTab.setEnabled(False)
        self.multiChannelTab.setEnabled(False)
        self.singleChannelStartWidget.setEnabled(False)
        self.singleChannelPixelWidget.setEnabled(False)
        self.singleChannelLevelWidget.setEnabled(False)
        self.multiChannelDeviceTabWidget.setEnabled(False)
        self.multiChannelStartWidget.setEnabled(False)
        self.statusbar.showMessage('Not Connected')

    def setWidgetEnabledOnConnect(self):
        self.singleChannelTab.setEnabled(True)
        self.multiChannelTab.setEnabled(True)
        self.singleChannelStartWidget.setEnabled(True)
        self.multiChannelStartWidget.setEnabled(True)
        self.multiChannelDeviceTabWidget.setEnabled(True)
        self.statusbar.showMessage('Connected, Mode = Stopped')

    def clearNormalization_Callback(self):
        chan = self.getCheckedChannelRadioButton()
        self.dev.unSetNormConst(chan-1)

    def setNormalization_Callback(self):
        chan = self.getCheckedChannelRadioButton()
        self.dev.setNormConstFromBuffer(chan-1)

    def saveNormalization_Callback(self):
        chan = self.getCheckedChannelRadioButton()
        self.dev.saveNormConstToFlash(chan-1)

    def loadNormalization_Callback(self):
        chan = self.getCheckedChannelRadioButton()
        self.dev.setNormConstFromFlash(chan-1)

    def getCheckedChannelRadioButton(self):
        for chan in range(1,array_reader.NUM_CHANNELS+1):
            rb = getattr(self,'channelRadioButton_{0}'.format(chan))
            if rb.isChecked():
                break
        return chan 

    def channelRadioButtonClicked_Callback(self):
        chan = self.getCheckedChannelRadioButton()
        self.dev.setChannel(chan-1)
        self.lowpassFilter[chan-1].value = None 
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
            self.dev.setModeStopped()
        else:
            # Start single channel mode - stream in level and pixel data
            # from single sensor
            self.dev.setModeSingleChannel()
            chan = self.getCheckedChannelRadioButton()
            self.lowpassFilter[chan-1].value = None 
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

        # Get dt for lowpass filter
        t = time.time()
        if self.tLast is not None:
            dt = t - self.tLast
        else:
            dt = 0.0
        self.tLast = t
        print(dt)

        # Get fluid level and pixel data
        try:
            pixelLevel, data = self.dev.getPixelData()
        except AttributeError, e:
            return
        fluidLevel = self.pixelToFluidLevel(pixelLevel)
        data = self.analogInputToVolt(data)

        # Lowpass filter fluid level
        chan = self.getCheckedChannelRadioButton()
        self.lowpassFilter[chan-1].update(fluidLevel,dt)
        fluidLevelLowpass = self.lowpassFilter[chan-1].value

        # Plot pixel data
        self.pixelPlot.set_data(self.pixelPosArray,data)

        # Plot level data and set progress bar value
        if pixelLevel >= 0:
            pixelLevel = int(pixelLevel)
            fluidLevel = int(fluidLevel)
            fluidLevelLowpass = int(fluidLevelLowpass)
            self.levelPlot.set_xdata([pixelLevel])
            self.levelPlot.set_ydata([data[pixelLevel]])
            self.levelPlot.set_visible(True)
            self.setSingleChanProgressBar(fluidLevelLowpass)
        else:
            self.levelPlot.set_visible(False)
            self.clearSingleChanProgressBar()
        self.mpl.canvas.fig.canvas.draw()

    def multiChannelStart_Callback(self):

        if self.timerMultiChannel.isActive():
            # Multi channel mode stop
            self.timerMultiChannel.stop()
            if self.multiChannelState == 'rsp':
                self.dev.getLevels_Rsp()
            self.multiChannelStart.setText('Start')
            self.statusbar.showMessage('Connected, Mode = Stopped')
            self.clearAllMultiChanProgressBar()
            self.deviceTab.setEnabled(True)
            self.singleChannelTab.setEnabled(True)
            self.logFileWidget.setEnabled(True)
            self.loggingCheckBox.setEnabled(True)
            self.dev.setModeStopped()
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
            self.dev.setModeMultiChannel()
            self.deviceTab.setEnabled(False)
            self.singleChannelTab.setEnabled(False)
            self.logFileWidget.setEnabled(False)
            self.loggingCheckBox.setEnabled(False)
            self.multiChannelStart.setText('Stop')
            self.statusbar.showMessage('Connected, Mode = Multi Channel')
            self.multiChannelState = 'cmd'
            # Initialize lowpass filters
            for i in range(array_reader.NUM_CHANNELS):
                self.lowpassFilter[i].value = None
            self.tLast = None
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
        for i in range(1,array_reader.NUM_CHANNELS+1):
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
        if self.multiChannelState == 'cmd':
            try:
                self.dev.getLevels_Cmd()
            except AttributeError, e:
                return
            self.multiChannelState = 'rsp'
        else:
            try:
                #pixelLevelList = self.dev.getLevels()
                pixelLevelList = self.dev.getLevels_Rsp()
            except AttributeError, e:
                return
            self.multiChannelState = 'cmd'
            fluidLevelList = map(self.pixelToFluidLevel, pixelLevelList)

            if self.tLast is not None:
                dt = t - self.tLast
            else:
                dt = 0.0
            self.tLast = t
            print(dt)

            # Lowpass filter fluid levels and update progress bars
            fluidLevelLowpassList = []
            if fluidLevelList is None:
                fluidLevelList = [-1 for i in range(array_reader.NUM_CHANNELS)]
            for i, fluidLevel in enumerate(fluidLevelList):
                self.lowpassFilter[i].update(fluidLevel,dt)
                fluidLevelLowpass = self.lowpassFilter[i].value
                fluidLevelLowpassList.append(fluidLevelLowpass)
                if fluidLevel >= 0: 
                    self.setMultiChanProgressBar(i+1,fluidLevelLowpass)
                else: 
                    self.clearMultiChanProgressBar(i+1)

            # Log data
            deviceName = 'device_1'
            if self.loggingCheckBox.isChecked():
                self.logger.add_dataset_value('/sample_t',tRun) 
                for i, level in enumerate(fluidLevelLowpassList):
                    if level < 0:
                        level = numpy.nan
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
        return pixelLevel*MM2NL*PIXEL2MM

    def analogInputToVolt(self,data):
        """
        Converts raw analog input values to voltages.
        """
        return data*PIXEL_TO_VOLT

    def getMultiChanProgressBar(self,num):
        return getattr(self, 'multiChannelProgressBar_{0}'.format(num))

    def clearProgressBar(self,progressBar):
        msg = 'no data'
        progressBar.setFormat(msg)
        progressBar.setValue(0)

    def clearMultiChanProgressBar(self,num):
        progressBar = self.getMultiChanProgressBar(num)
        self.clearProgressBar(progressBar)

    def clearAllMultiChanProgressBar(self):
        for i in range(1,array_reader.NUM_CHANNELS+1):
            self.clearMultiChanProgressBar(i)

    def clearSingleChanProgressBar(self):
        self.clearProgressBar(self.singleChannelProgressBar)

    def clearAllProgressBar(self):
        self.clearSingleChanProgressBar()
        self.clearAllMultiChanProgressBar()

    def setProgressBar(self,progressBar, value): 
        valueStr = '{0:04d} nl'.format(int(value))
        progressBar.setFormat(valueStr)
        progressBar.setValue(value)

    def setMultiChanProgressBar(self, num, value):
        progressBar = self.getMultiChanProgressBar(num)
        self.setProgressBar(progressBar, value)

    def setSingleChanProgressBar(self,value):
        self.setProgressBar(self.singleChannelProgressBar,value)

    def setProgressBarRange(self,progressBar):
        progressBar.setRange(0,CAPILLARY_VOLUME)

    def setSingleChanProgressBarRange(self):
        self.setProgressBarRange(self.singleChannelProgressBar)

    def setMultiChanProgressBarRange(self,i): 
        progressBar = self.getMultiChanProgressBar(i)
        self.setProgressBarRange(progressBar)

    def setAllMultiChanProgressBarRange(self):
        for i in range(1,array_reader.NUM_CHANNELS+1):
            self.setMultiChanProgressBarRange(i)

    def setAllProgressBarRange(self):
        self.setAllMultiChanProgressBarRange()
        self.setSingleChanProgressBarRange()

    def setMultiChanProgressBarFont(self,i):
        progressBar = self.getMultiChanProgressBar(i)
        self.setProgressBarFont(progressBar)

    def setAllMultiChanProgressBarFont(self):
        for i in range(1,array_reader.NUM_CHANNELS+1):
            self.setMultiChanProgressBarFont(i)

    def setSingleChanProgressBarFont(self):
        self.setProgressBarFont(self.singleChannelProgressBar)

    def setAllProgressBarFont(self):
        self.setSingleChanProgressBarFont()
        self.setAllMultiChanProgressBarFont()

    def setProgressBarFont(self, progressBar):
        font = QtGui.QFont("monospace")
        font.setStyleHint(QtGui.QFont.TypeWriter)
        font.setBold(True)
        progressBar.setFont(font)


def opticalSensorMain():
    app = QtGui.QApplication(sys.argv)
    mainWindow = OpticalSensorMainWindow()
    mainWindow.main()
    app.exec_()

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    opticalSensorMain()
