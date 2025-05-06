import sys
from PySide2.QtWidgets import \
    QApplication, QWidget, QPushButton, QMessageBox,\
    QDesktopWidget, QLabel, QToolBar, QLCDNumber, \
    QMainWindow, QStatusBar, QProgressBar, QDialog, QHBoxLayout, \
    QVBoxLayout, QGroupBox, QGridLayout, QCalendarWidget, \
    QCheckBox, QFontComboBox, QCompleter, QLineEdit

from PySide2.QtGui import QIcon, QPixmap, QFont
from PySide2.QtCore import QTime, QTimer, SIGNAL, Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide 2 - Completer") # Title.
        self.setGeometry(300, 300, 300, 300) # Положения окна.

        self.createCompleter()

        self.setIcon()
        self.show()

    def setIcon(self):
        appicon = QIcon("feather/anchor.svg")
        self.setWindowIcon(appicon)

    def createCompleter(self):
        vbox = QVBoxLayout()
        name = ["usa", "rus", "india", "japan"]
        completer = QCompleter(name)
        self.lineEdit = QLineEdit()
        self.lineEdit.setCompleter(completer)
        vbox.addWidget(self.lineEdit)
        self.setLayout(vbox)



myApp = QApplication(sys.argv) #
window = Window() # Окно дисплея
window.show() # Показать окно.

myApp.exec_() # Выполнить.
sys.exit(0) # Выдим из цикла.