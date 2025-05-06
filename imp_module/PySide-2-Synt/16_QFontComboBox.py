import sys
from PySide2.QtWidgets import \
    QApplication, QWidget, QPushButton, QMessageBox,\
    QDesktopWidget, QLabel, QToolBar, QLCDNumber, \
    QMainWindow, QStatusBar, QProgressBar, QDialog, QHBoxLayout, \
    QVBoxLayout, QGroupBox, QGridLayout, QCalendarWidget, \
    QCheckBox, QFontComboBox

from PySide2.QtGui import QIcon, QPixmap, QFont
from PySide2.QtCore import QTime, QTimer, SIGNAL, Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide 2 - Fond Box") # Title.
        self.setGeometry(300, 300, 300, 300) # Положения окна.

        self.setFontBox()
        self.setIcon()

        self.show()

    def setIcon(self):
        appicon = QIcon("feather/anchor.svg")
        self.setWindowIcon(appicon)

    def setFontBox(self):
        vbox = QVBoxLayout()
        fontcombobox = QFontComboBox()
        # Фильтр со списком шрифтов.
        fontcombobox.setFontFilters(QFontComboBox.MonospacedFonts)
        vbox.addWidget(fontcombobox)
        self.setLayout(vbox)


myApp = QApplication(sys.argv) #
window = Window() # Окно дисплея
window.show() # Показать окно.

myApp.exec_() # Выполнить.
sys.exit(0) # Выдим из цикла.