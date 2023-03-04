import requests
import logging

from src.anime.models import Anime
from src.bot.models import BotSettings

from . import utils


logger = logging.getLogger('db')


class TelegramApiClient:
    """Клиент телеграм api"""
    def __init__(self):
        bot_settings = BotSettings.get_solo()
        if not bot_settings.is_token:
            logger.error("Token and chat_id for telegram not exists")
        self.chat_id = bot_settings.chat_id
        self.url = f"https://api.telegram.org/bot{bot_settings.token}/"

    def _post(self, url: str, params: dict, **kwargs) -> dict | None:
        response = requests.post(url, params=params, **kwargs)
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f'Неверный статус код {response.status_code} '
                         f'[{response.json()}]')

    def send_photo(self, path_img: str) -> dict | None:
        """Отправка фото на сервер телеграм"""
        url = self.url + 'sendPhoto'
        params = {'chat_id': self.chat_id}
        with open(path_img, 'rb') as fl:
            response = self._post(url, params=params, files={'photo': fl})
        return response

    def send_cart(self, chat_id: int, anime: Anime):
        """Отправить карточку с аниме"""
        url = self.url + 'sendPhoto'
        file_id = anime.telegram_id_file
        params = {
            'chat_id': chat_id,
            'photo': file_id if file_id else anime.url_image_preview,
            'caption': utils.get_cart(anime),
            'parse_mode': 'HTML'
        }
        return self._post(url, params=params)
