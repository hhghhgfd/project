from telebot import TeleBot, types
from mimetypes import guess_type


def telegram_post(telegram_bot_token, channel_login, message="", files_paths=None):
    bot = TeleBot(telegram_bot_token)
    if files_paths:
        # проверка на количество файлов (должно быть не больше 10)
        if len(files_paths) > 10:
            return "too many files"

        medias = []
        for file in files_paths:
            print(file)
            file_type = guess_type(file)[0].split("/")

            print(file_type)
            if file_type[1] == "gif":
                medias.append(types.InputMediaAnimation(open(file=file, mode="rb"), caption=message))
            elif file_type[0] == "image":
                medias.append(types.InputMediaPhoto(open(file=file, mode="rb"), caption=message))
            elif file_type[0] == "video":
                medias.append(types.InputMediaVideo(open(file=file, mode="rb"), caption=message))
            elif file_type[0] == "audio":
                medias.append(types.InputMediaAudio(open(file=file, mode="rb"), caption=message))
            else:
                medias.append(types.InputMediaDocument(open(file=file, mode="rb"), caption=message))
        print(medias)

        # проверка на разность типов файлов
        # вместе могут идти только фото и видео

        bot.send_media_group(chat_id=channel_login, media=medias)
        return "success"
    elif message:
        bot.send_message(chat_id=channel_login, text=message)
        return "success"
    else:
        return "no specs"


print(telegram_post("5833708631:AAH3otkx2PXvhsGLXdxqyuv-Pr6IsAtioXc", "@boxofpitsa",
                    files_paths=["C:/Users/User/Downloads/Qt Designer Setup.exe"],
                    message="text"))

'''        if (types.InputMediaPhoto or types.InputMediaVideo) and types.InputMediaAudio in [type(media)
                                                                                          for media in medias]:
            return "can't mix photo/video content and audios"
        elif types.InputMediaPhoto in [type(media) for media in medias] or types.InputMediaVideo in [type(media) for media in medias]:
            return "can't mix photo/video content and documents"
'''

telegram_bot_token = '5833708631:AAH3otkx2PXvhsGLXdxqyuv-Pr6IsAtioXc'
channel_login = '@boxofpitsa'

# print(telegram_post("6688896910:AAGBTRUp8b0ZKTZot6k2ddNCvxaR359fB4o", "@aaaaaaaaaaaaaa1231231",
#                     files_paths=["D:/Downloads/fnaf-springtrap.gif", "D:/Downloads/fnaf-springtrap.gif"],
#                     message="text"))
