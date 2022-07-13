import logging
from dataclasses import dataclass
from django.contrib import messages

from src.anime.tasks import parser

from . import messages as ex_massages


logger = logging.getLogger('main')


@dataclass
class Status:
    """Сообщения"""
    message: str
    level: int = messages.INFO


class ParserControl:
    """Контролер Parser"""
    def control(self, action: str) -> Status:
        match action:
            case 'schedule':
                parser.delay('schedule')
                status = Status(message=ex_massages.SCHEDULE)
            case 'anons':
                parser.delay('anons')
                status = Status(message=ex_massages.ANONS)
            case 'delete':
                parser.delay('delete')
                status = Status(message=ex_massages.DElETE)
            case 'schedule_update':
                parser.delay('schedule_update')
                status = Status(message=ex_massages.SCHEDULE_UPDATE)
            case 'anons_update':
                parser.delay('anons_update')
                status = Status(message=ex_massages.ANONS_UPDATE)
            case _:
                status = Status(
                    message=ex_massages.ERROR,
                    level=messages.ERROR
                )
        return status
