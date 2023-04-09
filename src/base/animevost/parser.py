import logging
import requests
import re

from bs4 import BeautifulSoup

from .setting import HEADERS
from .schemas import Week, AnimeMin, AnimeComposed
from .exception import AnimeVostStatusCodeError


logger = logging.getLogger('anime_vost')


class ParserClient:

    def __init__(self) -> None:
        self.url = 'https://animevost.org'

    def _get(self, url) -> str | None:
        response = requests.get(url=url, headers=HEADERS)
        if response.status_code == 200:
            return response.text
        else:
            logger.error(
                'Status code %s request %s',
                response.status_code, url
            )
            raise AnimeVostStatusCodeError

    def get_composed(self, link: str, id: str) -> list[AnimeComposed | None]:
        """Get list anime composed"""
        text_page = self._get(link)

        soup = BeautifulSoup(text_page, 'lxml')
        try:
            anime_composed = []
            list_li = soup.find('div', class_='text_spoiler').find_all('li')
            for li in list_li:
                id_anime = re.search(
                    r'[/]\d+[-]',
                    li.a.get('href')
                ).group()[1:-1]
                if id_anime != id:
                    anime_composed.append(
                        AnimeComposed(
                            id_anime=id_anime,
                            link=self.url + li.a.get('href')
                        )
                    )
        except AttributeError:
            anime_composed = []

        return anime_composed

    def get_schedule(
            self,
            full: bool = False
    ) -> dict[str, list[AnimeMin] | None]:
        text_page = self._get(self.url)
        soup = BeautifulSoup(text_page, 'lxml')
        anime_week = {}
        for day in Week:

            try:
                link_list = soup.find(id=day.value).find_all('a')
            except AttributeError:
                logger.error('Not found link anime.')
                continue

            list_anime = []

            for link in link_list:
                try:
                    id_anime = re.search(
                        r'[/]\d+[-]',
                        link.get('href')
                    ).group()[1:-1]
                except AttributeError:
                    logger.warning(
                        'Not found link-[%s] day-%s',
                        link.text, day.name
                    )
                    id_anime = None

                if full and id_anime:
                    anime_composed = self.get_composed(
                        self.url + link.get('href'),
                        id_anime
                    )
                else:
                    anime_composed = None
                if id_anime:
                    list_anime.append(
                        AnimeMin(
                            id_anime=id_anime,
                            link=self.url + link.get('href'),
                            anime_composed=anime_composed
                        )
                    )
            anime_week[day.name] = list_anime
        return anime_week

    def _get_count_page(self) -> int:
        data = self._get(self.url + '/preview/')
        soup = BeautifulSoup(data, 'lxml')
        try:
            count_page = soup.find(class_='block_4').find_all('a')[-1].text
            count_page = int(count_page)
        except ValueError:
            count_page = 1
        except AttributeError:
            count_page = 1
        return count_page

    def get_anons(self, full: bool = False) -> list[AnimeMin] | None:
        list_anime = []
        for page in range(1, self._get_count_page() + 1):
            page_html = self._get(self.url + '/preview/' + f'page/{page}/')
            soup = BeautifulSoup(page_html, 'lxml')
            try:
                for div in soup.find_all(class_='shortstoryHead'):
                    id_anime = re.search(
                        r'[/]\d+[-]',
                        div.a.get('href')
                    ).group()[1:-1]
                    if full:
                        anime_composed = self.get_composed(
                            div.a.get('href'),
                            id_anime
                        )
                    else:
                        anime_composed = None
                    list_anime.append(
                        AnimeMin(
                            id_anime=id_anime,
                            link=div.a.get('href'),
                            anime_composed=anime_composed
                        )
                    )
            except AttributeError:
                logger.warning('Not found anons page [%s]', page)
                continue
        return list_anime

    def get_anime_one(self, id: int, link: str) -> AnimeMin:
        anime_composed = self.get_composed(link, str(id))
        return AnimeMin(id_anime=id, link=link, anime_composed=anime_composed)
