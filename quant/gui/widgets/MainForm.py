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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QSplitter,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        if not MainForm.objectName():
            MainForm.setObjectName(u"MainForm")
        MainForm.resize(800, 600)
        MainForm.setMinimumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u":/icon/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainForm.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(MainForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(MainForm)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter = QSplitter(self.widget)
        self.splitter.setObjectName(u"splitter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.splitter.setMaximumSize(QSize(16777215, 16777215))
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setHandleWidth(5)
        self.tabWidget = QTabWidget(self.splitter)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 300))
        self.tab_config = QWidget()
        self.tab_config.setObjectName(u"tab_config")
        self.pushButton = QPushButton(self.tab_config)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 180, 141, 24))
        self.tabWidget.addTab(self.tab_config, "")
        self.tab_spot_history_data = QWidget()
        self.tab_spot_history_data.setObjectName(u"tab_spot_history_data")
        self.pushButtonSymbolsLoad = QPushButton(self.tab_spot_history_data)
        self.pushButtonSymbolsLoad.setObjectName(u"pushButtonSymbolsLoad")
        self.pushButtonSymbolsLoad.setGeometry(QRect(30, 30, 141, 24))
        self.tabWidget.addTab(self.tab_spot_history_data, "")
        self.tab_futures_history_data = QWidget()
        self.tab_futures_history_data.setObjectName(u"tab_futures_history_data")
        self.tabWidget.addTab(self.tab_futures_history_data, "")
        self.tab_futures_order_book_level_2 = QWidget()
        self.tab_futures_order_book_level_2.setObjectName(u"tab_futures_order_book_level_2")
        self.tabWidget.addTab(self.tab_futures_order_book_level_2, "")
        self.splitter.addWidget(self.tabWidget)
        self.textEdit = QTextEdit(self.splitter)
        self.textEdit.setObjectName(u"textEdit")
        self.splitter.addWidget(self.textEdit)

        self.verticalLayout_2.addWidget(self.splitter)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(MainForm)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainForm)
    # setupUi

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QCoreApplication.translate("MainForm", u"Binance Downloader", None))
        self.pushButton.setText(QCoreApplication.translate("MainForm", u"Download All Symbols", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_config), QCoreApplication.translate("MainForm", u"Config", None))
        self.pushButtonSymbolsLoad.setText(QCoreApplication.translate("MainForm", u"Load", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_spot_history_data), QCoreApplication.translate("MainForm", u"Spot History Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_futures_history_data), QCoreApplication.translate("MainForm", u"Futures History Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_futures_order_book_level_2), QCoreApplication.translate("MainForm", u"Futures Order Book Leve 2", None))
    # retranslateUi

