from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import uic
import sys
from PostingTG import telegram_post
from PostingVk import vk_post

telegram_bot_token = '5833708631:AAH3otkx2PXvhsGLXdxqyuv-Pr6IsAtioXc'
channel_login = '@boxofpitsa'
group_id_vk = '-223288989'


class MainUI(QMainWindow):
    def __init__(self):
        self.files = []
        super().__init__()
        uic.loadUi("untitled_1.0.ui", self)
        self.post_button.clicked.connect(self.post)
        self.add_files_button.clicked.connect(self.add_files)
        self.clear_one.clicked.connect(self.removecell)
        self.clear_all.clicked.connect(self.delete)

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
            print(vk_post(group_id_vk, message=self.text_input.toPlainText(), files_path=None))

    def removecell(self):
        listItems = self.list_of_files.selectedItems()
        if not listItems: return
        for item in listItems:
            self.list_of_files.takeItem(self.list_of_files.row(item))
        self.files = [self.list_of_files.item(x).text() for x in range(self.list_of_files.count())]

    def delete(self):
        self.list_of_files.clear()
        self.files.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()
