from dataclasses import dataclass
from django.contrib import messages

from ..service import ServiceAnime
from . import messages as ex_massages


@dataclass
class Status:
    """Сообщения"""
    message: str
    level: messages = messages.INFO


class ParserControl:
    """Контролер Parser"""
    def control(self, action: str) -> Status:
        match action:
            case 'schedule':
                ServiceAnime().anime_schedule()
                status = Status(message=ex_massages.SCHEDULE)
            case 'anons':
                ServiceAnime().anime_anons()
                status = Status(message=ex_massages.ANONS)
            case 'delete':
                ServiceAnime().delete_table()
                status = Status(message=ex_massages.DElETE)
            case _:
                status = Status(
                    message=ex_massages.ERROR,
                    level=messages.ERROR
                )
        return status
