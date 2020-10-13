class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        import requests
        import os
        name = os.path.basename(file_path)
        response_url = requests.get(
            "https://cloud-api.yandex.net/v1/disk/resources/upload",
            params={'path': name, 'overwrite': True},
            headers={"Authorization": f"OAuth {self.token}"},
        )
        url = response_url.json()['href']

        with open(file_path, 'rb') as f:
            my_file = f.read()
            response = requests.put(url, data=my_file, headers={'content-type': 'picture'}, params={'file': name})
        return 'Файл успешно загружен'

if __name__ == '__main__':
    token = input('Введите токен Яндекс Диска: ')
    directory = input('Введите путь к файлу, который необходимо загрузить: ')
    uploader = YaUploader(token)
    result = uploader.upload(fr'{directory}')
    print(result)
