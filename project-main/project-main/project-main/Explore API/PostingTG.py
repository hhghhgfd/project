from telebot import TeleBot, types
from mimetypes import guess_type


def telegram_post(telegram_bot_token, channel_login, message="", files_paths=None):
    bot = TeleBot(telegram_bot_token)
    if files_paths:
        # проверка на количество файлов (должно быть не больше 10)
        if len(files_paths) > 10:
            return "too many files"

        # обработка файлов в зависимости от типа данных
        medias = []
        for file in files_paths:
            file_type = guess_type(file)[0].split("/")

            # гифки отправляются только по одной, поэтому с ними работаем отдельно
            if file_type[1] == "gif":
                if len(files_paths) > 1:
                    return "there can only be one gif"
                bot.send_animation(chat_id=channel_login, animation=open(file=file, mode="rb"), caption=message)
                return "successfully posted"

            # добавляем другие типы файлов в медиа группу
            elif file_type[0] == "image":
                medias.append(types.InputMediaPhoto(open(file=file, mode="rb")))
            elif file_type[0] == "video":
                medias.append(types.InputMediaVideo(open(file=file, mode="rb")))
            elif file_type[0] == "audio":
                medias.append(types.InputMediaAudio(open(file=file, mode="rb")))
            else:
                medias.append(types.InputMediaDocument(open(file=file, mode="rb")))

        # добавляем к первому файлу текст
        medias[0].caption = message

        # проверка на разность типов файлов
        # вместе могут идти только фото и видео
        media_types = list()
        for media in medias:
            media_types.append(media.type)
        if "photo" in set(media_types) and "document" in set(media_types):
            return "can't mix photos and documents"
        if "photo" in set(media_types) and "audio" in set(media_types):
            return "can't mix photos and audios"
        if "video" in set(media_types) and "document" in set(media_types):
            return "can't mix videos and documents"
        if "video" in set(media_types) and "audio" in set(media_types):
            return "can't mix videos and audios"
        if "document" in set(media_types) and "audio" in set(media_types):
            return "can't mix documents and audios"

        # пост медиа группы в канал
        bot.send_media_group(chat_id=channel_login, media=medias)
        return "successfully posted"
    elif message:
        # пост текста в канал
        bot.send_message(chat_id=channel_login, text=message)
        return "successfully posted"
    else:
        return "no specs"


# print(telegram_post("your_bot_token", "@channel_name", files_paths=[], message=""))
