import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from configFW import Ui_MainWindow
from configSW import Ui_OtherWindow
from telebot import TeleBot, types
from mimetypes import guess_type
import vk_api
import json
import sqlite3


files_paths = []

TELEGRAM_BOT_TOKEN = '5833708631:AAH3otkx2PXvhsGLXdxqyuv-Pr6IsAtioXc'
CHANEL_LOGIN = '@boxofpitsa'

group_id_vk = '-223288989'
login = '79966980274'
password = 'KtoBilol07('

try:
    VK = vk_api.VkApi(login, password, app_id=2685278)
    VK.auth()
    VK = VK.get_api()
    access_token = 0

    try:
        User = VK.users.get()
    except:
        print("Error")
    else:
        with open('vk_config.v2.json', 'r') as data_file:
            data = json.load(data_file)

        for xxx in data[login]['token'].keys():
            for yyy in data[login]['token'][xxx].keys():
                access_token = data[login]['token'][xxx][yyy]['access_token']
    vk_session = vk_api.VkApi(token=access_token)
except:
    print('ну и хуйня, братан')


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Button_Menu.clicked.connect(self.openOtherWindow)
        self.PostButton.clicked.connect(self.post)
        self.FileButton.clicked.connect(self.add_files)
        # self.Input_VK.clicked.connect(self.input_vk)

    def openOtherWindow(self):
        global ex2
        ex2 = MyWidget2()
        ex.close()
        ex2.show()

    def add_files(self):
        global files_paths
        files_paths = QFileDialog.getOpenFileNames(self, '')[0]
        self.FileNames.setText(f"{', '.join([name.split('/')[-1] for name in files_paths])}")
        # self.FileNames.adjustSize()
        self.FileNames.setWordWrap(True)
        # self.FileNames.adjustSize()

    def post(self):
        try:
            if self.Telegram.isChecked():
                telegram_post(TELEGRAM_BOT_TOKEN, CHANEL_LOGIN, message=self.InputText.toPlainText(),
                    files_paths=files_paths)
            if self.Vkontakte.isChecked():
                vk_post(group_id_vk, message=self.InputText.toPlainText(), files_path=files_paths)
        except:
            print('функцию зщые проверь, дебил')

    def input_vk(self):
        pass

def telegram_post(TELEGRAM_BOT_TOKEN, CHANEL_LOGIN, message="", files_paths=None):
    bot = TeleBot(TELEGRAM_BOT_TOKEN)
    if files_paths:
        # проверка на количество файлов (должно быть не больше 10)
        if len(files_paths) > 10:
            return "too many files"

        medias = []
        for i, file in enumerate(files_paths):
            file_type = guess_type(file)[0].split("/")
            if file_type[1] == "gif":
                medias.append(types.InputMediaAnimation(open(file=file, mode="rb"), caption=message if i == 0 else ''))
            elif file_type[0] == "image":
                medias.append(types.InputMediaPhoto(open(file=file, mode="rb"), caption=message if i == 0 else ''))
            elif file_type[0] == "video":
                medias.append(types.InputMediaVideo(open(file=file, mode="rb"), caption=message if i == 0 else ''))
            elif file_type[0] == "audio":
                medias.append(types.InputMediaAudio(open(file=file, mode="rb"), caption=message if i == 0 else ''))
            else:
                medias.append(types.InputMediaDocument(open(file=file, mode="rb"), caption=message if i == 0 else ''))
        # проверка на разность типов файлов
        # вместе могут идти только фото и видео

        bot.send_media_group(chat_id=CHANEL_LOGIN, media=medias)
        return "success"
    elif message:
        bot.send_message(chat_id=CHANEL_LOGIN, text=message)
        return "success"
    else:
        return "no specs"


def vk_post(group_id_vk, message="", files_path=None):
    if files_paths:
        media = []
        upload = vk_api.VkUpload(vk_session)
        for file in files_paths:
            file_type = guess_type(file)[0].split("/")
            if file_type[0] == "image":
                photo = upload.photo(file, album_id="299120623", group_id=group_id_vk[1:])
                media.append('photo{}_{}'.format(photo[0]['owner_id'], photo[0]['id']))
            elif file_type[0] == "video":
                video = upload.photo(file, album_id="299120623", group_id=group_id_vk[1:])
                media.append('video{}_{}'.format(video[0]['owner_id'], video[0]['id']))
        vk_session.method('wall.post', {
            'owner_id': group_id_vk,
            'from_group': 1,
            'message': message,
            'attachments': ', '.join(media),
        })
    else:
        vk_session.method('wall.post', {
            'owner_id': group_id_vk,
            'from_group': 1,
            'message': message,
        })


class MyWidget2(QMainWindow, Ui_OtherWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Button_MenuReturn.clicked.connect(self.returnToMain)

    def returnToMain(self):
        ex2.close()
        ex.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()

    ex2 = MyWidget2()
    sys.exit(app.exec_())

# self.pixmap = QPixmap('VK Text Logo.jpg')
#        self.logo = QtWidgets.QLabel(OtherWindow)
#        self.logo.resize(260, 45)
#        self.logo.move(90, 30)
#        self.logo.setPixmap(self.pixmap)
# 90, 30, 351, 61
