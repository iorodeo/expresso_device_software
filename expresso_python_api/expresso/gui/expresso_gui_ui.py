# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'expresso_gui.ui'
#
# Created: Tue Oct 30 17:20:49 2012
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
        MainWindow.resize(712, 677)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Expresso Capillary Sensor", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.deviceTab = QtGui.QWidget()
        self.deviceTab.setObjectName(_fromUtf8("deviceTab"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.deviceTab)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
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
        spacerItem1 = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
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
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem2)
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
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem3)
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
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem4)
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
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
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
        self.multiChannelDeviceTabWidget = QtGui.QTabWidget(self.widget_6)
        self.multiChannelDeviceTabWidget.setObjectName(_fromUtf8("multiChannelDeviceTabWidget"))
        self.widget = QtGui.QWidget()
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.scrollArea = QtGui.QScrollArea(self.widget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 630, 394))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_8 = QtGui.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Fluid Levels", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_2.addWidget(self.label_8)
        self.widget1 = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_7.setContentsMargins(-1, 15, -1, 15)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label = QtGui.QLabel(self.widget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(50, 0))
        self.label.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Ch 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_7.addWidget(self.label)
        self.multiChannelProgressBar_1 = QtGui.QProgressBar(self.widget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.multiChannelProgressBar_1.setFont(font)
        self.multiChannelProgressBar_1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.multiChannelProgressBar_1.setProperty("value", 0)
        self.multiChannelProgressBar_1.setTextVisible(True)
        self.multiChannelProgressBar_1.setOrientation(QtCore.Qt.Horizontal)
        self.multiChannelProgressBar_1.setInvertedAppearance(False)
        self.multiChannelProgressBar_1.setFormat(QtGui.QApplication.translate("MainWindow", "%v nl", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelProgressBar_1.setObjectName(_fromUtf8("multiChannelProgressBar_1"))
        self.horizontalLayout_7.addWidget(self.multiChannelProgressBar_1)
        spacerItem6 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.verticalLayout_2.addWidget(self.widget1)
        self.line = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.widget_3 = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_8.setContentsMargins(-1, 15, -1, 15)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_2 = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(50, 0))
        self.label_2.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Ch 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_8.addWidget(self.label_2)
        self.multiChannelProgressBar_2 = QtGui.QProgressBar(self.widget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.multiChannelProgressBar_2.setFont(font)
        self.multiChannelProgressBar_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.multiChannelProgressBar_2.setProperty("value", 0)
        self.multiChannelProgressBar_2.setFormat(QtGui.QApplication.translate("MainWindow", "%v nl", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelProgressBar_2.setObjectName(_fromUtf8("multiChannelProgressBar_2"))
        self.horizontalLayout_8.addWidget(self.multiChannelProgressBar_2)
        spacerItem7 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.line_4 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_2.addWidget(self.line_4)
        self.widget_7 = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.widget_7.setObjectName(_fromUtf8("widget_7"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.widget_7)
        self.horizontalLayout_9.setContentsMargins(-1, 15, -1, 15)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_4 = QtGui.QLabel(self.widget_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(50, 0))
        self.label_4.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Ch 3", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_9.addWidget(self.label_4)
        self.multiChannelProgressBar_3 = QtGui.QProgressBar(self.widget_7)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.multiChannelProgressBar_3.setFont(font)
        self.multiChannelProgressBar_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.multiChannelProgressBar_3.setProperty("value", 0)
        self.multiChannelProgressBar_3.setFormat(QtGui.QApplication.translate("MainWindow", "%v nl", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelProgressBar_3.setObjectName(_fromUtf8("multiChannelProgressBar_3"))
        self.horizontalLayout_9.addWidget(self.multiChannelProgressBar_3)
        spacerItem8 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.line_5 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout_2.addWidget(self.line_5)
        self.widget_8 = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.widget_8.setObjectName(_fromUtf8("widget_8"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.widget_8)
        self.horizontalLayout_10.setContentsMargins(-1, 15, -1, 15)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_5 = QtGui.QLabel(self.widget_8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(50, 0))
        self.label_5.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Ch 4", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_10.addWidget(self.label_5)
        self.multiChannelProgressBar_4 = QtGui.QProgressBar(self.widget_8)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.multiChannelProgressBar_4.setFont(font)
        self.multiChannelProgressBar_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.multiChannelProgressBar_4.setProperty("value", 0)
        self.multiChannelProgressBar_4.setFormat(QtGui.QApplication.translate("MainWindow", "%v nl", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelProgressBar_4.setObjectName(_fromUtf8("multiChannelProgressBar_4"))
        self.horizontalLayout_10.addWidget(self.multiChannelProgressBar_4)
        spacerItem9 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem9)
        self.verticalLayout_2.addWidget(self.widget_8)
        self.line_6 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout_2.addWidget(self.line_6)
        self.widget_9 = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.widget_9.setObjectName(_fromUtf8("widget_9"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.widget_9)
        self.horizontalLayout_11.setContentsMargins(-1, 15, -1, 15)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_6 = QtGui.QLabel(self.widget_9)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(50, 0))
        self.label_6.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Ch 5", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_11.addWidget(self.label_6)
        self.multiChannelProgressBar_5 = QtGui.QProgressBar(self.widget_9)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.multiChannelProgressBar_5.setFont(font)
        self.multiChannelProgressBar_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.multiChannelProgressBar_5.setProperty("value", 0)
        self.multiChannelProgressBar_5.setFormat(QtGui.QApplication.translate("MainWindow", "%v nl", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelProgressBar_5.setObjectName(_fromUtf8("multiChannelProgressBar_5"))
        self.horizontalLayout_11.addWidget(self.multiChannelProgressBar_5)
        spacerItem10 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.verticalLayout_2.addWidget(self.widget_9)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_10.addWidget(self.scrollArea)
        self.multiChannelDeviceTabWidget.addTab(self.widget, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.multiChannelDeviceTabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.multiChannelDeviceTabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.multiChannelDeviceTabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.multiChannelDeviceTabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.multiChannelDeviceTabWidget)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 712, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.multiChannelDeviceTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.deviceTab), QtGui.QApplication.translate("MainWindow", "Device Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.singleChannelTab), QtGui.QApplication.translate("MainWindow", "Single Channel Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelDeviceTabWidget.setTabText(self.multiChannelDeviceTabWidget.indexOf(self.widget), QtGui.QApplication.translate("MainWindow", "Device 1", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelDeviceTabWidget.setTabText(self.multiChannelDeviceTabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Device 2", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelDeviceTabWidget.setTabText(self.multiChannelDeviceTabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Device 3", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelDeviceTabWidget.setTabText(self.multiChannelDeviceTabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Device 4", None, QtGui.QApplication.UnicodeUTF8))
        self.multiChannelDeviceTabWidget.setTabText(self.multiChannelDeviceTabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "Device etc", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.multiChannelTab), QtGui.QApplication.translate("MainWindow", "Multi Channel Mode", None, QtGui.QApplication.UnicodeUTF8))

from mplwidget import MplWidget
