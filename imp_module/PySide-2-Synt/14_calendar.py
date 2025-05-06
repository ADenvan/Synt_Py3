import sys
from PySide2.QtWidgets import \
    QApplication, QWidget, QPushButton, QMessageBox,\
    QDesktopWidget, QLabel, QToolBar, QLCDNumber, \
    QMainWindow, QStatusBar, QProgressBar, QDialog, QHBoxLayout, \
    QVBoxLayout, QGroupBox, QGridLayout, QCalendarWidget

from PySide2.QtGui import QIcon, QPixmap, QFont
from PySide2.QtCore import QTime, QTimer, SIGNAL

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide 2 - Calendar ") # Title.
        self.setGeometry(300, 300, 300, 300) # Положения окна.

        self.setIcon()
        self.createCalendar()

        self.show()

    def setIcon(self):
        appicon = QIcon("feather/anchor.svg")
        self.setWindowIcon(appicon)
    def createCalendar(self):
        vbox = QVBoxLayout()
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)

        vbox.addWidget(self.calendar)
        self.setLayout(vbox)


myApp = QApplication(sys.argv) #
window = Window() # Окно дисплея
window.show() # Показать окно.

myApp.exec_() # Выполнить.
sys.exit(0) # Выдим из цикла.