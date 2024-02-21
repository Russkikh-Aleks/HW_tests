import requests


class YaUploader:
    """Класс для создания папки на на Яндекс Диск"""

    base_url = "https://cloud-api.yandex.net/v1/disk"

    def __init__(self, token: str):
        self.token = token
        self.header = {"Authorization": self.token}

    def create_folder(self, folder_name: str) -> int:
        """Метод создает папку на Яндекс Диск, если ее еще там нет."""

        params = {"path": folder_name}
        response = requests.put(
            f"{self.base_url}/resources", headers=self.header, params=params)

        return response
    
    def get_dir_inform(self) -> list:
        """ Метод получает информацию о файлах и папках, находящихся в переданной папке на яндекс диске"""

        params = {"path": f"disk:/",
                  "fields": 'items'}
        response = requests.get(f"{self.base_url}/resources",
                                headers=self.header, params=params).json()
        return [el['name'] for el in response["_embedded"]["items"]]
        
