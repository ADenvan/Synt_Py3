from PySide2.QtWidgets import QApplication, QDialog, QLCDNumber, QVBoxLayout
import sys
from PySide2.QtCore import QTime, QTimer

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 system Clock")
        self.setGeometry(300,200,200,100)

        timer = QTimer()

        timer.timeout.connect(self.show_clock)

        timer.start(1000)

        self.show_clock()


        self.show()


    def show_clock(self):
        vbox = QVBoxLayout()
        lcd = QLCDNumber()
        lcd.setStyleSheet('color:green')
        lcd.setStyleSheet('background:yellow')

        vbox.addWidget(lcd)

        time = QTime.currentTime()
        text = time.toString('hh:mm')
        lcd.display(text)

        self.setLayout(vbox)

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())