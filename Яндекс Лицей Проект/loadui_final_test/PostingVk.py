import vk_api
import json

group_id = '-223288989'

login = '79966980274'
password = 'KtoBilol07('

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

upload = vk_api.VkUpload(vk_session)
photo = upload.photo('1.png', album_id="299120623", group_id="223288989")
vk_photo_url = 'photo{}_{}'.format(photo[0]['owner_id'], photo[0]['id'])
rs = vk_session.method('wall.post', {
    'owner_id': group_id,
    'from_group': 1,
    'message': '1',
    'attachments': vk_photo_url,
})
