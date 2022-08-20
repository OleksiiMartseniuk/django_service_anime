import requests
import logging

from django.conf import settings


logger = logging.getLogger('main')


class TelegramApiClient:
    """Клиент телеграм api"""
    def __init__(self):
        self.url = settings.API_TELEGRAM
        self.chat_id = settings.BOT_CHAT_ID

    def _post(self, url: str, params: dict, **kwargs) -> dict | None:
        response = requests.post(url, params=params, **kwargs)
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f'Неверный статус код {response.status_code} '
                         f'url-"{url}"')

    def send_photo(self, path_img: str) -> dict | None:
        """Отправка фото на сервер телеграм"""
        url = self.url + 'sendPhoto'
        params = {'chat_id': self.chat_id}
        with open(path_img, 'rb') as fl:
            response = self._post(url, params=params, files={'photo': fl})
        return response
