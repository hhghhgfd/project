from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import uic
import sys
from PostingTG import telegram_post
import vk_api
import json
from mimetypes import guess_type
from PostingVk import vk_post

telegram_bot_token = '5833708631:AAH3otkx2PXvhsGLXdxqyuv-Pr6IsAtioXc'
channel_login = '@boxofpitsa'

files_paths = []

group_id_vk = ''
login = ''
password = ''


# VK = vk_api.VkApi(login, password, app_id=2685278)
# VK.auth()
# VK = VK.get_api()
# access_token = 0

# try:
#     User = VK.users.get()
# except:
#     print("Error")
# else:
#     with open('vk_config.v2.json', 'r') as data_file:
#         data = json.load(data_file)
#
#     for xxx in data[login]['token'].keys():
#         for yyy in data[login]['token'][xxx].keys():
#             access_token = data[login]['token'][xxx][yyy]['access_token']
# vk_session = vk_api.VkApi(token=access_token)


class MainUI(QMainWindow):
    def __init__(self):
        self.files = []

        super().__init__()
        uic.loadUi("untitled_1.0.ui", self)
        self.post_button.clicked.connect(self.post)
        self.add_files_button.clicked.connect(self.add_files)
        self.repeat.clicked.connect(self.translation)
        # self.clean_one.clicked.connect(self.removeSel)
        self.clear_all.clicked.connect(self.delete)

    def add_files(self):
        files_selected = QFileDialog.getOpenFileNames(self, "Открыть файлы")
        for file in files_selected[0]:
            self.files.append(file)

    def translation(self):
        self.list_of_files.clear()
        self.list_of_files.addItems([x.split('/')[-1] for x in self.files])

    def post(self):
        if self.tg_checkbox.isChecked():
            print(telegram_post(telegram_bot_token=telegram_bot_token,
                                channel_login=channel_login, message=self.text_input.toPlainText()))
        if self.vk_checkbox.isChecked():
            print(vk_post(group_id_vk, message=self.text_input.toPlainText(), files_path=None))

    def removeSel(self):
        listItems = self.list_of_files.selectedItems()
        if not listItems: return
        for item in listItems:
            self.list_of_files.takeItem(self.list_of_files.row(item))
        self.files = [self.list_of_files.item(x).text() for x in range(self.list_of_files.count())]

    def delete(self):
        self.list_of_files.clear()

    # def vk_post(group_id_vk, message="", files_path=None):
    #     if files_paths:
    #         media = []
    #         upload = vk_api.VkUpload(vk_session)
    #         for file in files_paths:
    #             file_type = guess_type(file)[0].split("/")
    #             if file_type[0] == "image":
    #                 photo = upload.photo(file, album_id="299120623", group_id=group_id_vk[1:])
    #                 media.append('photo{}_{}'.format(photo[0]['owner_id'], photo[0]['id']))
    #             elif file_type[0] == "video":
    #                 video = upload.photo(file, album_id="299120623", group_id=group_id_vk[1:])
    #                 media.append('video{}_{}'.format(video[0]['owner_id'], video[0]['id']))
    #         vk_session.method('wall.post', {
    #             'owner_id': group_id_vk,
    #             'from_group': 1,
    #             'message': message,
    #             'attachments': ', '.join(media),
    #         })
    #     else:
    #         vk_session.method('wall.post', {
    #             'owner_id': group_id_vk,
    #             'from_group': 1,
    #             'message': message,
    #         })


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()
