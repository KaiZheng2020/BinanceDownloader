# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainForm.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QDateTimeEdit,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSplitter, QTabWidget,
    QTableView, QTextBrowser, QTextEdit, QTimeEdit,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        if not MainForm.objectName():
            MainForm.setObjectName(u"MainForm")
        MainForm.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainForm.sizePolicy().hasHeightForWidth())
        MainForm.setSizePolicy(sizePolicy)
        MainForm.setMinimumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u":/logo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainForm.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(MainForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.splitter = QSplitter(MainForm)
        self.splitter.setObjectName(u"splitter")
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMaximumSize(QSize(16777215, 16777215))
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setHandleWidth(5)
        self.tabWidget = QTabWidget(self.splitter)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 320))
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tab_HistoryData = QWidget()
        self.tab_HistoryData.setObjectName(u"tab_HistoryData")
        self.verticalLayout_3 = QVBoxLayout(self.tab_HistoryData)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_main = QVBoxLayout()
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.horizontalLayout_up = QHBoxLayout()
        self.horizontalLayout_up.setObjectName(u"horizontalLayout_up")
        self.groupBox_TradingType = QGroupBox(self.tab_HistoryData)
        self.groupBox_TradingType.setObjectName(u"groupBox_TradingType")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_TradingType)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.checkBox_spot = QCheckBox(self.groupBox_TradingType)
        self.checkBox_spot.setObjectName(u"checkBox_spot")
        self.checkBox_spot.setChecked(True)

        self.horizontalLayout_7.addWidget(self.checkBox_spot)

        self.checkBox_um = QCheckBox(self.groupBox_TradingType)
        self.checkBox_um.setObjectName(u"checkBox_um")

        self.horizontalLayout_7.addWidget(self.checkBox_um)

        self.checkBox_cm = QCheckBox(self.groupBox_TradingType)
        self.checkBox_cm.setObjectName(u"checkBox_cm")

        self.horizontalLayout_7.addWidget(self.checkBox_cm)


        self.horizontalLayout_up.addWidget(self.groupBox_TradingType)

        self.groupBox_DataType = QGroupBox(self.tab_HistoryData)
        self.groupBox_DataType.setObjectName(u"groupBox_DataType")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_DataType)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBox_Kline = QCheckBox(self.groupBox_DataType)
        self.checkBox_Kline.setObjectName(u"checkBox_Kline")
        self.checkBox_Kline.setChecked(True)

        self.horizontalLayout_4.addWidget(self.checkBox_Kline)

        self.checkBox_AggTrade = QCheckBox(self.groupBox_DataType)
        self.checkBox_AggTrade.setObjectName(u"checkBox_AggTrade")

        self.horizontalLayout_4.addWidget(self.checkBox_AggTrade)

        self.checkBox_Trade = QCheckBox(self.groupBox_DataType)
        self.checkBox_Trade.setObjectName(u"checkBox_Trade")

        self.horizontalLayout_4.addWidget(self.checkBox_Trade)


        self.horizontalLayout_up.addWidget(self.groupBox_DataType)

        self.groupBox_Interval = QGroupBox(self.tab_HistoryData)
        self.groupBox_Interval.setObjectName(u"groupBox_Interval")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_Interval)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBox_1m = QCheckBox(self.groupBox_Interval)
        self.checkBox_1m.setObjectName(u"checkBox_1m")

        self.horizontalLayout_5.addWidget(self.checkBox_1m)

        self.checkBox_1h = QCheckBox(self.groupBox_Interval)
        self.checkBox_1h.setObjectName(u"checkBox_1h")

        self.horizontalLayout_5.addWidget(self.checkBox_1h)

        self.checkBox_1d = QCheckBox(self.groupBox_Interval)
        self.checkBox_1d.setObjectName(u"checkBox_1d")
        self.checkBox_1d.setChecked(True)

        self.horizontalLayout_5.addWidget(self.checkBox_1d)


        self.horizontalLayout_up.addWidget(self.groupBox_Interval)

        self.horizontalLayout_up.setStretch(0, 1)
        self.horizontalLayout_up.setStretch(1, 1)
        self.horizontalLayout_up.setStretch(2, 1)

        self.verticalLayout_main.addLayout(self.horizontalLayout_up)

        self.horizontalLayout_mid = QHBoxLayout()
        self.horizontalLayout_mid.setObjectName(u"horizontalLayout_mid")
        self.groupBox_DateRange = QGroupBox(self.tab_HistoryData)
        self.groupBox_DateRange.setObjectName(u"groupBox_DateRange")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_DateRange)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_StartDate = QLabel(self.groupBox_DateRange)
        self.label_StartDate.setObjectName(u"label_StartDate")
        self.label_StartDate.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_StartDate)

        self.dateEdit_StartDate = QDateEdit(self.groupBox_DateRange)
        self.dateEdit_StartDate.setObjectName(u"dateEdit_StartDate")
        self.dateEdit_StartDate.setDateTime(QDateTime(QDate(2022, 1, 1), QTime(0, 0, 1)))
        self.dateEdit_StartDate.setTime(QTime(0, 0, 1))
        self.dateEdit_StartDate.setCalendarPopup(True)
        self.dateEdit_StartDate.setDate(QDate(2022, 1, 1))

        self.horizontalLayout_6.addWidget(self.dateEdit_StartDate)

        self.label_EndDate = QLabel(self.groupBox_DateRange)
        self.label_EndDate.setObjectName(u"label_EndDate")
        self.label_EndDate.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_EndDate)

        self.dateEdit_EndDate = QDateEdit(self.groupBox_DateRange)
        self.dateEdit_EndDate.setObjectName(u"dateEdit_EndDate")
        self.dateEdit_EndDate.setDateTime(QDateTime(QDate(2021, 12, 23), QTime(0, 0, 0)))
        self.dateEdit_EndDate.setTime(QTime(0, 0, 0))
        self.dateEdit_EndDate.setCalendarPopup(True)

        self.horizontalLayout_6.addWidget(self.dateEdit_EndDate)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)
        self.horizontalLayout_6.setStretch(2, 1)
        self.horizontalLayout_6.setStretch(3, 2)

        self.horizontalLayout_mid.addWidget(self.groupBox_DateRange)

        self.groupBox_Proxy = QGroupBox(self.tab_HistoryData)
        self.groupBox_Proxy.setObjectName(u"groupBox_Proxy")
        self.groupBox_Proxy.setCheckable(False)
        self.groupBox_Proxy.setChecked(False)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_Proxy)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox_Proxy = QCheckBox(self.groupBox_Proxy)
        self.checkBox_Proxy.setObjectName(u"checkBox_Proxy")

        self.horizontalLayout_3.addWidget(self.checkBox_Proxy)

        self.lineEdit_Proxy = QLineEdit(self.groupBox_Proxy)
        self.lineEdit_Proxy.setObjectName(u"lineEdit_Proxy")

        self.horizontalLayout_3.addWidget(self.lineEdit_Proxy)


        self.horizontalLayout_mid.addWidget(self.groupBox_Proxy)

        self.horizontalLayout_mid.setStretch(0, 2)
        self.horizontalLayout_mid.setStretch(1, 1)

        self.verticalLayout_main.addLayout(self.horizontalLayout_mid)

        self.horizontalLayout_down = QHBoxLayout()
        self.horizontalLayout_down.setObjectName(u"horizontalLayout_down")
        self.groupBox_Controller = QGroupBox(self.tab_HistoryData)
        self.groupBox_Controller.setObjectName(u"groupBox_Controller")
        self.gridLayout = QGridLayout(self.groupBox_Controller)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_Step3 = QLabel(self.groupBox_Controller)
        self.label_Step3.setObjectName(u"label_Step3")
        self.label_Step3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_Step3, 2, 1, 1, 1)

        self.pushButton_DownloadSymbols = QPushButton(self.groupBox_Controller)
        self.pushButton_DownloadSymbols.setObjectName(u"pushButton_DownloadSymbols")

        self.gridLayout.addWidget(self.pushButton_DownloadSymbols, 0, 2, 1, 1)

        self.pushButton_DownloaderStart = QPushButton(self.groupBox_Controller)
        self.pushButton_DownloaderStart.setObjectName(u"pushButton_DownloaderStart")

        self.gridLayout.addWidget(self.pushButton_DownloaderStart, 2, 2, 1, 1)

        self.pushButton_SetSavePath = QPushButton(self.groupBox_Controller)
        self.pushButton_SetSavePath.setObjectName(u"pushButton_SetSavePath")

        self.gridLayout.addWidget(self.pushButton_SetSavePath, 1, 2, 1, 2)

        self.label_Step2 = QLabel(self.groupBox_Controller)
        self.label_Step2.setObjectName(u"label_Step2")
        self.label_Step2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_Step2, 1, 1, 1, 1)

        self.pushButton_LoadSymbols = QPushButton(self.groupBox_Controller)
        self.pushButton_LoadSymbols.setObjectName(u"pushButton_LoadSymbols")

        self.gridLayout.addWidget(self.pushButton_LoadSymbols, 0, 3, 1, 1)

        self.label_Step1 = QLabel(self.groupBox_Controller)
        self.label_Step1.setObjectName(u"label_Step1")
        self.label_Step1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_Step1, 0, 1, 1, 1)

        self.pushButton_DownloaderStop = QPushButton(self.groupBox_Controller)
        self.pushButton_DownloaderStop.setObjectName(u"pushButton_DownloaderStop")

        self.gridLayout.addWidget(self.pushButton_DownloaderStop, 2, 3, 1, 1)


        self.horizontalLayout_down.addWidget(self.groupBox_Controller)

        self.groupBox_Timer = QGroupBox(self.tab_HistoryData)
        self.groupBox_Timer.setObjectName(u"groupBox_Timer")
        self.gridLayout_Timer = QGridLayout(self.groupBox_Timer)
        self.gridLayout_Timer.setObjectName(u"gridLayout_Timer")
        self.pushButton_TimerStop = QPushButton(self.groupBox_Timer)
        self.pushButton_TimerStop.setObjectName(u"pushButton_TimerStop")

        self.gridLayout_Timer.addWidget(self.pushButton_TimerStop, 0, 2, 1, 1)

        self.timeEdit_Timer = QTimeEdit(self.groupBox_Timer)
        self.timeEdit_Timer.setObjectName(u"timeEdit_Timer")

        self.gridLayout_Timer.addWidget(self.timeEdit_Timer, 0, 0, 1, 1)

        self.pushButton_TimerStart = QPushButton(self.groupBox_Timer)
        self.pushButton_TimerStart.setObjectName(u"pushButton_TimerStart")

        self.gridLayout_Timer.addWidget(self.pushButton_TimerStart, 0, 1, 1, 1)


        self.horizontalLayout_down.addWidget(self.groupBox_Timer)

        self.horizontalLayout_down.setStretch(0, 2)
        self.horizontalLayout_down.setStretch(1, 1)

        self.verticalLayout_main.addLayout(self.horizontalLayout_down)


        self.verticalLayout_3.addLayout(self.verticalLayout_main)

        self.tabWidget.addTab(self.tab_HistoryData, "")
        self.tab_FuturesOrderBookLevel2 = QWidget()
        self.tab_FuturesOrderBookLevel2.setObjectName(u"tab_FuturesOrderBookLevel2")
        self.groupBoxFutures = QGroupBox(self.tab_FuturesOrderBookLevel2)
        self.groupBoxFutures.setObjectName(u"groupBoxFutures")
        self.groupBoxFutures.setGeometry(QRect(50, 50, 601, 91))
        self.pushButtonFuturesOrderBookSpiderStart = QPushButton(self.groupBoxFutures)
        self.pushButtonFuturesOrderBookSpiderStart.setObjectName(u"pushButtonFuturesOrderBookSpiderStart")
        self.pushButtonFuturesOrderBookSpiderStart.setGeometry(QRect(510, 60, 81, 24))
        self.dateTimeFuturesOrderBookEditEndDateTime = QDateTimeEdit(self.groupBoxFutures)
        self.dateTimeFuturesOrderBookEditEndDateTime.setObjectName(u"dateTimeFuturesOrderBookEditEndDateTime")
        self.dateTimeFuturesOrderBookEditEndDateTime.setGeometry(QRect(290, 60, 141, 22))
        self.dateTimeFuturesOrderBookEditEndDateTime.setDate(QDate(2022, 1, 1))
        self.dateTimeFuturesOrderBookEditEndDateTime.setCalendarPopup(True)
        self.labelEndTime = QLabel(self.groupBoxFutures)
        self.labelEndTime.setObjectName(u"labelEndTime")
        self.labelEndTime.setGeometry(QRect(250, 60, 21, 16))
        self.labelBeginTime = QLabel(self.groupBoxFutures)
        self.labelBeginTime.setObjectName(u"labelBeginTime")
        self.labelBeginTime.setGeometry(QRect(250, 30, 31, 16))
        self.dateTimeEditFuturesOrderBookBeginDateTime = QDateTimeEdit(self.groupBoxFutures)
        self.dateTimeEditFuturesOrderBookBeginDateTime.setObjectName(u"dateTimeEditFuturesOrderBookBeginDateTime")
        self.dateTimeEditFuturesOrderBookBeginDateTime.setGeometry(QRect(290, 30, 141, 22))
        self.dateTimeEditFuturesOrderBookBeginDateTime.setDateTime(QDateTime(QDate(2021, 1, 1), QTime(0, 0, 0)))
        self.dateTimeEditFuturesOrderBookBeginDateTime.setDate(QDate(2021, 1, 1))
        self.dateTimeEditFuturesOrderBookBeginDateTime.setCalendarPopup(True)
        self.lineEditSecretKey = QLineEdit(self.groupBoxFutures)
        self.lineEditSecretKey.setObjectName(u"lineEditSecretKey")
        self.lineEditSecretKey.setGeometry(QRect(80, 60, 161, 21))
        self.lineEditAPIKey = QLineEdit(self.groupBoxFutures)
        self.lineEditAPIKey.setObjectName(u"lineEditAPIKey")
        self.lineEditAPIKey.setGeometry(QRect(80, 30, 161, 21))
        self.labelSecretKey = QLabel(self.groupBoxFutures)
        self.labelSecretKey.setObjectName(u"labelSecretKey")
        self.labelSecretKey.setGeometry(QRect(10, 60, 71, 16))
        self.labelAPIKey = QLabel(self.groupBoxFutures)
        self.labelAPIKey.setObjectName(u"labelAPIKey")
        self.labelAPIKey.setGeometry(QRect(10, 30, 51, 16))
        self.tabWidget.addTab(self.tab_FuturesOrderBookLevel2, "")
        self.tab_Realtime = QWidget()
        self.tab_Realtime.setObjectName(u"tab_Realtime")
        self.tabWidget.addTab(self.tab_Realtime, "")
        self.tab_Parser = QWidget()
        self.tab_Parser.setObjectName(u"tab_Parser")
        self.verticalLayout_2 = QVBoxLayout(self.tab_Parser)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_FileParserUp = QHBoxLayout()
        self.horizontalLayout_FileParserUp.setObjectName(u"horizontalLayout_FileParserUp")
        self.groupBox_Path = QGroupBox(self.tab_Parser)
        self.groupBox_Path.setObjectName(u"groupBox_Path")
        self.gridLayout_4 = QGridLayout(self.groupBox_Path)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_Des = QLabel(self.groupBox_Path)
        self.label_Des.setObjectName(u"label_Des")

        self.gridLayout_4.addWidget(self.label_Des, 1, 0, 1, 1)

        self.label_Src = QLabel(self.groupBox_Path)
        self.label_Src.setObjectName(u"label_Src")

        self.gridLayout_4.addWidget(self.label_Src, 0, 0, 1, 1)

        self.pushButton_SetDesDir = QPushButton(self.groupBox_Path)
        self.pushButton_SetDesDir.setObjectName(u"pushButton_SetDesDir")

        self.gridLayout_4.addWidget(self.pushButton_SetDesDir, 1, 2, 1, 1)

        self.lineEdit_SrcDir = QLineEdit(self.groupBox_Path)
        self.lineEdit_SrcDir.setObjectName(u"lineEdit_SrcDir")

        self.gridLayout_4.addWidget(self.lineEdit_SrcDir, 0, 1, 1, 1)

        self.pushButton_SetSrcDir = QPushButton(self.groupBox_Path)
        self.pushButton_SetSrcDir.setObjectName(u"pushButton_SetSrcDir")

        self.gridLayout_4.addWidget(self.pushButton_SetSrcDir, 0, 2, 1, 1)

        self.lineEdit_DesDir = QLineEdit(self.groupBox_Path)
        self.lineEdit_DesDir.setObjectName(u"lineEdit_DesDir")

        self.gridLayout_4.addWidget(self.lineEdit_DesDir, 1, 1, 1, 1)


        self.horizontalLayout_FileParserUp.addWidget(self.groupBox_Path)

        self.groupBox_ParseFileFormat = QGroupBox(self.tab_Parser)
        self.groupBox_ParseFileFormat.setObjectName(u"groupBox_ParseFileFormat")
        self.gridLayout_5 = QGridLayout(self.groupBox_ParseFileFormat)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.checkBox_ParseZIP = QCheckBox(self.groupBox_ParseFileFormat)
        self.checkBox_ParseZIP.setObjectName(u"checkBox_ParseZIP")
        self.checkBox_ParseZIP.setTabletTracking(False)
        self.checkBox_ParseZIP.setChecked(True)

        self.gridLayout_5.addWidget(self.checkBox_ParseZIP, 0, 0, 1, 1)

        self.checkBox_ParseCSV = QCheckBox(self.groupBox_ParseFileFormat)
        self.checkBox_ParseCSV.setObjectName(u"checkBox_ParseCSV")
        self.checkBox_ParseCSV.setTabletTracking(False)
        self.checkBox_ParseCSV.setChecked(True)

        self.gridLayout_5.addWidget(self.checkBox_ParseCSV, 0, 1, 1, 1)

        self.checkBox_ParseFeather = QCheckBox(self.groupBox_ParseFileFormat)
        self.checkBox_ParseFeather.setObjectName(u"checkBox_ParseFeather")

        self.gridLayout_5.addWidget(self.checkBox_ParseFeather, 0, 2, 1, 1)


        self.horizontalLayout_FileParserUp.addWidget(self.groupBox_ParseFileFormat)


        self.verticalLayout_2.addLayout(self.horizontalLayout_FileParserUp)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_ParseFileTpye = QGroupBox(self.tab_Parser)
        self.groupBox_ParseFileTpye.setObjectName(u"groupBox_ParseFileTpye")
        self.gridLayout_ParseFileType = QGridLayout(self.groupBox_ParseFileTpye)
        self.gridLayout_ParseFileType.setObjectName(u"gridLayout_ParseFileType")
        self.radioButton_AggTrade = QRadioButton(self.groupBox_ParseFileTpye)
        self.radioButton_AggTrade.setObjectName(u"radioButton_AggTrade")

        self.gridLayout_ParseFileType.addWidget(self.radioButton_AggTrade, 0, 2, 1, 1)

        self.radioButton_Trade = QRadioButton(self.groupBox_ParseFileTpye)
        self.radioButton_Trade.setObjectName(u"radioButton_Trade")

        self.gridLayout_ParseFileType.addWidget(self.radioButton_Trade, 0, 3, 1, 1)

        self.radioButton_Kline = QRadioButton(self.groupBox_ParseFileTpye)
        self.radioButton_Kline.setObjectName(u"radioButton_Kline")

        self.gridLayout_ParseFileType.addWidget(self.radioButton_Kline, 0, 1, 1, 1)

        self.radioButton_None = QRadioButton(self.groupBox_ParseFileTpye)
        self.radioButton_None.setObjectName(u"radioButton_None")
        self.radioButton_None.setChecked(True)

        self.gridLayout_ParseFileType.addWidget(self.radioButton_None, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_ParseFileTpye)

        self.groupBox_SaveFileFormat = QGroupBox(self.tab_Parser)
        self.groupBox_SaveFileFormat.setObjectName(u"groupBox_SaveFileFormat")
        self.gridLayout_SaveFileFormat = QGridLayout(self.groupBox_SaveFileFormat)
        self.gridLayout_SaveFileFormat.setObjectName(u"gridLayout_SaveFileFormat")
        self.checkBox_SaveFeather = QCheckBox(self.groupBox_SaveFileFormat)
        self.checkBox_SaveFeather.setObjectName(u"checkBox_SaveFeather")

        self.gridLayout_SaveFileFormat.addWidget(self.checkBox_SaveFeather, 0, 1, 1, 1)

        self.checkBox_SaveCSV = QCheckBox(self.groupBox_SaveFileFormat)
        self.checkBox_SaveCSV.setObjectName(u"checkBox_SaveCSV")
        self.checkBox_SaveCSV.setChecked(True)

        self.gridLayout_SaveFileFormat.addWidget(self.checkBox_SaveCSV, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_SaveFileFormat)

        self.groupBox_FileParserController = QGroupBox(self.tab_Parser)
        self.groupBox_FileParserController.setObjectName(u"groupBox_FileParserController")
        self.gridLayout_FileParserController = QGridLayout(self.groupBox_FileParserController)
        self.gridLayout_FileParserController.setObjectName(u"gridLayout_FileParserController")
        self.pushButton_ParseStart = QPushButton(self.groupBox_FileParserController)
        self.pushButton_ParseStart.setObjectName(u"pushButton_ParseStart")

        self.gridLayout_FileParserController.addWidget(self.pushButton_ParseStart, 0, 0, 1, 1)

        self.pushButton_ParseStop = QPushButton(self.groupBox_FileParserController)
        self.pushButton_ParseStop.setObjectName(u"pushButton_ParseStop")

        self.gridLayout_FileParserController.addWidget(self.pushButton_ParseStop, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_FileParserController)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.textBrowser_FileParseNotice = QTextBrowser(self.tab_Parser)
        self.textBrowser_FileParseNotice.setObjectName(u"textBrowser_FileParseNotice")
        self.textBrowser_FileParseNotice.setAutoFillBackground(False)

        self.verticalLayout_2.addWidget(self.textBrowser_FileParseNotice)

        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 3)
        self.verticalLayout_2.setStretch(2, 3)
        self.tabWidget.addTab(self.tab_Parser, "")
        self.tab_DataView = QWidget()
        self.tab_DataView.setObjectName(u"tab_DataView")
        self.verticalLayout_4 = QVBoxLayout(self.tab_DataView)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_DataView_Open = QPushButton(self.tab_DataView)
        self.pushButton_DataView_Open.setObjectName(u"pushButton_DataView_Open")

        self.gridLayout_2.addWidget(self.pushButton_DataView_Open, 0, 0, 1, 1)

        self.pushButton_DataView_Info = QPushButton(self.tab_DataView)
        self.pushButton_DataView_Info.setObjectName(u"pushButton_DataView_Info")

        self.gridLayout_2.addWidget(self.pushButton_DataView_Info, 0, 1, 1, 1)

        self.pushButton_DataView_Null = QPushButton(self.tab_DataView)
        self.pushButton_DataView_Null.setObjectName(u"pushButton_DataView_Null")

        self.gridLayout_2.addWidget(self.pushButton_DataView_Null, 0, 2, 1, 1)

        self.pushButton_DataView_Describe = QPushButton(self.tab_DataView)
        self.pushButton_DataView_Describe.setObjectName(u"pushButton_DataView_Describe")

        self.gridLayout_2.addWidget(self.pushButton_DataView_Describe, 0, 3, 1, 1)

        self.pushButton_DataView_Scatter = QPushButton(self.tab_DataView)
        self.pushButton_DataView_Scatter.setObjectName(u"pushButton_DataView_Scatter")

        self.gridLayout_2.addWidget(self.pushButton_DataView_Scatter, 0, 4, 1, 1)

        self.pushButton_DataView_KDE = QPushButton(self.tab_DataView)
        self.pushButton_DataView_KDE.setObjectName(u"pushButton_DataView_KDE")

        self.gridLayout_2.addWidget(self.pushButton_DataView_KDE, 0, 5, 1, 1)

        self.pushButton_DataView_PairPlot = QPushButton(self.tab_DataView)
        self.pushButton_DataView_PairPlot.setObjectName(u"pushButton_DataView_PairPlot")

        self.gridLayout_2.addWidget(self.pushButton_DataView_PairPlot, 0, 6, 1, 1)

        self.pushButton_DataView_CorrMap = QPushButton(self.tab_DataView)
        self.pushButton_DataView_CorrMap.setObjectName(u"pushButton_DataView_CorrMap")

        self.gridLayout_2.addWidget(self.pushButton_DataView_CorrMap, 0, 7, 1, 1)

        self.pushButton_DataView_Feature = QPushButton(self.tab_DataView)
        self.pushButton_DataView_Feature.setObjectName(u"pushButton_DataView_Feature")

        self.gridLayout_2.addWidget(self.pushButton_DataView_Feature, 0, 8, 1, 1)

        self.tableView_DataView = QTableView(self.tab_DataView)
        self.tableView_DataView.setObjectName(u"tableView_DataView")

        self.gridLayout_2.addWidget(self.tableView_DataView, 1, 0, 1, 9)


        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.tabWidget.addTab(self.tab_DataView, "")
        self.tab_Config = QWidget()
        self.tab_Config.setObjectName(u"tab_Config")
        self.pushButton_SaveConfig = QPushButton(self.tab_Config)
        self.pushButton_SaveConfig.setObjectName(u"pushButton_SaveConfig")
        self.pushButton_SaveConfig.setGeometry(QRect(480, 270, 75, 24))
        self.lineEdit_LogPath = QLineEdit(self.tab_Config)
        self.lineEdit_LogPath.setObjectName(u"lineEdit_LogPath")
        self.lineEdit_LogPath.setGeometry(QRect(120, 50, 421, 20))
        self.label = QLabel(self.tab_Config)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 50, 54, 16))
        self.tabWidget.addTab(self.tab_Config, "")
        self.splitter.addWidget(self.tabWidget)
        self.textEdit_Log = QTextEdit(self.splitter)
        self.textEdit_Log.setObjectName(u"textEdit_Log")
        font = QFont()
        font.setFamilies([u"Courier New"])
        font.setPointSize(9)
        self.textEdit_Log.setFont(font)
        self.splitter.addWidget(self.textEdit_Log)

        self.verticalLayout.addWidget(self.splitter)


        self.retranslateUi(MainForm)

        self.tabWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainForm)
    # setupUi

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QCoreApplication.translate("MainForm", u"Binance Downloader", None))
        self.groupBox_TradingType.setTitle(QCoreApplication.translate("MainForm", u"Trading Type", None))
        self.checkBox_spot.setText(QCoreApplication.translate("MainForm", u"spot", None))
        self.checkBox_um.setText(QCoreApplication.translate("MainForm", u"um", None))
        self.checkBox_cm.setText(QCoreApplication.translate("MainForm", u"cm", None))
        self.groupBox_DataType.setTitle(QCoreApplication.translate("MainForm", u"Data Type", None))
        self.checkBox_Kline.setText(QCoreApplication.translate("MainForm", u"kline", None))
        self.checkBox_AggTrade.setText(QCoreApplication.translate("MainForm", u"aggTrade", None))
        self.checkBox_Trade.setText(QCoreApplication.translate("MainForm", u"trade", None))
        self.groupBox_Interval.setTitle(QCoreApplication.translate("MainForm", u"Interval", None))
        self.checkBox_1m.setText(QCoreApplication.translate("MainForm", u"1 minute", None))
        self.checkBox_1h.setText(QCoreApplication.translate("MainForm", u"1 hour", None))
        self.checkBox_1d.setText(QCoreApplication.translate("MainForm", u"1 day", None))
        self.groupBox_DateRange.setTitle(QCoreApplication.translate("MainForm", u"Date Range", None))
        self.label_StartDate.setText(QCoreApplication.translate("MainForm", u"Start Date", None))
        self.label_EndDate.setText(QCoreApplication.translate("MainForm", u"End Date", None))
        self.groupBox_Proxy.setTitle(QCoreApplication.translate("MainForm", u"Proxy", None))
        self.checkBox_Proxy.setText(QCoreApplication.translate("MainForm", u"Addr", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_Proxy.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_Proxy.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_Proxy.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_Proxy.setInputMask("")
        self.lineEdit_Proxy.setPlaceholderText("")
        self.groupBox_Controller.setTitle(QCoreApplication.translate("MainForm", u"Controller", None))
        self.label_Step3.setText(QCoreApplication.translate("MainForm", u"Step 3", None))
        self.pushButton_DownloadSymbols.setText(QCoreApplication.translate("MainForm", u"Download Symbols", None))
        self.pushButton_DownloaderStart.setText(QCoreApplication.translate("MainForm", u"Start", None))
        self.pushButton_SetSavePath.setText(QCoreApplication.translate("MainForm", u"Set Save Path", None))
        self.label_Step2.setText(QCoreApplication.translate("MainForm", u"Step 2", None))
        self.pushButton_LoadSymbols.setText(QCoreApplication.translate("MainForm", u"Load Symbols", None))
        self.label_Step1.setText(QCoreApplication.translate("MainForm", u"Step 1", None))
        self.pushButton_DownloaderStop.setText(QCoreApplication.translate("MainForm", u"Stop", None))
        self.groupBox_Timer.setTitle(QCoreApplication.translate("MainForm", u"Timer (Auto Download Last Day's Data)", None))
        self.pushButton_TimerStop.setText(QCoreApplication.translate("MainForm", u"Stop", None))
        self.pushButton_TimerStart.setText(QCoreApplication.translate("MainForm", u"Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_HistoryData), QCoreApplication.translate("MainForm", u"Trading History Data", None))
        self.groupBoxFutures.setTitle(QCoreApplication.translate("MainForm", u"Futures Order Book Level 2", None))
        self.pushButtonFuturesOrderBookSpiderStart.setText(QCoreApplication.translate("MainForm", u"Start", None))
        self.labelEndTime.setText(QCoreApplication.translate("MainForm", u"To", None))
        self.labelBeginTime.setText(QCoreApplication.translate("MainForm", u"From", None))
        self.labelSecretKey.setText(QCoreApplication.translate("MainForm", u"Secret Key", None))
        self.labelAPIKey.setText(QCoreApplication.translate("MainForm", u"API Key", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_FuturesOrderBookLevel2), QCoreApplication.translate("MainForm", u"Futures Order Book Leve 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Realtime), QCoreApplication.translate("MainForm", u"Real-Time Data", None))
        self.groupBox_Path.setTitle(QCoreApplication.translate("MainForm", u"Path", None))
        self.label_Des.setText(QCoreApplication.translate("MainForm", u"Destination", None))
        self.label_Src.setText(QCoreApplication.translate("MainForm", u"Source", None))
        self.pushButton_SetDesDir.setText(QCoreApplication.translate("MainForm", u"Set", None))
        self.pushButton_SetSrcDir.setText(QCoreApplication.translate("MainForm", u"Set", None))
        self.groupBox_ParseFileFormat.setTitle(QCoreApplication.translate("MainForm", u"Parse File Format", None))
        self.checkBox_ParseZIP.setText(QCoreApplication.translate("MainForm", u"ZIP", None))
        self.checkBox_ParseCSV.setText(QCoreApplication.translate("MainForm", u"CSV", None))
        self.checkBox_ParseFeather.setText(QCoreApplication.translate("MainForm", u"Feather", None))
        self.groupBox_ParseFileTpye.setTitle(QCoreApplication.translate("MainForm", u"Parse File Type", None))
        self.radioButton_AggTrade.setText(QCoreApplication.translate("MainForm", u"aggTrade", None))
        self.radioButton_Trade.setText(QCoreApplication.translate("MainForm", u"trade", None))
        self.radioButton_Kline.setText(QCoreApplication.translate("MainForm", u"kline", None))
        self.radioButton_None.setText(QCoreApplication.translate("MainForm", u"none", None))
        self.groupBox_SaveFileFormat.setTitle(QCoreApplication.translate("MainForm", u"Save File Format", None))
        self.checkBox_SaveFeather.setText(QCoreApplication.translate("MainForm", u"Feather", None))
        self.checkBox_SaveCSV.setText(QCoreApplication.translate("MainForm", u"CSV", None))
        self.groupBox_FileParserController.setTitle(QCoreApplication.translate("MainForm", u"Controller", None))
        self.pushButton_ParseStart.setText(QCoreApplication.translate("MainForm", u"Start", None))
        self.pushButton_ParseStop.setText(QCoreApplication.translate("MainForm", u"Stop", None))
        self.textBrowser_FileParseNotice.setMarkdown(QCoreApplication.translate("MainForm", u"1. Unzip the zip files to the same direction and combine all csv and feather\n"
"files to one single csv and feather file. \n"
"\n"
"2. If the Parse File Tpye is checked, there will be an optimation after the\n"
"unzip progress, such as column name, datetime index, symbol name, etc.    \n"
"\n"
"", None))
        self.textBrowser_FileParseNotice.setHtml(QCoreApplication.translate("MainForm", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. Unzip the zip files to the same direction and combine all csv and feather files to one single csv and feather file. </p>\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. If the Parse File Tpye is checked, there will be an optimation after the unzip progress, such as column name, datetime index, symbol name, etc.    </p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Parser), QCoreApplication.translate("MainForm", u"File Parser", None))
        self.pushButton_DataView_Open.setText(QCoreApplication.translate("MainForm", u"Open", None))
        self.pushButton_DataView_Info.setText(QCoreApplication.translate("MainForm", u"Info", None))
        self.pushButton_DataView_Null.setText(QCoreApplication.translate("MainForm", u"Null", None))
        self.pushButton_DataView_Describe.setText(QCoreApplication.translate("MainForm", u"Describe", None))
        self.pushButton_DataView_Scatter.setText(QCoreApplication.translate("MainForm", u"Scatter", None))
        self.pushButton_DataView_KDE.setText(QCoreApplication.translate("MainForm", u"KDE", None))
        self.pushButton_DataView_PairPlot.setText(QCoreApplication.translate("MainForm", u"PairPlot", None))
        self.pushButton_DataView_CorrMap.setText(QCoreApplication.translate("MainForm", u"CorrMap", None))
        self.pushButton_DataView_Feature.setText(QCoreApplication.translate("MainForm", u"Feature", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_DataView), QCoreApplication.translate("MainForm", u"Data View", None))
        self.pushButton_SaveConfig.setText(QCoreApplication.translate("MainForm", u"Save", None))
        self.label.setText(QCoreApplication.translate("MainForm", u"Log Path", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Config), QCoreApplication.translate("MainForm", u"Config", None))
#if QT_CONFIG(tooltip)
        self.textEdit_Log.setToolTip("")
#endif // QT_CONFIG(tooltip)
    # retranslateUi

