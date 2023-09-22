import logging
import requests
import re
from collections import defaultdict

from bs4 import BeautifulSoup

from .schemas import Week, AnimeMin, AnimeComposed
from .exception import AnimeVostStatusCodeError


class ParserClient:

    def __init__(
        self,
        logger: logging.Logger = logging.getLogger(__name__),
    ) -> None:
        self.url = 'https://animevost.org'
        self.logger = logger

    def _get(self, url: str) -> str:
        response = requests.get(url=url)
        if response.status_code == 200:
            return response.text
        else:
            raise AnimeVostStatusCodeError(
                f"Request {url} status code [{response.status_code}] "
            )

    def get_composed(self, link: str, id: str) -> list[AnimeComposed] | None:
        """Get list anime composed"""
        try:
            text_page = self._get(link)
        except Exception as ex:
            self.logger.error(f"Page {link} error anime_id[{id}]", exc_info=ex)
            return None
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
                            link=f'{self.url}{li.a.get("href")}',
                        )
                    )
        except AttributeError:
            anime_composed = None
        return anime_composed

    def get_schedule(self) -> defaultdict[list]:
        text_page = self._get(self.url)
        soup = BeautifulSoup(text_page, 'lxml')
        anime_week = defaultdict(list)
        for day in Week:
            try:
                link_list = soup.find(id=day.value).find_all('a')
            except AttributeError:
                self.logger.error(f'Not found link anime for day[{day.name}]')
                continue
            for link in link_list:
                try:
                    id_anime = re.search(
                        r'[/]\d+[-]',
                        link.get('href')
                    ).group()[1:-1]
                except AttributeError:
                    self.logger.warning(
                        f'Not found link-[{link.text}] day-{day.name}',
                    )
                    id_anime = None

                if id_anime:
                    anime_composed = self.get_composed(
                        f'{self.url}{link.get("href")}',
                        id_anime
                    )
                else:
                    anime_composed = None
                if id_anime:
                    anime_week[day.name].append(
                        AnimeMin(
                            id_anime=id_anime,
                            link=f'{self.url}{link.get("href")}',
                            anime_composed=anime_composed
                        )
                    )
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

    def get_anons(self) -> list[AnimeMin | None]:
        list_anime = []
        for page in range(1, self._get_count_page() + 1):
            url = f'{self.url}/preview/page/{page}/'
            try:
                page_html = self._get(url)
            except Exception as ex:
                self.logger.error(f'Page for anons {url}', exc_info=ex)
                continue

            soup = BeautifulSoup(page_html, 'lxml')
            try:
                for div in soup.find_all(class_='shortstoryHead'):
                    id_anime = re.search(
                        r'[/]\d+[-]',
                        div.a.get('href')
                    ).group()[1:-1]
                    if id_anime:
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
                self.logger.warning(f'Not found anons page [{page}]',)
                continue
        return list_anime
