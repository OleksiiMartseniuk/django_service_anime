import logging
from dataclasses import dataclass
from django.contrib import messages

from src.anime.tasks import parser
from src.anime.service.utils import delete_img_files

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
            case 'delete_img':
                delete_img_files()
                status = Status(message=ex_massages.DElETE)
            case 'schedule_update':
                parser.delay('schedule_update')
                status = Status(message=ex_massages.SCHEDULE_UPDATE)
            case 'anons_update':
                parser.delay('anons_update')
                status = Status(message=ex_massages.ANONS_UPDATE)
            case 'series':
                parser.delay('series')
                status = Status(message=ex_massages.SERIES)
            case 'series_update':
                parser.delay('series_update')
                status = Status(message=ex_massages.SERIES_UPDATE)
            case 'delete_series':
                parser.delay('delete_series')
                status = Status(message=ex_massages.DElETE)
            case 'update_indefinite_exit':
                parser.delay('update_indefinite_exit')
                status = Status(message=ex_massages.UPDATE_INDEFINITE_EXIT)
            case _:
                status = Status(
                    message=ex_massages.ERROR,
                    level=messages.ERROR
                )
        return status
