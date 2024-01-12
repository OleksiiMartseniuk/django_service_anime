from typing import Any

from pydantic import BaseModel


class Names(BaseModel):
    ru: str
    en: str
    alternative: Any | None


class Franchise(BaseModel):
    id: str
    name: str


class Releases(BaseModel):
    id: int | None
    code: str | None
    ordinal: int | None
    namas: Names | None


class Status(BaseModel):
    string: str
    code: int


class Poster(BaseModel):
    url: str
    raw_base64_file: Any | None


class Posters(BaseModel):
    small: Poster
    medium: Poster
    original: Poster


class TypeTitle(BaseModel):
    full_string: str
    code: int
    string: str
    series: int | None
    length: int | None


class Team(BaseModel):
    voice: list[str | None]
    translator: list[str | None]
    editing: list[str | None]
    decor: list[str | None]
    timing: list[str | None]


class Season(BaseModel):
    string: str
    code: int
    year: int
    week_day: int


class Blocked(BaseModel):
    blocked: bool
    bakanim: bool


class HLS(BaseModel):
    fhd: str
    hd: str
    sd: str


class Skips(BaseModel):
    opening: list[Any | None]
    ending: list[Any | None]


class Episodes(BaseModel):
    first: int | None
    last: int | None
    string: str | None


class Episode(BaseModel):
    episode: int
    name: str | None
    uuid: str
    created_timestamp: str
    preview: str | None
    skips: Skips
    hls: HLS


class Player(BaseModel):
    alternative_player: str | None
    host: str
    episodes: Episodes
    list: dict[str, Episode]


class Title(BaseModel):
    id: int
    code: str
    names: Names
    franchises: Releases
    announce: str | None
    status: Status
    posters: Posters
    updated: int
    last_change: int
    type: TypeTitle
    genres: list[str]
    team: Team
    season: Season
    description: str
    in_favorites: int
    blocked: Blocked
    player: Player
