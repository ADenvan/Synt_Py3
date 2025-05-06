import sys
from PySide2.QtWidgets import \
    QApplication, QWidget, QPushButton, QMessageBox, QLabel, QToolBar

from PySide2.QtGui import QIcon, QPixmap, QFont

# Квласс Наследует от QWidget.
# Получаем доступ ко всем возможностям класса QWidget.
class Window(QWidget):
    def __init__(self): # Консеруктор
        super().__init__()
        self.setWindowTitle("Pyside2 Qt Push Button") # Title.
        self.setGeometry(300, 300, 300, 300) # Положения окна.

        self.setIcon()
        self.setButton()
    def setIcon(self):
        appicon =QIcon("feather/anchor.svg")
        self.setWindowIcon(appicon)

    # Отрисовка кнопки.
    def setButton(self):
        btn_1 = QPushButton("Quit", self) # Названия.
        btn_1.move(50, 100)
        # Действие по Слушателю.
        btn_1.clicked.connect(self.quiteApp)

    # Слушатель сигнала
    def quiteApp(self):
        userInfo = QMessageBox.question(self, "Имя приложения !", "Do you want Quit ?",
                                        QMessageBox.Yes | QMessageBox.No)
        if userInfo == QMessageBox.Yes:
            myApp.quit()
        elif userInfo == QMessageBox.No:
            pass

myApp = QApplication(sys.argv) #
window = Window()
window.show() # Показать окно.

myApp.exec_() # Выполнить.
sys.exit(0) # Выдим из цикла.