from PySide2.QtWidgets import QApplication, QWidget, QSpinBox, QLabel, QVBoxLayout, QDoubleSpinBox
import sys
from PySide2.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 SpinBox")
        self.setGeometry(300,200,300,100)

        self.setIcon()

        self.spin_box()


        self.show()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)



    def spin_box(self):
        vbox = QVBoxLayout()

        self.label = QLabel()


        self.spinbox = QDoubleSpinBox()
        self.spinbox.setMinimum(10)
        self.spinbox.setMaximum(100)
        self.spinbox.valueChanged.connect(self.spin_value)

        vbox.addWidget(self.label)
        vbox.addWidget(self.spinbox)

        self.setLayout(vbox)


    def spin_value(self):
        self.label.setText("Current Value Is : " + str(self.spinbox.value()))



myapp = QApplication(sys.argv)
window = Window()
myapp.exec_()
sys.exit()