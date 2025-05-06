import sys
from PySide2.QtWidgets import \
    QApplication, QWidget, QPushButton, QMessageBox,\
    QDesktopWidget, QLabel, QToolBar, QLCDNumber, \
    QMainWindow, QStatusBar, QProgressBar

from PySide2.QtGui import QIcon, QPixmap, QFont
from PySide2.QtCore import QTime, QTimer, SIGNAL


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About Box Creat") # Title.
        self.setGeometry(300, 300, 300, 300) # Положения окна.

        self.statusLabel = QLabel("Showing Progress")
        self.progressbar = QProgressBar()
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(100)

        self.setIcon()

        self.createStatusBar()

    def setIcon(self):
        appicon = QIcon("feather/anchor.svg")
        self.setWindowIcon(appicon)

    def createStatusBar(self):
        self.statusBar = QStatusBar()
        self.progressbar.setValue(10) # % Прогрес заполнен на 10 %
        self.statusBar.addWidget(self.statusLabel, 1)
        self.statusBar.addWidget(self.progressbar, 2)
        self.setStatusBar(self.statusBar)





myApp = QApplication(sys.argv) #
window = Window() # Окно дисплея
window.show() # Показать окно.

myApp.exec_() # Выполнить.
sys.exit(0) # Выдим из цикла.