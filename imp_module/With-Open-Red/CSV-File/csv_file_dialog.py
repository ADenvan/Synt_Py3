import csv
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox, QTextEdit, QFileDialog


class QuizApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quiz App")
        # self.initUI()
        self.import_csv()
    def import_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Import CSV", "", "CSV Files (*.csv)")
        if file_path:
            self.db.import_from_csv(file_path)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    quiz_app = QuizApp()
    quiz_app.show()
    sys.exit(app.exec())
