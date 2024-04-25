from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QInputDialog, QMessageBox
from PyQt5 import uic
import sys
from PostingTG import telegram_post
from PostingVk import vk_post
from json import dump, load
from os import path


class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("interface.ui", self)

        if not path.exists('user_data.txt'):
            self.user_data = {
                'TG': 'group_id',
                'VK': ['token', 'id']
            }
            with open('user_data.txt', 'w') as f:
                dump(self.user_data, f)
        else:
            with open('user_data.txt', 'r') as f:
                self.user_data = load(f)

        self.files = []
        self.post_button.clicked.connect(self.post)
        self.add_files_button.clicked.connect(self.add_files)
        self.clear_one.clicked.connect(self.detach_one)
        self.clear_all.clicked.connect(self.detach_all)
        self.actionTelegram.triggered.connect(self.link_telegram)
        self.actionVK.triggered.connect(self.link_vk)

    def add_files(self):
        files_selected = QFileDialog.getOpenFileNames(self, "Открыть файлы")
        for file in files_selected[0]:
            self.files.append(file)
        self.list_of_files.clear()
        self.list_of_files.addItems([x.split('/')[-1] for x in self.files])

    def post(self):
        if self.tg_checkbox.isChecked():
            code, msg_text = telegram_post(channel_login=self.user_data["TG"], message=self.text_input.toPlainText(),
                                files_paths=self.files)
            if code:
                msg = QMessageBox()
                msg.setWindowTitle("Успешно")
                msg.setText(msg_text)
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText(msg_text)
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()

        if self.vk_checkbox.isChecked():
            code, msg_text = vk_post(access_token=self.user_data["VK"][0], group_id_vk=self.user_data["VK"][1],
                          message=self.text_input.toPlainText(), files_paths=self.files)
            if code:
                msg = QMessageBox()
                msg.setWindowTitle("Успешно")
                msg.setText(msg_text)
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText(msg_text)
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()

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

    def link_telegram(self):
        msg = QMessageBox()
        msg.setWindowTitle("Добавьте нашего бота")
        msg.setText("Добавьте @school_crossposting_bot как администратора в свой канал и выдайте ему права поста")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

        self.user_data['TG'] = QInputDialog.getText(self, 'Логин канала', 'Введите логин канала (@your_channel):')[0]
        with open('user_data.txt', 'w') as f:
            dump(self.user_data, f)

    def link_vk(self):
        self.user_data['VK'][0] = QInputDialog.getText(self, 'Токен для работы с сообществом', 'Введите токен:')[0]
        self.user_data['VK'][1] = QInputDialog.getText(self, 'ID канала', 'Введите id сообщества:')[0]
        with open('user_data.txt', 'w') as f:
            dump(self.user_data, f)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()
