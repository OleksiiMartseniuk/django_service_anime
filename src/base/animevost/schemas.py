from enum import Enum
from typing import List

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
    anime_composed: List[AnimeComposed] | None


class Anime(BaseModel):
    id: int
    title: str
    screen_image: List[str]
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
    std: str
    hd: str


class AnimeData(Anime):
    link: str


class AnimeFull(AnimeData):
    anime_composed: List[AnimeData]
