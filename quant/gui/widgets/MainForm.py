# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainForm.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, Qt, QTime,
                            QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QDateTimeEdit, QGridLayout, QGroupBox, QHBoxLayout, QLabel,
                               QLayout, QLineEdit, QPushButton, QSizePolicy, QSplitter, QTabWidget, QTextEdit, QTimeEdit,
                               QVBoxLayout, QWidget)

from ..resources import resources


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
        self.dateEdit_EndDate.setDateTime(QDateTime(QDate(2021, 12, 26), QTime(0, 0, 0)))
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
        self.label_Step1 = QLabel(self.groupBox_Controller)
        self.label_Step1.setObjectName(u"label_Step1")
        self.label_Step1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_Step1, 0, 0, 1, 1)

        self.label_Step2 = QLabel(self.groupBox_Controller)
        self.label_Step2.setObjectName(u"label_Step2")
        self.label_Step2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_Step2, 1, 0, 1, 1)

        self.pushButton_SetSavePath = QPushButton(self.groupBox_Controller)
        self.pushButton_SetSavePath.setObjectName(u"pushButton_SetSavePath")

        self.gridLayout.addWidget(self.pushButton_SetSavePath, 1, 1, 1, 2)

        self.label_Step3 = QLabel(self.groupBox_Controller)
        self.label_Step3.setObjectName(u"label_Step3")
        self.label_Step3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_Step3, 2, 0, 1, 1)

        self.pushButton_DownloaderStart = QPushButton(self.groupBox_Controller)
        self.pushButton_DownloaderStart.setObjectName(u"pushButton_DownloaderStart")

        self.gridLayout.addWidget(self.pushButton_DownloaderStart, 2, 1, 1, 1)

        self.pushButton_DownloadSymbols = QPushButton(self.groupBox_Controller)
        self.pushButton_DownloadSymbols.setObjectName(u"pushButton_DownloadSymbols")

        self.gridLayout.addWidget(self.pushButton_DownloadSymbols, 0, 1, 1, 1)

        self.pushButton_LoadSymbols = QPushButton(self.groupBox_Controller)
        self.pushButton_LoadSymbols.setObjectName(u"pushButton_LoadSymbols")

        self.gridLayout.addWidget(self.pushButton_LoadSymbols, 0, 2, 1, 1)

        self.pushButton_DownloaderStop = QPushButton(self.groupBox_Controller)
        self.pushButton_DownloaderStop.setObjectName(u"pushButton_DownloaderStop")

        self.gridLayout.addWidget(self.pushButton_DownloaderStop, 2, 2, 1, 1)

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
        self.tab_Utility = QWidget()
        self.tab_Utility.setObjectName(u"tab_Utility")
        self.groupBox_CSV2Feature = QGroupBox(self.tab_Utility)
        self.groupBox_CSV2Feature.setObjectName(u"groupBox_CSV2Feature")
        self.groupBox_CSV2Feature.setGeometry(QRect(130, 70, 481, 80))
        self.tabWidget.addTab(self.tab_Utility, "")
        self.tab_About = QWidget()
        self.tab_About.setObjectName(u"tab_About")
        self.tabWidget.addTab(self.tab_About, "")
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

        self.tabWidget.setCurrentIndex(0)

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
        self.label_Step1.setText(QCoreApplication.translate("MainForm", u"Step 1", None))
        self.label_Step2.setText(QCoreApplication.translate("MainForm", u"Step 2", None))
        self.pushButton_SetSavePath.setText(QCoreApplication.translate("MainForm", u"Set Save Path", None))
        self.label_Step3.setText(QCoreApplication.translate("MainForm", u"Step 3", None))
        self.pushButton_DownloaderStart.setText(QCoreApplication.translate("MainForm", u"Start", None))
        self.pushButton_DownloadSymbols.setText(QCoreApplication.translate("MainForm", u"Download Symbols", None))
        self.pushButton_LoadSymbols.setText(QCoreApplication.translate("MainForm", u"Load Symbols", None))
        self.pushButton_DownloaderStop.setText(QCoreApplication.translate("MainForm", u"Stop", None))
        self.groupBox_Timer.setTitle(QCoreApplication.translate("MainForm", u"Timer (Auto Download Last Day's Data)", None))
        self.pushButton_TimerStop.setText(QCoreApplication.translate("MainForm", u"Stop", None))
        self.pushButton_TimerStart.setText(QCoreApplication.translate("MainForm", u"Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_HistoryData),
                                  QCoreApplication.translate("MainForm", u"Trading History Data", None))
        self.groupBoxFutures.setTitle(QCoreApplication.translate("MainForm", u"Futures Order Book Level 2", None))
        self.pushButtonFuturesOrderBookSpiderStart.setText(QCoreApplication.translate("MainForm", u"Start", None))
        self.labelEndTime.setText(QCoreApplication.translate("MainForm", u"To", None))
        self.labelBeginTime.setText(QCoreApplication.translate("MainForm", u"From", None))
        self.labelSecretKey.setText(QCoreApplication.translate("MainForm", u"Secret Key", None))
        self.labelAPIKey.setText(QCoreApplication.translate("MainForm", u"API Key", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_FuturesOrderBookLevel2),
                                  QCoreApplication.translate("MainForm", u"Futures Order Book Leve 2", None))
        self.groupBox_CSV2Feature.setTitle(QCoreApplication.translate("MainForm", u"CSV to Feature", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Utility),
                                  QCoreApplication.translate("MainForm", u"CSV Utility", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_About),
                                  QCoreApplication.translate("MainForm", u"About", None))
        #if QT_CONFIG(tooltip)
        self.textEdit_Log.setToolTip("")


#endif // QT_CONFIG(tooltip)
# retranslateUi
