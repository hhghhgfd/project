import pkgutil

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QInputDialog
from PyQt5 import uic
import sys
from PostingTG import telegram_post
from PostingVk import vk_post

telegram_bot_token = ''
channel_login = ''

group_id_vk = ''
login = ''
password = ''

# создание исходного файла
user_data = [
    'Телеграм\n',
    '1\n',
    '2\n',
    'Вконтакте\n',
    '3\n',
    '4\n'
]
with open('user_data.txt', 'w+') as f:
    f.writelines(user_data)


class MainUI(QMainWindow):
    def __init__(self):

        super().__init__()
        uic.loadUi("interface.ui", self)
        self.post_button.clicked.connect(self.post)
        self.add_files_button.clicked.connect(self.add_files)
        self.clear_one.clicked.connect(self.detach_one)
        self.clear_all.clicked.connect(self.detach_all)
        self.actionTelegram.triggered.connect(self.action_Telegram)
        self.actionVK.triggered.connect(self.action_VK)

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
            print(vk_post(access_token=self.access_token, group_id_vk=group_id_vk,
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

    def action_Telegram(self):
        self.bot_token = QInputDialog.getText(self, 'Токен бота', 'Введите токен бота:')
        # это всё попытки изменить содержимое файла
        # with open('user_data.txt', 'r') as f:
        #     old_data = f.read()
        #
        # new_data = old_data.replace(f.readlines()[1], self.bot_token)
        #
        # with open('user_data.txt', 'w') as f:
        #     f.write(new_data)
        #     print(f.readlines())
        #
        self.channel_login = QInputDialog.getText(self, 'Логин канала', 'Введите ваш логин:')

    def action_VK(self):
        self.access_token = QInputDialog.getText(self, 'Токен для работы с сообществом', 'Введите токен:')
        self.group_id_vk = QInputDialog.getText(self, 'ID канала', 'Введите id сообщества:')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()
