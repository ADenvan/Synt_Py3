import sys
from PySide2.QtWidgets import \
    QApplication, QWidget, QPushButton, QMessageBox,\
    QDesktopWidget, QLabel, QToolBar, QLCDNumber, \
    QMainWindow, QStatusBar, QProgressBar, QDialog, QHBoxLayout, \
    QVBoxLayout, QGroupBox, QGridLayout, QCalendarWidget, \
    QCheckBox, QFontComboBox, QCompleter, QLineEdit, QSlider

from PySide2.QtGui import QIcon, QPixmap, QFont
from PySide2.QtCore import QTime, QTimer, SIGNAL, Qt
from PySide2 import QtGui

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide 2 - Slider") # Title.
        self.setGeometry(300, 300, 300, 300) # Положения окна.

        self.setStyleSheet('background-color:red')

        self.createSlaider()

        self.setIcon()
        self.show()

    def setIcon(self):
        appicon = QIcon("feather/anchor.svg")
        self.setWindowIcon(appicon)

    def createSlaider(self):
        hbox = QHBoxLayout()
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal) # Горизонтальное
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)

        self.slider.valueChanged.connect(self.changedValue)

        self.label = QLabel("0")
        self.label.setFont(QtGui.QFont("Sanserif", 15))

        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)
        self.setLayout(hbox)

    # Изменение значения ползунка.
    def changedValue(self):
        size = self.slider.value()
        self.label.setText(str(size))



myApp = QApplication(sys.argv) #
window = Window() # Окно дисплея
window.show() # Показать окно.

myApp.exec_() # Выполнить.
sys.exit(0) # Выдим из цикла.