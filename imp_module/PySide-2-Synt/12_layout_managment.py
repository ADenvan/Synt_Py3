import sys
from PySide2.QtWidgets import \
    QApplication, QWidget, QPushButton, QMessageBox,\
    QDesktopWidget, QLabel, QToolBar, QLCDNumber, \
    QMainWindow, QStatusBar, QProgressBar, QDialog, QHBoxLayout, \
    QVBoxLayout, QGroupBox

from PySide2.QtGui import QIcon, QPixmap, QFont
from PySide2.QtCore import QTime, QTimer, SIGNAL

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout Managment") # Title.
        self.setGeometry(300, 300, 300, 300) # Положения окна.

        self.setIcon()

        self.creatLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

        self.show()


    def setIcon(self):
        appicon = QIcon("feather/anchor.svg")
        self.setWindowIcon(appicon)

    def creatLayout(self):
        self.groupBox = QGroupBox("Please choose one Language")
        self.groupBox.setFont(QFont("Sanserif", 13))
        hbox = QHBoxLayout() # Горизонтальная


        button = QPushButton("CSS", self)
        button.setIcon(QIcon("feather/save.svg"))
        button.setMinimumHeight(40)
        hbox.addWidget(button)

        button_1 =QPushButton("C++", self)
        button_1.setIcon(QIcon("feather/box.svg"))
        button_1.setMinimumHeight(40)
        hbox.addWidget(button_1)

        button_2 =QPushButton("javaScript", self)
        button_2.setIcon(QIcon("feather/book.svg"))
        button_2.setMinimumHeight(40)
        hbox.addWidget(button_2)

        self.groupBox.setLayout(hbox)







myApp = QApplication(sys.argv) #
window = Window() # Окно дисплея
window.show() # Показать окно.

myApp.exec_() # Выполнить.
sys.exit(0) # Выдим из цикла.