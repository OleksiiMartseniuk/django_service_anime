import re
import requests
import logging

from typing import List

from .setting import HEADERS
from .schemas import Anime, Series
from .exception import (
    ApiAnimeVostClientStatusCodeError,
    ApiAnimeVostClientAttributeError
)


logger = logging.getLogger('main')


class ApiAnimeVostClient:
    """
    Api клиент animevost
    """
    def __init__(self):
        self.url_v1 = 'https://api.animevost.org/v1'
        self.url_v2 = 'https://api.animevost.org/animevost/api/v0.2'
        self.base_url = 'https://animevost.org'

    def _get(self, url: str, params: dict = {}) -> dict | None:
        response = requests.get(url=url, params=params, headers=HEADERS)
        if response.status_code == 200:
            if not response.json().get('data'):
                logger.error(f'Неверный статус код {response.status_code} '
                             f'и нет данных на запрос "{url}"')
                raise ApiAnimeVostClientAttributeError
            return response.json()
        else:
            raise ApiAnimeVostClientStatusCodeError

    def _post(self, url: str, params: dict = {},
              data: dict = {}, data_list: bool = False) -> dict | None:
        response = requests.post(url=url, params=params, data=data)
        if response.status_code == 200:
            if data_list:
                return response.json()
            elif not response.json().get('data'):
                raise ApiAnimeVostClientAttributeError
            return response.json()
        elif response.status_code == 404:
            if response.json().get('error'):
                return response.json()
            else:
                logger.error(f'Неверный статус код {response.status_code} '
                             f'и нет данных на запрос "{url}"')
                raise ApiAnimeVostClientStatusCodeError
        else:
            raise ApiAnimeVostClientStatusCodeError

    def _create_anime_series(self, data: dict) -> Series:
        """Создания Series схемы"""
        return Series(
            name=data.get('name'),
            std=data.get('std'),
            hd=data.get('hd')
        )

    def _create_anime_schemas(self, data: dict) -> Anime:
        """ Создания Anime схемы """
        if re.search(r'^/', data.get('urlImagePreview')):
            url_image_preview = self.base_url + data.get('urlImagePreview')
        else:
            url_image_preview = data.get('urlImagePreview')

        screen_image = []

        for img in data.get('screenImage'):
            if re.search(r'^/', img):
                screen_image.append(self.base_url + img)
            elif not img:
                pass
            else:
                screen_image.append(img)

        anime = Anime(
            id=data.get('id'),
            title=data.get('title'),
            screen_image=screen_image,
            rating=data.get('rating'),
            votes=data.get('votes'),
            description=data.get('description'),
            director=data.get('director'),
            url_image_preview=url_image_preview,
            year=data.get('year'),
            genre=data.get('genre'),
            timer=data.get('timer'),
            type=data.get('type')
        )
        return anime

    def get_anime(self, id: int) -> None | Anime:
        """ Получения аниме по id"""
        url = self.url_v2 + '/GetInfo/' + str(id)
        data_json = self._get(url)
        data = data_json.get('data')
        return self._create_anime_schemas(data[0])

    def get_last_anime(self, page: int = 1, quantity: int = 10) -> List[Anime]:
        """ Получения последних обновленных аниме"""
        url = self.url_v2 + '/last'
        params = {'page': page, 'quantity': quantity}
        data_json = self._get(url, params=params)
        return list(map(self._create_anime_schemas, data_json['data']))

    def get_play_list(self, id: int) -> List[Series]:
        """Play list аниме по id"""
        url = self.url_v1 + '/playlist'
        data = {'id': id}
        data_json = self._post(url, data=data, data_list=True)
        return list(map(self._create_anime_series, data_json))

    def search(self, name: str) -> List[Anime] | dict:
        """ Поиск """
        url = self.url_v1 + '/search'
        data = {'name': name}
        data_json = self._post(url, data=data)
        if data_json.get('error'):
            return data_json
        return list(map(self._create_anime_schemas, data_json['data']))
