from __future__ import print_function
import sys
import functools
import pylab
import time
import array_reader
from PyQt4 import QtCore
from PyQt4 import QtGui
from optical_sensor_gui_ui import Ui_MainWindow 

STOPPED = 0
RUNNING = 1

DFLT_PORT = '/dev/ttyACM0'

TIMER_SINGLE_INTERVAL_MS =  300 
TIMER_MULTI_INTERVAL_MS =  500 

MM2NL = 5.0e3/54.8
PIXEL2MM = 63.5e-3
AIN_MAX_VOLT= 3.3
PIXEL_TO_VOLT = AIN_MAX_VOLT/float(255)
CAPILLARY_VOLUME = PIXEL2MM*MM2NL*array_reader.ARRAY_SZ


class OpticalSensorMainWindow(QtGui.QMainWindow,Ui_MainWindow):

    def __init__(self,parent=None):
        super(OpticalSensorMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
        self.initialize()
        self.setupTimers()

        # Testing --------------- 
        self.t_last = None
        # -----------------------

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

        # Actions for widgets on the multi channel mode tab
        self.multiChannelStart.clicked.connect(self.multiChannelStart_Callback)
        #self.logMultiChannel.clicked.connect(self.logMultiChannel_Callback)

    def initialize(self):
        # ####################################
        # Note, set default port based on OS
        # ####################################
        self.dev = None
        self.port = DFLT_PORT
        self.portLineEdit.setText(self.port)
        self.statusbar.showMessage('Not Connected')

        #self.multiChannelState = STOPPED
        self.channelRadioButton_1.setChecked(True)
        self.singleChannelDeviceComboBox.addItem('Device 1')

        # Set progressbar ranges 
        self.setAllProgressBarRange()
        self.clearAllProgressBar()

        # Initialize plot and array for sensor data
        self.initializePlot()
        self.pixelPosArray = pylab.arange(0,array_reader.ARRAY_SZ)
            
        # Set Enabled state of widgets for startup.
        self.setWidgetEnabledOnDisconnect()

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
        self.singleChannelPixelBox.setEnabled(False)
        self.singleChannelLevelBox.setEnabled(False)
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

    def getCheckedChannelRadioButton(self):
        for chan in range(1,array_reader.NUM_CHANNELS+1):
            rb = getattr(self,'channelRadioButton_{0}'.format(chan))
            if rb.isChecked():
                break
        return chan 

    def channelRadioButtonClicked_Callback(self):
        chan = self.getCheckedChannelRadioButton()
        self.dev.setChannel(chan-1)

    def singleChannelStart_Callback(self):
        if self.timerSingleChannel.isActive():
            # Stop single channel mode. 
            self.timerSingleChannel.stop()
            self.singleChannelPixelBox.setEnabled(False)
            self.singleChannelLevelBox.setEnabled(False)
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
            self.singleChannelPixelBox.setEnabled(True)
            self.singleChannelLevelBox.setEnabled(True)
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
        
        ## Testing Compute timer dt 
        ## ------------------------
        #t0 = time.time()
        #if self.t_last is not None:
        #    dt = t0 - self.t_last
        #    print(dt)
        #self.t_last = t0
        ## ------------------------

        try:
            pixelLevel, data = self.dev.getPixelData()
        except AttributeError:
            return 

        fluidLevel = self.pixelToFluidLevel(pixelLevel)
        data = self.analogInputToVolt(data)

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
            # Multi channel mode stop
            self.timerMultiChannel.stop()
            self.multiChannelStart.setText('Start')
            self.statusbar.showMessage('Connected, Mode = Stopped')
            self.clearAllMultiChanProgressBar()
            self.deviceTab.setEnabled(True)
            self.singleChannelTab.setEnabled(True)
            self.logFileWidget.setEnabled(True)
            self.loggingCheckBox.setEnabled(True)
            self.dev.setModeStopped()
        else:
            # Multi channel mode start
            self.dev.setModeMultiChannel()
            self.deviceTab.setEnabled(False)
            self.singleChannelTab.setEnabled(False)
            self.logFileWidget.setEnabled(False)
            self.loggingCheckBox.setEnabled(False)
            self.multiChannelStart.setText('Stop')
            self.statusbar.showMessage('Connected, Mode = Multi Channel')
            self.timerMultiChannel.start()

    def timerMultiChannel_Callback(self):
        pixelLevelList = self.dev.getLevels()
        fluidLevelList = map(self.pixelToFluidLevel, pixelLevelList)
        if fluidLevelList is None:
            fluidLevelList = [-1 for i in range(array_reader.NUM_CHANNELS)]
        for i, fluidLevel in enumerate(fluidLevelList):
            if fluidLevel >= 0: 
                self.setMultiChanProgressBar(i+1,fluidLevel)
            else: 
                self.clearMultiChanProgressBar(i+1)


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
        progressBar.setFormat(r'no data')
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
        progressBar.setFormat(r'%v nl') 
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


def opticalSensorMain():
    app = QtGui.QApplication(sys.argv)
    mainWindow = OpticalSensorMainWindow()
    mainWindow.main()
    app.exec_()

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    opticalSensorMain()
