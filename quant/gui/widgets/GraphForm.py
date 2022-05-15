# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GraphForm.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl,
                          Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage,
                         QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QSizePolicy, QWidget)


class Ui_GraphForm(object):
    def setupUi(self, GraphForm):
        if not GraphForm.objectName():
            GraphForm.setObjectName(u"GraphForm")
        GraphForm.resize(400, 300)
        self.gridLayout = QGridLayout(GraphForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.graphicsView = QGraphicsView(GraphForm)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)

        self.retranslateUi(GraphForm)

        QMetaObject.connectSlotsByName(GraphForm)

    # setupUi

    def retranslateUi(self, GraphForm):
        GraphForm.setWindowTitle(QCoreApplication.translate("GraphForm", u"Form", None))

    # retranslateUi
