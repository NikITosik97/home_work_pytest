from TOKEN import TOKEN
import requests


class CreateFolderYandexDisc:
    def __init__(self):
        self.token = TOKEN
        self.url = f'https://cloud-api.yandex.net/v1/disk/resources'

    def create_folder(self):
        headers = {'Authorization': self.token}

        params = {'path': 'TestFolder'}

        response = requests.put(url=self.url, params=params, headers=headers)

        return response
