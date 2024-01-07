from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import uic
import sys
from PostingTG import telegram_post


class MainUI(QMainWindow):
    def __init__(self):
        self.files = []

        super().__init__()
        uic.loadUi("untitled.ui", self)
        self.post_button.clicked.connect(self.post)
        self.add_files_button.clicked.connect(self.add_files)

    def post(self):
        if self.tg_checkbox.isChecked():
            print(telegram_post(telegram_bot_token="",
                                channel_login="@", message=self.text_input.toPlainText()))

    def add_files(self):
        files_selected = QFileDialog.getOpenFileNames(self, "Открыть файлы")
        for file in files_selected[0]:
            self.files.append(file)
        print(self.files)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()
