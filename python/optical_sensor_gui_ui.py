# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optical_sensor_gui.ui'
#
# Created: Mon Apr 16 12:39:54 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(717, 662)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.deviceTab = QtGui.QWidget()
        self.deviceTab.setObjectName("deviceTab")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.deviceTab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_13 = QtGui.QWidget(self.deviceTab)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_16 = QtGui.QHBoxLayout(self.widget_13)
        self.horizontalLayout_16.setContentsMargins(-1, 15, -1, 15)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_7 = QtGui.QLabel(self.widget_13)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_16.addWidget(self.label_7)
        self.verticalLayout_8.addWidget(self.widget_13)
        self.line_8 = QtGui.QFrame(self.deviceTab)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_8.addWidget(self.line_8)
        self.widget_1 = QtGui.QWidget(self.deviceTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_1.sizePolicy().hasHeightForWidth())
        self.widget_1.setSizePolicy(sizePolicy)
        self.widget_1.setObjectName("widget_1")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_3 = QtGui.QGroupBox(self.widget_1)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.portLineEdit = QtGui.QLineEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portLineEdit.sizePolicy().hasHeightForWidth())
        self.portLineEdit.setSizePolicy(sizePolicy)
        self.portLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.portLineEdit.setObjectName("portLineEdit")
        self.horizontalLayout.addWidget(self.portLineEdit)
        self.connectPushButton = QtGui.QPushButton(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectPushButton.sizePolicy().hasHeightForWidth())
        self.connectPushButton.setSizePolicy(sizePolicy)
        self.connectPushButton.setObjectName("connectPushButton")
        self.horizontalLayout.addWidget(self.connectPushButton)
        spacerItem = QtGui.QSpacerItem(114, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.verticalLayout_8.addWidget(self.widget_1)
        self.line_2 = QtGui.QFrame(self.deviceTab)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_8.addWidget(self.line_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem1)
        self.tabWidget.addTab(self.deviceTab, "")
        self.singleChannelTab = QtGui.QWidget()
        self.singleChannelTab.setObjectName("singleChannelTab")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.singleChannelTab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.singleChannelStartWidget = QtGui.QWidget(self.singleChannelTab)
        self.singleChannelStartWidget.setObjectName("singleChannelStartWidget")
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.singleChannelStartWidget)
        self.horizontalLayout_12.setContentsMargins(-1, 9, -1, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.suBox = QtGui.QGroupBox(self.singleChannelStartWidget)
        self.suBox.setObjectName("suBox")
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.suBox)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.singleChannelDeviceComboBox = QtGui.QComboBox(self.suBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.singleChannelDeviceComboBox.sizePolicy().hasHeightForWidth())
        self.singleChannelDeviceComboBox.setSizePolicy(sizePolicy)
        self.singleChannelDeviceComboBox.setMinimumSize(QtCore.QSize(180, 0))
        self.singleChannelDeviceComboBox.setMaximumSize(QtCore.QSize(180, 16777215))
        self.singleChannelDeviceComboBox.setObjectName("singleChannelDeviceComboBox")
        self.horizontalLayout_13.addWidget(self.singleChannelDeviceComboBox)
        self.horizontalLayout_12.addWidget(self.suBox)
        self.channelBox = QtGui.QGroupBox(self.singleChannelStartWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.channelBox.sizePolicy().hasHeightForWidth())
        self.channelBox.setSizePolicy(sizePolicy)
        self.channelBox.setTitle("")
        self.channelBox.setObjectName("channelBox")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.channelBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.channelRadioButton_1 = QtGui.QRadioButton(self.channelBox)
        self.channelRadioButton_1.setObjectName("channelRadioButton_1")
        self.horizontalLayout_3.addWidget(self.channelRadioButton_1)
        self.channelRadioButton_2 = QtGui.QRadioButton(self.channelBox)
        self.channelRadioButton_2.setObjectName("channelRadioButton_2")
        self.horizontalLayout_3.addWidget(self.channelRadioButton_2)
        self.channelRadioButton_3 = QtGui.QRadioButton(self.channelBox)
        self.channelRadioButton_3.setObjectName("channelRadioButton_3")
        self.horizontalLayout_3.addWidget(self.channelRadioButton_3)
        self.channelRadioButton_4 = QtGui.QRadioButton(self.channelBox)
        self.channelRadioButton_4.setObjectName("channelRadioButton_4")
        self.horizontalLayout_3.addWidget(self.channelRadioButton_4)
        self.channelRadioButton_5 = QtGui.QRadioButton(self.channelBox)
        self.channelRadioButton_5.setObjectName("channelRadioButton_5")
        self.horizontalLayout_3.addWidget(self.channelRadioButton_5)
        spacerItem2 = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.singleChannelStart = QtGui.QPushButton(self.channelBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.singleChannelStart.sizePolicy().hasHeightForWidth())
        self.singleChannelStart.setSizePolicy(sizePolicy)
        self.singleChannelStart.setMinimumSize(QtCore.QSize(80, 0))
        self.singleChannelStart.setObjectName("singleChannelStart")
        self.horizontalLayout_3.addWidget(self.singleChannelStart)
        self.horizontalLayout_12.addWidget(self.channelBox)
        self.verticalLayout_7.addWidget(self.singleChannelStartWidget)
        self.line_3 = QtGui.QFrame(self.singleChannelTab)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_7.addWidget(self.line_3)
        self.widget_4 = QtGui.QWidget(self.singleChannelTab)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.singleChannelPixelBox = QtGui.QGroupBox(self.widget_4)
        self.singleChannelPixelBox.setObjectName("singleChannelPixelBox")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.singleChannelPixelBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.mpl = MplWidget(self.singleChannelPixelBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl.sizePolicy().hasHeightForWidth())
        self.mpl.setSizePolicy(sizePolicy)
        self.mpl.setMinimumSize(QtCore.QSize(200, 200))
        self.mpl.setObjectName("mpl")
        self.verticalLayout_5.addWidget(self.mpl)
        self.widget_11 = QtGui.QWidget(self.singleChannelPixelBox)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.widget_11)
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem3)
        self.label_10 = QtGui.QLabel(self.widget_11)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_14.addWidget(self.label_10)
        self.clearNormalizationPushButton = QtGui.QPushButton(self.widget_11)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearNormalizationPushButton.sizePolicy().hasHeightForWidth())
        self.clearNormalizationPushButton.setSizePolicy(sizePolicy)
        self.clearNormalizationPushButton.setMinimumSize(QtCore.QSize(80, 0))
        self.clearNormalizationPushButton.setObjectName("clearNormalizationPushButton")
        self.horizontalLayout_14.addWidget(self.clearNormalizationPushButton)
        self.setNormalizationPushButton = QtGui.QPushButton(self.widget_11)
        self.setNormalizationPushButton.setObjectName("setNormalizationPushButton")
        self.horizontalLayout_14.addWidget(self.setNormalizationPushButton)
        self.saveNormalizationPushButton = QtGui.QPushButton(self.widget_11)
        self.saveNormalizationPushButton.setObjectName("saveNormalizationPushButton")
        self.horizontalLayout_14.addWidget(self.saveNormalizationPushButton)
        self.loadNormalizationPushButton = QtGui.QPushButton(self.widget_11)
        self.loadNormalizationPushButton.setObjectName("loadNormalizationPushButton")
        self.horizontalLayout_14.addWidget(self.loadNormalizationPushButton)
        self.verticalLayout_5.addWidget(self.widget_11)
        self.verticalLayout_6.addWidget(self.singleChannelPixelBox)
        self.verticalLayout_7.addWidget(self.widget_4)
        self.widget_5 = QtGui.QWidget(self.singleChannelTab)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.singleChannelLevelBox = QtGui.QGroupBox(self.widget_5)
        self.singleChannelLevelBox.setObjectName("singleChannelLevelBox")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.singleChannelLevelBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.singleChannelProgressBar = QtGui.QProgressBar(self.singleChannelLevelBox)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.singleChannelProgressBar.setFont(font)
        self.singleChannelProgressBar.setProperty("value", 0)
        self.singleChannelProgressBar.setObjectName("singleChannelProgressBar")
        self.horizontalLayout_5.addWidget(self.singleChannelProgressBar)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.horizontalLayout_6.addWidget(self.singleChannelLevelBox)
        self.verticalLayout_7.addWidget(self.widget_5)
        self.tabWidget.addTab(self.singleChannelTab, "")
        self.multiChannelTab = QtGui.QWidget()
        self.multiChannelTab.setObjectName("multiChannelTab")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.multiChannelTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_6 = QtGui.QWidget(self.multiChannelTab)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.multiChannelStartWidget = QtGui.QWidget(self.widget_6)
        self.multiChannelStartWidget.setObjectName("multiChannelStartWidget")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.multiChannelStartWidget)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtGui.QLabel(self.multiChannelStartWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.multiChannelTimeLabel = QtGui.QLabel(self.multiChannelStartWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.multiChannelTimeLabel.sizePolicy().hasHeightForWidth())
        self.multiChannelTimeLabel.setSizePolicy(sizePolicy)
        self.multiChannelTimeLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.multiChannelTimeLabel.setObjectName("multiChannelTimeLabel")
        self.horizontalLayout_4.addWidget(self.multiChannelTimeLabel)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.loggingCheckBox = QtGui.QCheckBox(self.multiChannelStartWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.loggingCheckBox.setFont(font)
        self.loggingCheckBox.setChecked(True)
        self.loggingCheckBox.setObjectName("loggingCheckBox")
        self.horizontalLayout_4.addWidget(self.loggingCheckBox)
        self.multiChannelStart = QtGui.QPushButton(self.multiChannelStartWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.multiChannelStart.sizePolicy().hasHeightForWidth())
        self.multiChannelStart.setSizePolicy(sizePolicy)
        self.multiChannelStart.setObjectName("multiChannelStart")
        self.horizontalLayout_4.addWidget(self.multiChannelStart)
        self.verticalLayout_3.addWidget(self.multiChannelStartWidget)
        self.line_7 = QtGui.QFrame(self.widget_6)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_3.addWidget(self.line_7)
        self.multiChannelDeviceTabWidget = QtGui.QTabWidget(self.widget_6)
        self.multiChannelDeviceTabWidget.setObjectName("multiChannelDeviceTabWidget")
        self.widget = QtGui.QWidget()
        self.widget.setObjectName("widget")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.scrollArea = QtGui.QScrollArea(self.widget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 635, 386))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtGui.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.widget1 = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_7.setContentsMargins(-1, 15, -1, 15)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtGui.QLabel(self.widget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(50, 0))
        self.label.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.multiChannelProgressBar_1 = QtGui.QProgressBar(self.widget1)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.multiChannelProgressBar_1.setFont(font)
        self.multiChannelProgressBar_1.setProperty("value", 0)
        self.multiChannelProgressBar_1.setTextVisible(True)
        self.multiChannelProgressBar_1.setOrientation(QtCore.Qt.Horizontal)
        self.multiChannelProgressBar_1.setInvertedAppearance(False)
        self.multiChannelProgressBar_1.setObjectName("multiChannelProgressBar_1")
        self.horizontalLayout_7.addWidget(self.multiChannelProgressBar_1)
        spacerItem7 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.verticalLayout_2.addWidget(self.widget1)
        self.line = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.widget_3 = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_8.setContentsMargins(-1, 15, -1, 15)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_2 = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(50, 0))
        self.label_2.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        self.multiChannelProgressBar_2 = QtGui.QProgressBar(self.widget_3)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.multiChannelProgressBar_2.setFont(font)
        self.multiChannelProgressBar_2.setProperty("value", 0)
        self.multiChannelProgressBar_2.setObjectName("multiChannelProgressBar_2")
        self.horizontalLayout_8.addWidget(self.multiChannelProgressBar_2)
        spacerItem8 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.line_4 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.widget_7 = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.widget_7)
        self.horizontalLayout_9.setContentsMargins(-1, 15, -1, 15)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QtGui.QLabel(self.widget_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(50, 0))
        self.label_4.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        self.multiChannelProgressBar_3 = QtGui.QProgressBar(self.widget_7)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.multiChannelProgressBar_3.setFont(font)
        self.multiChannelProgressBar_3.setProperty("value", 0)
        self.multiChannelProgressBar_3.setObjectName("multiChannelProgressBar_3")
        self.horizontalLayout_9.addWidget(self.multiChannelProgressBar_3)
        spacerItem9 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.line_5 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_2.addWidget(self.line_5)
        self.widget_8 = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.widget_8)
        self.horizontalLayout_10.setContentsMargins(-1, 15, -1, 15)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_5 = QtGui.QLabel(self.widget_8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(50, 0))
        self.label_5.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_10.addWidget(self.label_5)
        self.multiChannelProgressBar_4 = QtGui.QProgressBar(self.widget_8)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.multiChannelProgressBar_4.setFont(font)
        self.multiChannelProgressBar_4.setProperty("value", 0)
        self.multiChannelProgressBar_4.setObjectName("multiChannelProgressBar_4")
        self.horizontalLayout_10.addWidget(self.multiChannelProgressBar_4)
        spacerItem10 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem10)
        self.verticalLayout_2.addWidget(self.widget_8)
        self.line_6 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_2.addWidget(self.line_6)
        self.widget_9 = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.widget_9)
        self.horizontalLayout_11.setContentsMargins(-1, 15, -1, 15)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_6 = QtGui.QLabel(self.widget_9)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(50, 0))
        self.label_6.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_11.addWidget(self.label_6)
        self.multiChannelProgressBar_5 = QtGui.QProgressBar(self.widget_9)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.multiChannelProgressBar_5.setFont(font)
        self.multiChannelProgressBar_5.setProperty("value", 0)
        self.multiChannelProgressBar_5.setObjectName("multiChannelProgressBar_5")
        self.horizontalLayout_11.addWidget(self.multiChannelProgressBar_5)
        spacerItem11 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem11)
        self.verticalLayout_2.addWidget(self.widget_9)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_10.addWidget(self.scrollArea)
        self.multiChannelDeviceTabWidget.addTab(self.widget, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.multiChannelDeviceTabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.multiChannelDeviceTabWidget.addTab(self.tab_3, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.multiChannelDeviceTabWidget.addTab(self.tab, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.multiChannelDeviceTabWidget.addTab(self.tab_4, "")
        self.verticalLayout_3.addWidget(self.multiChannelDeviceTabWidget)
        self.logFileWidget = QtGui.QWidget(self.widget_6)
        self.logFileWidget.setObjectName("logFileWidget")
        self.horizontalLayout_15 = QtGui.QHBoxLayout(self.logFileWidget)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_9 = QtGui.QLabel(self.logFileWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_15.addWidget(self.label_9)
        self.logFileLabel = QtGui.QLabel(self.logFileWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logFileLabel.sizePolicy().hasHeightForWidth())
        self.logFileLabel.setSizePolicy(sizePolicy)
        self.logFileLabel.setObjectName("logFileLabel")
        self.horizontalLayout_15.addWidget(self.logFileLabel)
        self.setLogFileToolButton = QtGui.QToolButton(self.logFileWidget)
        self.setLogFileToolButton.setObjectName("setLogFileToolButton")
        self.horizontalLayout_15.addWidget(self.setLogFileToolButton)
        self.verticalLayout_3.addWidget(self.logFileWidget)
        self.verticalLayout_4.addWidget(self.widget_6)
        self.tabWidget.addTab(self.multiChannelTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 717, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.multiChannelDeviceTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Expresso Capillary Sensor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Note:  this tab will be flushed out later to handle multiple devices.", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.connectPushButton.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.deviceTab), QtGui.QApplication.translate("MainWindow", "Device Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.suBox.setTitle(QtGui.QApplication.translate("MainWindow", "Active Device && Channel", None, QtGui.QApplication.UnicodeUTF8))
        self.channelRadioButton_1.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.channelRadioButton_2.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.channelRadioButton_3.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.channelRadioButton_4.setText(QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.channelRadioButton_5.setText(QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.singleChannelStart.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.singleChannelPixelBox.setTitle(QtGui.QApplication.translate("MainWindow", "Pixel Values", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Pixel Normalization", None, QtGui.QApplication.UnicodeUTF8))
        self.clearNormalizationPushButton.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.setNormalizationPushButton.setText(QtGui.QApplication.translate("MainWindow", "Set", None, QtGui.QApplication.UnicodeUTF8))
        self.saveNormalizationPushButton.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.loadNormalizationPushButton.setText(QtGui.QApplication.translate("MainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.singleChannelLevelBox.setTitle(QtGui.QApplication.translate("MainWindow", "Fluid Level", None, QtGui.QApplication.UnicodeUTF8))
        self.singleChannelProgressBar.setFormat(QtGui.QApplication.translate("MainWindow", "%v nl", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.singleChannelTab), QtGui.QApplication.translate("MainWindow", "Single Channel Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Time:", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelTimeLabel.setText(QtGui.QApplication.translate("MainWindow", "_____ s", None, QtGui.QApplication.UnicodeUTF8))
        self.loggingCheckBox.setText(QtGui.QApplication.translate("MainWindow", "Logging", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelStart.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Fluid Levels", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Ch 1", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelProgressBar_1.setFormat(QtGui.QApplication.translate("MainWindow", "%v nl", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Ch 2", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelProgressBar_2.setFormat(QtGui.QApplication.translate("MainWindow", "%v nl", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Ch 3", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelProgressBar_3.setFormat(QtGui.QApplication.translate("MainWindow", "%v nl", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Ch 4", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelProgressBar_4.setFormat(QtGui.QApplication.translate("MainWindow", "%v nl", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Ch 5", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelProgressBar_5.setFormat(QtGui.QApplication.translate("MainWindow", "%v nl", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelDeviceTabWidget.setTabText(self.multiChannelDeviceTabWidget.indexOf(self.widget), QtGui.QApplication.translate("MainWindow", "Device 1", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelDeviceTabWidget.setTabText(self.multiChannelDeviceTabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Device 2", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelDeviceTabWidget.setTabText(self.multiChannelDeviceTabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Device 3", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelDeviceTabWidget.setTabText(self.multiChannelDeviceTabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Device 4", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelDeviceTabWidget.setTabText(self.multiChannelDeviceTabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "Device etc", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Log File: ", None, QtGui.QApplication.UnicodeUTF8))
        self.logFileLabel.setText(QtGui.QApplication.translate("MainWindow", "default_log_file.hdf5", None, QtGui.QApplication.UnicodeUTF8))
        self.setLogFileToolButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.multiChannelTab), QtGui.QApplication.translate("MainWindow", "Multi Channel Mode", None, QtGui.QApplication.UnicodeUTF8))

from mplwidget import MplWidget
