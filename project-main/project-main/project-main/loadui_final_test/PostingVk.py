import vk_api
import json
from mimetypes import guess_type


def vk_post(access_token, group_id_vk, message="", files_paths=None):
    try:
        # из-за .auth() возникала ошибка. закоментировал 9-10 строку, так как без них приложение работает корректно
        # vk = vk_api.VkApi(login, password, app_id=2685278)
        # vk.auth()
        # access_token =
        # with open('vk_config.v2.json', 'r') as data_file:
        #     data = json.load(data_file)
        #
        # for xxx in data[login]['token'].keys():
        #     for yyy in data[login]['token'][xxx].keys():
        #         access_token = data[login]['token'][xxx][yyy]['access_token']

        vk_session = vk_api.VkApi(token=access_token)
        vk_session_api = vk_session.get_api()

    except vk_api.AuthError:
        return "Ошибка аутентификации в ВК"

    try:
        # получаю id первого альбома сообщества
        album_id = vk_session_api.photos.getAlbums(owner_id=group_id_vk, access_token=access_token)['items'][0]['id']
    except:
        return 'Ошибка получения id альбома'

    if files_paths:
        # проверка на количество файлов (должно быть не больше 10)
        if len(files_paths) > 10:
            return "Добавлено слишком много файлов"

        # загрузка файлов в ВК
        upload = vk_api.VkUpload(vk_session)
        medias = []
        for file in files_paths:
            try:
                file_type = guess_type(file)[0].split("/")
                if file_type[0] == "image":
                    photo = upload.photo(file, album_id=album_id, group_id=group_id_vk[1:])
                    medias.append('photo{}_{}'.format(photo[0]['owner_id'], photo[0]['id']))
                elif file_type[0] == "video":
                    video = upload.video(file, group_id=group_id_vk[1:])
                    medias.append('video{}_{}'.format(video['owner_id'], video['video_id']))
                else:
                    return "Недопустимый тип файла"
            except AttributeError:
                return "Недопустимый тип файла"

        # размещения поста с всеми файлами
        vk_session_api.wall.post(owner_id=group_id_vk, from_group=1, message=message, attachments=', '.join(medias))
        return "Успешно размещено в ВК"
    elif message:
        vk_session_api.wall.post(owner_id=group_id_vk, from_group=1, message=message)
        return "Успешно размещено в ВК"
    else:
        return "Не указано никаких данных"

