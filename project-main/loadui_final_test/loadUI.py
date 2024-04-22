from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import uic
import sys
from PostingTG import telegram_post
from PostingVk import vk_post

telegram_bot_token = ''
channel_login = ''

group_id_vk = ''
login = ''
password = ''


class MainUI(QMainWindow):
    def __init__(self):
        self.files = []

        super().__init__()
        uic.loadUi("interface.ui", self)
        self.post_button.clicked.connect(self.post)
        self.add_files_button.clicked.connect(self.add_files)
        self.clear_one.clicked.connect(self.detach_one)
        self.clear_all.clicked.connect(self.detach_all)

    def add_files(self):
        files_selected = QFileDialog.getOpenFileNames(self, "Открыть файлы")
        for file in files_selected[0]:
            self.files.append(file)
        self.list_of_files.clear()
        self.list_of_files.addItems([x.split('/')[-1] for x in self.files])

    def post(self):
        if self.tg_checkbox.isChecked():
            print(telegram_post(telegram_bot_token=telegram_bot_token,
                                channel_login=channel_login, message=self.text_input.toPlainText(),
                                files_paths=self.files))
        if self.vk_checkbox.isChecked():
            print(vk_post(login=login, password=password, group_id_vk=group_id_vk,
                          message=self.text_input.toPlainText(), files_paths=self.files))

    def detach_one(self):
        list_items = self.list_of_files.selectedItems()
        if not list_items:
            return
        for item in list_items:
            self.list_of_files.takeItem(self.list_of_files.row(item))
        self.files = [self.list_of_files.item(x).text() for x in range(self.list_of_files.count())]

    def detach_all(self):
        self.list_of_files.clear()
        self.files.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()
