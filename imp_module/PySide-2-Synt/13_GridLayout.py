import sys
from PySide2.QtWidgets import \
    QApplication, QWidget, QPushButton, QMessageBox,\
    QDesktopWidget, QLabel, QToolBar, QLCDNumber, \
    QMainWindow, QStatusBar, QProgressBar, QDialog, QHBoxLayout, \
    QVBoxLayout, QGroupBox, QGridLayout

from PySide2.QtGui import QIcon, QPixmap, QFont
from PySide2.QtCore import QTime, QTimer, SIGNAL

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layout") # Title.
        self.setGeometry(300, 300, 300, 300) # Положения окна.

        self.setIcon()

        self.creatGridlayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)


        self.show()


    def setIcon(self):
        appicon = QIcon("feather/anchor.svg")
        self.setWindowIcon(appicon)

    def creatGridlayout(self):
        self.groupBox = QGroupBox("pleas choose One language")
        self.groupBox.setFont(QFont("Sanserif", 13))
        gridLayout = QGridLayout()

        button = QPushButton("C++", self)
        button.setIcon(QIcon("feather/award.svg"))
        gridLayout.addWidget(button, 0, 0)

        button_1 = QPushButton("Css", self)
        button_1.setIcon(QIcon('feather/feather.svg'))
        gridLayout.addWidget(button_1, 0, 1)

        button_2 = QPushButton("Javascript", self)
        button_2.setIcon(QIcon('feather/cpu.svg'))
        gridLayout.addWidget(button_2, 1, 0)

        button_3 = QPushButton("Python", self)
        button_3.setIcon(QIcon('feather/play.svg'))
        gridLayout.addWidget(button_3, 1, 1)

        self.groupBox.setLayout(gridLayout)

myApp = QApplication(sys.argv) #
window = Window() # Окно дисплея
window.show() # Показать окно.

myApp.exec_() # Выполнить.
sys.exit(0) # Выдим из цикла.