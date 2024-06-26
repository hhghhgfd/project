from telebot import TeleBot, types
from mimetypes import guess_type


def telegram_post(channel_login, telegram_bot_token='7167304130:AAEED0jnNdIIbEqdYyQL3vGvFsdMt2O5P94',
                  message="", files_paths=None):
    bot = TeleBot(telegram_bot_token)
    if files_paths:
        # проверка на количество файлов (должно быть не больше 10)
        if len(files_paths) > 10:
            return 0, "Добавлено слишком много файлов"

        # обработка файлов в зависимости от типа данных
        medias = []
        for file in files_paths:
            try:
                file_type = guess_type(file)[0].split("/")
            except AttributeError:  # guess_type некорректно обрабатывает архивы, поэтому для них сделано исключение
                file_type = [1, 1]

            # добавляем типы файлов в медиа группу
            if file_type[0] == "image":
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
            return 0, "Нельзя совмещать фото и документы"
        if "photo" in set(media_types) and "audio" in set(media_types):
            return 0, "Нельзя совмещать фото и аудио"
        if "video" in set(media_types) and "document" in set(media_types):
            return 0, "Нельзя совмещать видео и документы"
        if "video" in set(media_types) and "audio" in set(media_types):
            return 0, "Нельзя совмещать видео и аудио"
        if "document" in set(media_types) and "audio" in set(media_types):
            return 0, "Нельзя совмещать документы и аудио"

        try:
            # пост медиа группы в канал
            bot.send_media_group(chat_id=channel_login, media=medias)
            return 1, "Успешно размещено в Телеграм"
        except:
            return 0, "Ошибка размещения поста в Телеграм"
    elif message:
        try:
            # пост текста в канал
            bot.send_message(chat_id=channel_login, text=message)
            return 1, "Успешно размещено в Телеграм"
        except:
            return 0, "Ошибка размещения поста в Телеграм"
    else:
        return 0, "Не указано никаких данных"
