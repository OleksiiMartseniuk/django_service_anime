from typing import Any

from pydantic import BaseModel


class Names(BaseModel):
    ru: str
    en: str
    alternative: Any | None


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
    series: int
    length: int


class Season(BaseModel):
    string: str
    code: int
    year: int
    week_day: int


class Team(BaseModel):
    voice: list[str | None]
    translator: list[str | None]
    editing: list[str | None]
    decor: list[str | None]
    timing: list[str | None]


class Blocked(BaseModel):
    blocked: bool
    bakanim: bool


class Series(BaseModel):
    first: int
    last: int
    string: str


class Skips(BaseModel):
    opening: list[Any | None]
    ending: list[Any | None]


class HLS(BaseModel):
    fhd: str
    hd: str
    sd: str


class Serie(BaseModel):
    serie: int
    created_timestamp: int
    preview: Any | None
    skips: Skips
    hls: HLS


class Player(BaseModel):
    alternative_player: str
    host: str
    series: Series
    playlist: dict[str, Serie]


class Title(BaseModel):
    id: int
    code: str
    names: Names
    announce: str
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


class Schedule(BaseModel):
    day: int
    list: list[Title]


class ScheduleList(BaseModel):
    schedule: list[Schedule]
