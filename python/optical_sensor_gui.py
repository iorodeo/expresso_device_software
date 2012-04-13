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

        self.t_last = None

    def closeEvent(self,event):
        if self.dev is not None:
            self.cleanUpAndCloseDevice()
        event.accept()
        
    def connectActions(self):

        # Device Manager tab
        self.portLineEdit.editingFinished.connect(self.portLineEditFinished_Callback)
        self.connectPushButton.pressed.connect(self.connectPressed_Callback)
        self.connectPushButton.clicked.connect(self.connectClicked_Callback)

        # Single channel mode tab
        for chan in range(1,array_reader.NUM_CHANNELS+1):
            radioButton = getattr(self,'channelRadioButton_{0}'.format(chan))
            radioButton.clicked.connect(self.channelRadioButtonClicked_Callback)
        self.singleChannelStart.clicked.connect(self.singleChannelStart_Callback)

        ## Multi channel mode tab
        #self.multiChannelStart.clicked.connect(self.multiChannelStart_Callback)

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
        self.singleChannelProgressBar.setRange(0,CAPILLARY_VOLUME)
        for i in range(1,6):
            progressBar = getattr(self,'multiChannelProgressBar_{0}'.format(i))
            progressBar.setRange(0,CAPILLARY_VOLUME) 

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
            self.timerSingleChannel.stop()
            self.singleChannelPixelBox.setEnabled(False)
            self.singleChannelLevelBox.setEnabled(False)
            self.singleChannelStart.setText('Start')
            self.multiChannelStartWidget.setEnabled(True)
            self.singleChannelProgressBar.setFormat(r'no data')
            self.singleChannelProgressBar.setValue(0)
            self.statusbar.showMessage('Connected, Mode = Stopped')
        else:
            self.dev.setModeSingleChannel()
            self.timerSingleChannel.start()
            self.singleChannelPixelBox.setEnabled(True)
            self.singleChannelLevelBox.setEnabled(True)
            self.singleChannelStart.setText('Stop')
            self.multiChannelStartWidget.setEnabled(False)
            self.statusbar.showMessage('Connected, Mode = Single Channel')

    def setupTimers(self):
        """
        Setup timer object
        """
        self.timerSingleChannel = QtCore.QTimer()
        self.timerSingleChannel.setInterval(TIMER_SINGLE_INTERVAL_MS)
        self.timerSingleChannel.timeout.connect(self.timerSingleChannel_Callback)

        #self.timerMultiChannel = QtCore.QTimer()
        #self.timerMultiChannel.setInterval(TIMER_MULTI_INTERVAL_MS)
        #self.timerMultiChannel.timeout.connect(self.timerMultiChannel_Callback)

    def timerSingleChannel_Callback(self):
        
        t0 = time.time()
        if self.t_last is not None:
            dt = t0 - self.t_last
            print(dt)
        self.t_last = t0

        pixelLevel, data = self.dev.getPixelData()
        fluidLevel = pixelLevel*MM2NL*PIXEL2MM
        data = data*PIXEL_TO_VOLT
        #print(fluidLevel)

        # Plot pixel data
        self.pixelPlot.set_visible(True)
        self.pixelPlot.set_data(self.pixelPosArray,data)

        # Plot level data and set progress bar value
        if pixelLevel >= 0:
            pixelLevel = int(pixelLevel)
            fluidLevel = int(fluidLevel)
            self.levelPlot.set_xdata([pixelLevel])
            self.levelPlot.set_ydata([data[pixelLevel]])
            self.levelPlot.set_visible(True)
            self.singleChannelProgressBar.setFormat(r'%v nl')
            self.singleChannelProgressBar.show()
            self.singleChannelProgressBar.setValue(fluidLevel)
        else:
            self.levelPlot.set_visible(False)
            self.singleChannelProgressBar.setFormat(r'no data')
            self.singleChannelProgressBar.setValue(0)

        self.mpl.canvas.show()
        self.mpl.canvas.fig.canvas.draw()

        t1 = time.time()
        dt = t1-t0
        #print(dt)
