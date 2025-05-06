from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit
import sys
from PySide2.QtGui import QIcon, QFont
from PySide2.QtPrintSupport import QPrinter, QPrintPreviewDialog


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple Notepad App")
        self.setGeometry(300,200,1280,600)

        self.textEdit = QTextEdit(self)
        self.textEdit.setFont(QFont('Sanserif', 13))
        self.setCentralWidget(self.textEdit)


        self.setIcon()

        self.create_menu()
        self.show()



    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)


    def create_menu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        viewMenu = mainMenu.addMenu('View')
        editMenu = mainMenu.addMenu('Edit')
        fontMenu = mainMenu.addMenu('Font')
        helpMenu = mainMenu.addMenu('Help')


        openAction = QAction(QIcon('feather/octagon.svg'), "Open", self)
        openAction.setShortcut('Ctrl+O')


        saveAction = QAction(QIcon('feather/save.svg'), "Save", self)
        saveAction.setShortcut('Ctrl+S')

        exitAction = QAction(QIcon('exit.png'), "Exit", self)
        exitAction.setShortcut('Ctrl+X')


        previewAction = QAction(QIcon('feather/file.svg'), "Print Preview", self)

        exitAction.triggered.connect(self.exit_app)

        previewAction.triggered.connect(self.print_preview_dialog)

        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(exitAction)

        viewMenu.addAction(previewAction)

    def exit_app(self):
        self.close()

    def print_preview_dialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)

        previewDialog.paintRequested.connect(self.print_preview)
        previewDialog.exec_()

    def print_preview(self, printer):
        self.textEdit.print_(printer)

myapp = QApplication(sys.argv)
window = Window()
myapp.exec_()
sys.exit()