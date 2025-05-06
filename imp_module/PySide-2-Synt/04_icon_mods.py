from PySide2.QtWidgets import QApplication, QWidget, QLabel, QToolBar
import sys
from PySide2.QtGui import QIcon, QPixmap, QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Icon Modes")
        self.setGeometry(300,300, 500,400)

        # window.setIconModes -тожу самое
        self.setIcon()
        self.setIconModes()
    def setIcon(self):
        appIcon = QIcon("feather/archive.svg")
        self.setWindowIcon(appIcon)

    def setIconModes(self):
        icon1 = QIcon("feather/airplay.svg")
        label1 = QLabel('Sample', self)
        pixmap1 = icon1.pixmap(100,100, QIcon.Active, QIcon.On)
        label1.setPixmap(pixmap1) # Крайний левый угол.

        icon2 = QIcon("feather/arrow-up.svg")
        label2 = QLabel('Sample', self)
        pixmap2 = icon2.pixmap(100, 100, QIcon.Disabled, QIcon.Off)
        label2.setPixmap(pixmap2)
        label2.move(100,0) # Смещение.

        icon3 = QIcon("feather/airplay.svg")
        label3 = QLabel('Sample', self)
        pixmap3 = icon3.pixmap(100, 100, QIcon.Selected, QIcon.On)
        label3.setPixmap(pixmap3)
        label3.move(200, 0) # Смещение.

myApp = QApplication(sys.argv)
window = Window()

# Вывод в окно приложения.
# window.setIcon()
# window.setIconModes()
window.show()

myApp.exec_()
sys.exit(0)