#
#    def timerMultiChannel_Callback(self):
#        if self.timerMultiChannel.isActive():
#            pixelLevelList = self.dev.getLevels()
#            if pixelLevelList is not None:
#                for i, pixelLevel in enumerate(pixelLevelList):
#                    pb = getattr(self,'multiChannelProgressBar_{0}'.format(i+1))
#                    fluidLevel = pixelLevel*PIXEL2MM*MM2NL
#                    if fluidLevel >= 0:
#                        pb.setFormat(r'%v nl')
#                        pb.show()
#                        pb.setValue(fluidLevel)
#                    else:
#                        pb.setFormat(r'no data')
#                        pb.setValue(0)
#            else:

#                for i in range(array_reader.NUM_CHANNELS):
#                    pb.setFormat(r'no data')
#                    pb.setValue(0)
#
#
#
#    def multiChannelStart_Callback(self):
#        if (self.multiChannelState==STOPPED):
#            self.timerMultiChannel.start()
#            rsp = self.dev.setMode(array_reader.MODE_MULTI_CHANNEL)
#            self.multiChannelStart.setText('Stop')
#            self.multiChannelState = RUNNING 
#            self.logMultiChannel.setEnabled(True)
#            return
#
#        if (self.multiChannelState==RUNNING):
#            self.timerMultiChannel.stop()
#            self.logMultiChannel.setDisabled(True)
#            self.multiChannelStart.setText('Start')
#            self.multiChannelState = STOPPED
#            for i in range(array_reader.NUM_CHANNELS):
#                pb = getattr(self,'multiChannelProgressBar_{0}'.format(i+1))
#                pb.setFormat(r'no data')
#                pb.setValue(0)
#
#            

#    def logMultiChannel_Callback(self):
#        pass
#    


#    def setWidgetEnableOnConnect(self):
#        if (self.tabWidget.currentIndex()==SINGLE_CHANNEL_TAB):
#            self.portLineEdit.setEnabled(False)
#            for i in range(array_reader.NUM_CHANNELS):
#                rb = getattr(self,'channelRadioButton_{0}'.format(i+1))
#                rb.setEnabled(True)
#            
#
#        if (self.tabWidget.currentIndex()==MULTI_CHANNEL_TAB):
#            self.multiChannelLevelBox.setEnabled(True)
#            self.multiChannelStart.setEnabled(True)
#            self.logMultiChannel.setDisabled(True)
#            for i in range(array_reader.NUM_CHANNELS):
#                pb = getattr(self,'multiChannelProgressBar_{0}'.format(i+1))
#                pb.setFormat(r'no data')
#                pb.setValue(0)
#
#    def setWidgetEnableOnDisconnect(self):
#        self.portLineEdit.setEnabled(True)
#        if (self.tabWidget.currentIndex()==SINGLE_CHANNEL_TAB):
#            for i in range(array_reader.NUM_CHANNELS):
#                rb = getattr(self,'channelRadioButton_{0}'.format(i+1))
#                if rb.isChecked():
#                    rb.setChecked(False)
#                rb.setDisabled(True)
#            self.singleChannelPixelBox.setDisabled(True)
#            self.singleChannelLevelBox.setDisabled(True)
#            self.singleChannelStart.setDisabled(True)
#            self.singleChannelProgressBar.setFormat(r'no data')
#            self.mpl.canvas.hide()
#            if self.timerSingleChannel.isActive():
#                self.timerSingleChannel.stop()
#            if self.timerMultiChannel.isActive():
#                self.timerMultiChannel.stop()
#                
#        if (self.tabWidget.currentIndex()==MULTI_CHANNEL_TAB):
#            self.logMultiChannel.setDisabled(True)
#            self.multiChannelStart.setDisabled(True)
#            self.multiChannelLevelBox.setDisabled(True)
#            for i in range(array_reader.NUM_CHANNELS):
#                pb = getattr(self,'multiChannelProgressBar_{0}'.format(i+1))
#                pb.setFormat(r'no data')
#                pb.setValue(0)
#            if self.timerSingleChannel.isActive():
#                self.timerSingleChannel.stop()
#            if self.timerMultiChannel.isActive():
#                self.timerMultiChannel.stop()

    def cleanUpAndCloseDevice(self):
        self.dev.setModeStopped()
        self.dev.setChannel(0)
        self.dev.close()
        self.dev = None

    def main(self):
        self.show()


def opticalSensorMain():
    app = QtGui.QApplication(sys.argv)
    mainWindow = OpticalSensorMainWindow()
    mainWindow.main()
    app.exec_()

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    opticalSensorMain()
