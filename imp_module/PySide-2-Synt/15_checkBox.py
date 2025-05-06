import sys
from PySide2.QtWidgets import \
    QApplication, QWidget, QPushButton, QMessageBox,\
    QDesktopWidget, QLabel, QToolBar, QLCDNumber, \
    QMainWindow, QStatusBar, QProgressBar, QDialog, QHBoxLayout, \
    QVBoxLayout, QGroupBox, QGridLayout, QCalendarWidget, \
    QCheckBox

from PySide2.QtGui import QIcon, QPixmap, QFont
from PySide2.QtCore import QTime, QTimer, SIGNAL, Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide 2 - QCheckBox") # Title.
        self.setGeometry(300, 300, 300, 300) # Положения окна.

        self.setIcon()

        self.createCheckBox()
        self.show()

    def setIcon(self):
        appicon = QIcon("feather/anchor.svg")
        self.setWindowIcon(appicon)

    def createCheckBox(self):
        vbox = QVBoxLayout()
        self.label = QLabel("", self)

        check = QCheckBox("I Like Football", self)
        # Вызов - Изменение переключателя
        check.stateChanged.connect(self.checkBoxChenge)
        check.toggle()

        vbox.addWidget(check)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def checkBoxChenge(self, state):
        if state == Qt.Checked: # Переключатель.
            self.label.setText("Yes i Like python")
        else:
            self.label.setText("No i Like JS")

myApp = QApplication(sys.argv) #
window = Window() # Окно дисплея
window.show() # Показать окно.

myApp.exec_() # Выполнить.
sys.exit(0) # Выдим из цикла.