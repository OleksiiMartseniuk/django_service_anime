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
