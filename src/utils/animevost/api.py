import requests
import json

from .schemas import (
    Anime,
    Series,
    create_anime_series,
    create_anime_schemas,
)
from .exception import AnimeVostDataError, AnimeVostStatusCodeError


class ApiAnimeVostClient:

    def __init__(self):
        self.url_v1 = 'https://api.animevost.org/v1'
        self.url_v2 = 'https://api.animevost.org/animevost/api/v0.2'
        self.base_url = 'https://animevost.org'

    def _get(self, url: str, **kwargs) -> dict:
        response = requests.get(url=url, **kwargs)
        if response.status_code == 200:
            if not response.json().get('data'):
                raise AnimeVostDataError(
                    f"Request {url} kwargs[{json.dumps(kwargs)}]"
                )
            return response.json()
        else:
            raise AnimeVostStatusCodeError(
                f"Request {url} status code [{response.status_code}] "
                f"kwargs[{json.dumps(kwargs)}]"
            )

    def _post(self, url: str, **kwargs) -> dict:
        response = requests.post(url=url, **kwargs)
        if response.status_code == 200:
            return response.json()
        else:
            raise AnimeVostStatusCodeError(
                f"Request {url} status code [{response.status_code}] "
                f"kwargs[{json.dumps(kwargs)}]"
            )

    def get_anime(self, anime_id: int) -> None | Anime:
        url = f'{self.url_v2}/GetInfo/{anime_id}'
        data_json = self._get(url)
        data = data_json.get('data')
        return create_anime_schemas(self.base_url, data[0])

    def get_last_anime(
        self,
        page: int = 1,
        quantity: int = 30
    ) -> list[Anime]:
        """Get last update anime"""
        url = f'{self.url_v2}/last'
        params = {'page': page, 'quantity': quantity}
        data_json = self._get(url, params=params)
        return list(
            map(
                create_anime_schemas,
                [self.base_url for _ in range(len(data_json['data']))],
                data_json['data']
            )
        )

    def get_play_list(self, id: int) -> list[Series]:
        url = f'{self.url_v1}/playlist'
        data = {'id': id}
        data_json = self._post(url, data=data)
        if isinstance(data_json, dict) and data_json.get('error'):
            raise AnimeVostDataError(f'Play list not data for anime_id {id}')
        return list(map(create_anime_series, data_json))

    def search(self, name: str) -> list[Anime]:
        url = f'{self.url_v1}/search'
        data = {'name': name}
        data_json = self._post(url, data=data)
        return list(
            map(
                create_anime_schemas,
                [self.base_url for _ in range(len(data_json['data']))],
                data_json['data']
            )
        )
