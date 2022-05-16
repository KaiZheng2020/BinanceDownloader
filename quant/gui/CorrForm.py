import matplotlib.pyplot as plt
import seaborn
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg, NavigationToolbar2QT)
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QVBoxLayout, QWidget

from .resources import resources


class CorrForm(QWidget):
    def __init__(self):

        super(CorrForm, self).__init__()

        self.figure = plt.figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

        icon = QIcon()
        icon.addFile(u":/logo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        self.setWindowTitle('Correlation')

    def plot(self, data_df):

        self.figure.clear()
        self.ax = self.figure.subplots()
        self.spearman = data_df.corr('spearman')
        seaborn.heatmap(self.spearman, annot=True, fmt='.2f', ax=self.ax).set_title('Spearman')
        self.canvas.draw()
