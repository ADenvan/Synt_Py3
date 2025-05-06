from PySide2.QtWidgets import QApplication, QWidget
import sys

# Квласс Наследует от QWidget.
# Получаем доступ ко всем возможностям класса QWidget.
class Window(QWidget):

    def __init__(self): # Консеруктор
        super().__init__()

        self.setWindowTitle("PySid Window") # Title.
        self.setGeometry(300, 300, 300, 300) # Положения окна.

        # Ограничение окна.
        self.setMinimumHeight(100)
        self.setMinimumWidth(250)
        self.setMaximumHeight(200)
        self.setMaximumWidth(800)

myApp = QApplication(sys.argv) #
window = Window()
window.show() # Показать окно.

myApp.exec_() # Выполнить.
sys.exit(0) # Выдим из цикла.