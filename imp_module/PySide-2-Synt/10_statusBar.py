import sys
from PySide2.QtWidgets import \
    QApplication, QWidget, QPushButton, QMessageBox,\
    QDesktopWidget, QLabel, QToolBar, QLCDNumber, \
    QMainWindow, QStatusBar

from PySide2.QtGui import QIcon, QPixmap, QFont
from PySide2.QtCore import QTime, QTimer, SIGNAL

# Наследуем от ЛСИД Дисплей класса.
class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About Box Creat") # Title.
        self.setGeometry(300, 300, 300, 300) # Положения окна.

        self.setIcon()
        self.createStatusbar()

    def setIcon(self):
        appicon = QIcon("feather/anchor.svg")
        self.setWindowIcon(appicon)

    def createStatusbar(self):

        self.myStatus = QStatusBar()
        # Строка состояния.
        self.myStatus.showMessage("Status Bar is ", 3000)
        self.setStatusBar(self.myStatus)



myApp = QApplication(sys.argv) #
window = Window() # Окно дисплея
window.show() # Показать окно.

myApp.exec_() # Выполнить.
sys.exit(0) # Выдим из цикла.
