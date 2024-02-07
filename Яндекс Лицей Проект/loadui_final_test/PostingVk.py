from mimetypes import guess_type
import vk_api
import json

group_id = '-223288989'
files_paths = []

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
