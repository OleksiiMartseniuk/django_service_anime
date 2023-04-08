import re

from enum import Enum

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
    title: str
    screen_image: list[str]
    rating: int
    votes: int
    description: str
    director: str
    url_image_preview: str
    year: str
    genre: str
    timer: int
    type: str


class Series(BaseModel):
    name: str
    serial: str
    preview: str


class AnimeData(Anime):
    link: str


class AnimeFull(AnimeData):
    anime_composed: list[AnimeData]


def create_anime_series(data: dict) -> Series:
    serial = data.get('hd') or data.get('std', '')
    return Series(
        name=data.get('name'),
        serial=serial.split('/')[-1].split('.')[0],
        preview=data.get('preview')
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

    return Anime(
        id=data.get('id'),
        title=data.get('title'),
        screen_image=screen_image,
        rating=data.get('rating'),
        votes=data.get('votes'),
        description=description,
        director=data.get('director'),
        url_image_preview=url_image_preview,
        year=data.get('year'),
        genre=data.get('genre'),
        timer=data.get('timer'),
        type=data.get('type')
    )
