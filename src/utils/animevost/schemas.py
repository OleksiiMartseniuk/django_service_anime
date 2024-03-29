import re

from enum import Enum
from datetime import datetime
from dateutil.relativedelta import relativedelta

from pydantic import BaseModel


class Week(Enum):
    monday = 'raspisMon'
    tuesday = 'raspisTue'
    wednesday = 'raspisWed'
    thursday = 'raspisThu'
    friday = 'raspisFri'
    saturday = 'raspisSat'
    sunday = 'raspisSun'


class AnimeComposed(BaseModel):
    id_anime: int
    link: str


class AnimeMin(BaseModel):
    id_anime: int
    link: str
    anime_composed: list[AnimeComposed] | None


class Anime(BaseModel):
    id: int
    title_ru: str
    title_en: str
    screen_image: list[str]
    rating: int
    votes: int
    description: str
    director: str
    url_image_preview: str
    year: str
    genres: list
    timer: int
    type: str
    anons: bool
    anons_date: None | datetime
    day: int | None


class Series(BaseModel):
    name: str
    serial_number: str
    number: int | None


class AnimeData(Anime):
    link: str


class AnimeFull(AnimeData):
    anime_composed: list[AnimeData]


def create_anime_series(data: dict) -> Series:
    serial = data.get('hd') or data.get('std', '')
    name = data.get('name')
    number = re.search(r'^\d*', name).group()
    if number.strip().isnumeric():
        number = int(number)
    else:
        number = None

    return Series(
        name=name,
        serial_number=serial.split('/')[-1].split('.')[0],
        number=number,
    )


def create_anime_schemas(base_url: str, data: dict) -> Anime:
    if re.search(r'^/', data.get('urlImagePreview')):
        url_image_preview = base_url + data.get('urlImagePreview')
    else:
        url_image_preview = data.get('urlImagePreview')

    screen_image = []
    for img in data.get('screenImage'):
        if re.search(r'^/', img):
            screen_image.append(base_url + img)
        elif not img:
            pass
        else:
            screen_image.append(img)

    remove_list = ['\n', '\r', '<br>', '<br />']
    description = data.get('description', '')
    for sub in remove_list:
        description = description.replace(sub, '')

    genres = []
    for genre in re.split(r', |\. ', data.get('genre', '')):
        genres.append(genre.lower().strip())

    anons = False
    anons_date = None
    if re.search(r'Анонс', data.get('title', '')):
        anons = True
        data_str = data.get('title', '').split("Анонс")[-1]
        result = re.search("\s\d+", data_str)
        try:
            numbers = int(result.group(0))
        except ValueError:
            pass
        else:
            now = datetime.now()
            if now.day > numbers:
                new = now + relativedelta(months=1)
                anons_date = new.replace(day=numbers)
            else:
                anons_date = now.replace(day=numbers)

    titles = data.get('title', '').split('/')
    title_ru, title_en = '', ''
    if len(titles) > 1:
        title_ru = titles[0].strip()
        tow_part = titles[1].split('[')
        if len(tow_part) > 1:
            title_en = tow_part[0].strip()
        else:
            title_en = titles[1].strip()

    timer = data.get('timer')
    day = None
    if timer and timer != '0':
        day = datetime.utcfromtimestamp(int(timer)).weekday()

    return Anime(
        id=data.get('id'),
        title_ru=title_ru,
        title_en=title_en,
        screen_image=screen_image,
        rating=data.get('rating'),
        votes=data.get('votes'),
        description=description,
        director=data.get('director'),
        url_image_preview=url_image_preview,
        year=data.get('year'),
        genres=genres,
        timer=data.get('timer'),
        type=data.get('type'),
        anons=anons,
        day=day,
        anons_date=anons_date,
    )
