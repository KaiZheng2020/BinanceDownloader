from PySide6.QtWidgets import QWidget

from .widgets.MainForm import Ui_MainForm


class MainForm(QWidget, Ui_MainForm):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
