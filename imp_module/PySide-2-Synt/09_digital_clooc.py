import sys
from PySide2.QtWidgets import \
    QApplication, QWidget, QPushButton, QMessageBox,\
    QDesktopWidget, QLabel, QToolBar, QLCDNumber

from PySide2.QtGui import QIcon, QPixmap, QFont
from PySide2.QtCore import QTime, QTimer, SIGNAL

# Наследуем от ЛСИД Дисплей класса.
class DigitalClock(QLCDNumber):
    def __init__(self, parent=None):
        super(DigitalClock, self).__init__(parent)

        self.setSegmentStyle((QLCDNumber.Filled))
        timer = QTimer(self)
        self.connect(timer, SIGNAL('timeout()'), self.showTime)
        timer.start(1000)
        self.showTime()
        self.setWindowTitle("Digital Clock")
        self.resize(300, 200)

        self.setIcon()
    def showTime(self):
        time =QTime.currentTime()
        text = time.toString("hh:mm")
        # Каждый второй секунде.
        if (time.second() % 2) == 0:
            # Отрисовка 3 Элемента
            text = text[:2] + ' ' + text[3:]
        self.display(text)

    def setIcon(self):
        appicon = QIcon("feather/anchor.svg")
        self.setWindowIcon(appicon)

myApp = QApplication(sys.argv) #
window = DigitalClock() # Окно дисплея
window.show() # Показать окно.

myApp.exec_() # Выполнить.
sys.exit(0) # Выдим из цикла.