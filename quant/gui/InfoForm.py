from PyQt5.QtCore import QDate, QObject, QSize, Signal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget

from .resources import resources
from .widgets.InfoForm import Ui_InfoForm


class InfoForm(QWidget, Ui_InfoForm):
    def __init__(self):
        super().__init__()

        self.gui = Ui_InfoForm()
        self.gui.setupUi(self)

        icon = QIcon()
        icon.addFile(u":/logo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
