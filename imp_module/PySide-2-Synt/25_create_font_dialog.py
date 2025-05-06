from PySide2.QtWidgets import QApplication, QMainWindow, QAction,QFontDialog , QTextEdit, QFileDialog
import sys
from PySide2.QtGui import QIcon, QFont
from PySide2.QtPrintSupport import QPrinter, QPrintPreviewDialog, QPrintDialog
from PySide2.QtCore import QFileInfo


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple Notepad App")
        self.setGeometry(300,200,700,500)

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

        # open action
        openAction = QAction(QIcon('open.png'), "Open", self)
        openAction.setShortcut('Ctrl+O')

        # save action
        saveAction = QAction(QIcon('save.png'), "Save", self)
        saveAction.setShortcut('Ctrl+S')

        # exit action
        exitAction = QAction(QIcon('exit.png'), "Exit", self)
        exitAction.setShortcut('Ctrl+X')


        #print previeq action
        previewAction = QAction(QIcon('printpreview.png'), "Print Preview", self)

        # print action
        printAction = QAction(QIcon('print.png'), "Print", self)
        printAction.setShortcut("Ctrl+P")


        #export as pdf newly added for this article
        pdfAction = QAction(QIcon('pdf.png'), "Export PDF", self)


        #font action
        fontAction = QAction(QIcon('font.png'), "Font", self)




        #signals for the actions
        exitAction.triggered.connect(self.exit_app)
        previewAction.triggered.connect(self.print_preview_dialog)
        printAction.triggered.connect(self.print_dialog)
        pdfAction.triggered.connect(self.pdf_export)
        fontAction.triggered.connect(self.font_dialog)




        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(exitAction)

        viewMenu.addAction(previewAction)
        viewMenu.addAction(printAction)
        viewMenu.addAction(pdfAction)

        fontMenu.addAction(fontAction)



    def exit_app(self):
        self.close()


    def print_preview_dialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)

        previewDialog.paintRequested.connect(self.print_preview)
        previewDialog.exec_()




    def print_preview(self, printer):
        self.textEdit.print_(printer)



    def print_dialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.textEdit.print_(printer)


    def pdf_export(self):
        fn, _ = QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files (.pdf); All files")

        if fn != '':

            if QFileInfo(fn).suffix() == "": fn += '.pdf'

            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print_(printer)


    def font_dialog(self):
        (ok, font) = QFontDialog.getFont()

        if ok:
            self.textEdit.setFont(font)


myapp = QApplication(sys.argv)
window = Window()
myapp.exec_()
sys.exit()