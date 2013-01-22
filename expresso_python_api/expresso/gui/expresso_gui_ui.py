# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'expresso_gui.ui'
#
# Created: Wed Jan 16 12:41:39 2013
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(674, 663)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        MainWindow.setFont(font)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Expresso Data Acquisition", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.deviceTab = QtGui.QWidget()
        self.deviceTab.setObjectName(_fromUtf8("deviceTab"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.deviceTab)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.label_7 = QtGui.QLabel(self.deviceTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Welcome!", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_11.addWidget(self.label_7)
        self.widget_12 = QtGui.QWidget(self.deviceTab)
        self.widget_12.setObjectName(_fromUtf8("widget_12"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_12)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.scanPushButton = QtGui.QPushButton(self.widget_12)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.scanPushButton.setFont(font)
        self.scanPushButton.setText(QtGui.QApplication.translate("MainWindow", "Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.scanPushButton.setObjectName(_fromUtf8("scanPushButton"))
        self.horizontalLayout_2.addWidget(self.scanPushButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_11.addWidget(self.widget_12)
        self.devWidgetContainer = QtGui.QWidget(self.deviceTab)
        self.devWidgetContainer.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.devWidgetContainer.setFont(font)
        self.devWidgetContainer.setStyleSheet(_fromUtf8(""))
        self.devWidgetContainer.setObjectName(_fromUtf8("devWidgetContainer"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.devWidgetContainer)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_14 = QtGui.QLabel(self.devWidgetContainer)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "Expresso Devices", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_8.addWidget(self.label_14)
        self.devWidget = QtGui.QWidget(self.devWidgetContainer)
        self.devWidget.setStyleSheet(_fromUtf8(""))
        self.devWidget.setObjectName(_fromUtf8("devWidget"))
        self.devWidgetVLay = QtGui.QVBoxLayout(self.devWidget)
        self.devWidgetVLay.setMargin(0)
        self.devWidgetVLay.setObjectName(_fromUtf8("devWidgetVLay"))
        self.verticalLayout_8.addWidget(self.devWidget)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_8.addItem(spacerItem2)
        self.widget_4 = QtGui.QWidget(self.devWidgetContainer)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem3 = QtGui.QSpacerItem(226, 24, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.connectPushButton = QtGui.QPushButton(self.widget_4)
        self.connectPushButton.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.connectPushButton.setObjectName(_fromUtf8("connectPushButton"))
        self.horizontalLayout.addWidget(self.connectPushButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_8.addWidget(self.widget_4)
        self.verticalLayout_11.addWidget(self.devWidgetContainer)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem5)
        self.tabWidget.addTab(self.deviceTab, _fromUtf8(""))
        self.singleChannelTab = QtGui.QWidget()
        self.singleChannelTab.setObjectName(_fromUtf8("singleChannelTab"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.singleChannelTab)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.singleChannelStartWidget_2 = QtGui.QWidget(self.singleChannelTab)
        self.singleChannelStartWidget_2.setObjectName(_fromUtf8("singleChannelStartWidget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.singleChannelStartWidget_2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_11 = QtGui.QLabel(self.singleChannelStartWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Active Device & Channel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout.addWidget(self.label_11)
        self.singleChannelStartWidget = QtGui.QWidget(self.singleChannelStartWidget_2)
        self.singleChannelStartWidget.setObjectName(_fromUtf8("singleChannelStartWidget"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.singleChannelStartWidget)
        self.horizontalLayout_12.setMargin(0)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.singleChannelDeviceComboBox = QtGui.QComboBox(self.singleChannelStartWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.singleChannelDeviceComboBox.sizePolicy().hasHeightForWidth())
        self.singleChannelDeviceComboBox.setSizePolicy(sizePolicy)
        self.singleChannelDeviceComboBox.setMinimumSize(QtCore.QSize(180, 0))
        self.singleChannelDeviceComboBox.setMaximumSize(QtCore.QSize(180, 16777215))
        self.singleChannelDeviceComboBox.setObjectName(_fromUtf8("singleChannelDeviceComboBox"))
        self.horizontalLayout_12.addWidget(self.singleChannelDeviceComboBox)
        self.channelRadioButton_1 = QtGui.QRadioButton(self.singleChannelStartWidget)
        self.channelRadioButton_1.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.channelRadioButton_1.setObjectName(_fromUtf8("channelRadioButton_1"))
        self.horizontalLayout_12.addWidget(self.channelRadioButton_1)
        self.channelRadioButton_2 = QtGui.QRadioButton(self.singleChannelStartWidget)
        self.channelRadioButton_2.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.channelRadioButton_2.setObjectName(_fromUtf8("channelRadioButton_2"))
        self.horizontalLayout_12.addWidget(self.channelRadioButton_2)
        self.channelRadioButton_3 = QtGui.QRadioButton(self.singleChannelStartWidget)
        self.channelRadioButton_3.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.channelRadioButton_3.setObjectName(_fromUtf8("channelRadioButton_3"))
        self.horizontalLayout_12.addWidget(self.channelRadioButton_3)
        self.channelRadioButton_4 = QtGui.QRadioButton(self.singleChannelStartWidget)
        self.channelRadioButton_4.setText(QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.channelRadioButton_4.setObjectName(_fromUtf8("channelRadioButton_4"))
        self.horizontalLayout_12.addWidget(self.channelRadioButton_4)
        self.channelRadioButton_5 = QtGui.QRadioButton(self.singleChannelStartWidget)
        self.channelRadioButton_5.setText(QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.channelRadioButton_5.setObjectName(_fromUtf8("channelRadioButton_5"))
        self.horizontalLayout_12.addWidget(self.channelRadioButton_5)
        spacerItem6 = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem6)
        self.singleChannelStart = QtGui.QPushButton(self.singleChannelStartWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.singleChannelStart.sizePolicy().hasHeightForWidth())
        self.singleChannelStart.setSizePolicy(sizePolicy)
        self.singleChannelStart.setMinimumSize(QtCore.QSize(80, 0))
        self.singleChannelStart.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.singleChannelStart.setObjectName(_fromUtf8("singleChannelStart"))
        self.horizontalLayout_12.addWidget(self.singleChannelStart)
        self.verticalLayout.addWidget(self.singleChannelStartWidget)
        self.verticalLayout_7.addWidget(self.singleChannelStartWidget_2)
        self.line_3 = QtGui.QFrame(self.singleChannelTab)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_7.addWidget(self.line_3)
        self.singleChannelPixelWidget = QtGui.QWidget(self.singleChannelTab)
        self.singleChannelPixelWidget.setObjectName(_fromUtf8("singleChannelPixelWidget"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.singleChannelPixelWidget)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_12 = QtGui.QLabel(self.singleChannelPixelWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Pixel Values", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_6.addWidget(self.label_12)
        self.mpl = MplWidget(self.singleChannelPixelWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl.sizePolicy().hasHeightForWidth())
        self.mpl.setSizePolicy(sizePolicy)
        self.mpl.setMinimumSize(QtCore.QSize(200, 200))
        self.mpl.setObjectName(_fromUtf8("mpl"))
        self.verticalLayout_6.addWidget(self.mpl)
        self.widget_11 = QtGui.QWidget(self.singleChannelPixelWidget)
        self.widget_11.setObjectName(_fromUtf8("widget_11"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.widget_11)
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem7)
        self.label_10 = QtGui.QLabel(self.widget_11)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Pixel Normalization", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_14.addWidget(self.label_10)
        self.clearNormalizationPushButton = QtGui.QPushButton(self.widget_11)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearNormalizationPushButton.sizePolicy().hasHeightForWidth())
        self.clearNormalizationPushButton.setSizePolicy(sizePolicy)
        self.clearNormalizationPushButton.setMinimumSize(QtCore.QSize(80, 0))
        self.clearNormalizationPushButton.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.clearNormalizationPushButton.setObjectName(_fromUtf8("clearNormalizationPushButton"))
        self.horizontalLayout_14.addWidget(self.clearNormalizationPushButton)
        self.setNormalizationPushButton = QtGui.QPushButton(self.widget_11)
        self.setNormalizationPushButton.setText(QtGui.QApplication.translate("MainWindow", "Set", None, QtGui.QApplication.UnicodeUTF8))
        self.setNormalizationPushButton.setObjectName(_fromUtf8("setNormalizationPushButton"))
        self.horizontalLayout_14.addWidget(self.setNormalizationPushButton)
        self.saveNormalizationPushButton = QtGui.QPushButton(self.widget_11)
        self.saveNormalizationPushButton.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.saveNormalizationPushButton.setObjectName(_fromUtf8("saveNormalizationPushButton"))
        self.horizontalLayout_14.addWidget(self.saveNormalizationPushButton)
        self.loadNormalizationPushButton = QtGui.QPushButton(self.widget_11)
        self.loadNormalizationPushButton.setText(QtGui.QApplication.translate("MainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.loadNormalizationPushButton.setObjectName(_fromUtf8("loadNormalizationPushButton"))
        self.horizontalLayout_14.addWidget(self.loadNormalizationPushButton)
        self.verticalLayout_6.addWidget(self.widget_11)
        self.verticalLayout_7.addWidget(self.singleChannelPixelWidget)
        self.widget_5 = QtGui.QWidget(self.singleChannelTab)
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_7.addWidget(self.widget_5)
        self.line_9 = QtGui.QFrame(self.singleChannelTab)
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.verticalLayout_7.addWidget(self.line_9)
        self.singleChannelLevelWidget = QtGui.QWidget(self.singleChannelTab)
        self.singleChannelLevelWidget.setObjectName(_fromUtf8("singleChannelLevelWidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.singleChannelLevelWidget)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_13 = QtGui.QLabel(self.singleChannelLevelWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "Fluid Level", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_5.addWidget(self.label_13)
        self.widget_2 = QtGui.QWidget(self.singleChannelLevelWidget)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_13.setMargin(0)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem8)
        self.singleChannelProgressBar = QtGui.QProgressBar(self.widget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.singleChannelProgressBar.setFont(font)
        self.singleChannelProgressBar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.singleChannelProgressBar.setProperty("value", 0)
        self.singleChannelProgressBar.setFormat(QtGui.QApplication.translate("MainWindow", "%v nl", None, QtGui.QApplication.UnicodeUTF8))
        self.singleChannelProgressBar.setObjectName(_fromUtf8("singleChannelProgressBar"))
        self.horizontalLayout_13.addWidget(self.singleChannelProgressBar)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem9)
        self.verticalLayout_5.addWidget(self.widget_2)
        self.verticalLayout_7.addWidget(self.singleChannelLevelWidget)
        self.tabWidget.addTab(self.singleChannelTab, _fromUtf8(""))
        self.multiChannelTab = QtGui.QWidget()
        self.multiChannelTab.setObjectName(_fromUtf8("multiChannelTab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.multiChannelTab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.widget_6 = QtGui.QWidget(self.multiChannelTab)
        self.widget_6.setObjectName(_fromUtf8("widget_6"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.multiChannelStartWidget = QtGui.QWidget(self.widget_6)
        self.multiChannelStartWidget.setObjectName(_fromUtf8("multiChannelStartWidget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.multiChannelStartWidget)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.multiChannelStartWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Time:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.multiChannelTimeLabel = QtGui.QLabel(self.multiChannelStartWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.multiChannelTimeLabel.sizePolicy().hasHeightForWidth())
        self.multiChannelTimeLabel.setSizePolicy(sizePolicy)
        self.multiChannelTimeLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.multiChannelTimeLabel.setText(QtGui.QApplication.translate("MainWindow", "_____ s", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelTimeLabel.setObjectName(_fromUtf8("multiChannelTimeLabel"))
        self.horizontalLayout_4.addWidget(self.multiChannelTimeLabel)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.loggingCheckBox = QtGui.QCheckBox(self.multiChannelStartWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.loggingCheckBox.setFont(font)
        self.loggingCheckBox.setText(QtGui.QApplication.translate("MainWindow", "Logging", None, QtGui.QApplication.UnicodeUTF8))
        self.loggingCheckBox.setChecked(True)
        self.loggingCheckBox.setObjectName(_fromUtf8("loggingCheckBox"))
        self.horizontalLayout_4.addWidget(self.loggingCheckBox)
        self.multiChannelStart = QtGui.QPushButton(self.multiChannelStartWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.multiChannelStart.sizePolicy().hasHeightForWidth())
        self.multiChannelStart.setSizePolicy(sizePolicy)
        self.multiChannelStart.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelStart.setObjectName(_fromUtf8("multiChannelStart"))
        self.horizontalLayout_4.addWidget(self.multiChannelStart)
        self.verticalLayout_3.addWidget(self.multiChannelStartWidget)
        self.line_7 = QtGui.QFrame(self.widget_6)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.verticalLayout_3.addWidget(self.line_7)
        self.multiChannelDeviceTabs = QtGui.QTabWidget(self.widget_6)
        self.multiChannelDeviceTabs.setObjectName(_fromUtf8("multiChannelDeviceTabs"))
        self.mc_tab1 = QtGui.QWidget()
        self.mc_tab1.setObjectName(_fromUtf8("mc_tab1"))
        self.mc_1 = McWidget(self.mc_tab1)
        self.mc_1.setGeometry(QtCore.QRect(9, 9, 594, 382))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mc_1.sizePolicy().hasHeightForWidth())
        self.mc_1.setSizePolicy(sizePolicy)
        self.mc_1.setMinimumSize(QtCore.QSize(200, 200))
        self.mc_1.setObjectName(_fromUtf8("mc_1"))
        self.multiChannelDeviceTabs.addTab(self.mc_tab1, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.multiChannelDeviceTabs)
        self.logFileWidget = QtGui.QWidget(self.widget_6)
        self.logFileWidget.setObjectName(_fromUtf8("logFileWidget"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout(self.logFileWidget)
        self.horizontalLayout_15.setMargin(0)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_9 = QtGui.QLabel(self.logFileWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Log File: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_15.addWidget(self.label_9)
        self.logFileLabel = QtGui.QLabel(self.logFileWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logFileLabel.sizePolicy().hasHeightForWidth())
        self.logFileLabel.setSizePolicy(sizePolicy)
        self.logFileLabel.setText(QtGui.QApplication.translate("MainWindow", "default_log_file.hdf5", None, QtGui.QApplication.UnicodeUTF8))
        self.logFileLabel.setObjectName(_fromUtf8("logFileLabel"))
        self.horizontalLayout_15.addWidget(self.logFileLabel)
        self.setLogFileToolButton = QtGui.QToolButton(self.logFileWidget)
        self.setLogFileToolButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.setLogFileToolButton.setObjectName(_fromUtf8("setLogFileToolButton"))
        self.horizontalLayout_15.addWidget(self.setLogFileToolButton)
        self.verticalLayout_3.addWidget(self.logFileWidget)
        self.verticalLayout_4.addWidget(self.widget_6)
        self.tabWidget.addTab(self.multiChannelTab, _fromUtf8(""))
        self.verticalLayout_9.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 674, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.multiChannelDeviceTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.deviceTab), QtGui.QApplication.translate("MainWindow", "Device Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.singleChannelTab), QtGui.QApplication.translate("MainWindow", "Single Channel Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelDeviceTabs.setTabText(self.multiChannelDeviceTabs.indexOf(self.mc_tab1), QtGui.QApplication.translate("MainWindow", "Device", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.multiChannelTab), QtGui.QApplication.translate("MainWindow", "Multi Channel Mode", None, QtGui.QApplication.UnicodeUTF8))

from mplwidget import MplWidget
from mcwidget import McWidget
