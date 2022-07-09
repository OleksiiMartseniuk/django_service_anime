import logging
from dataclasses import dataclass
from django.contrib import messages

from src.base.animevost import exception

from ..service import ServiceAnime
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
        try:
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
                case 'schedule_update':
                    ServiceAnime().anime_schedule_update()
                    status = Status(message=ex_massages.SCHEDULE_UPDATE)
                case 'anons_update':
                    ServiceAnime().anime_anons_update()
                    status = Status(message=ex_massages.ANONS_UPDATE)
                case _:
                    status = Status(
                        message=ex_massages.ERROR,
                        level=messages.ERROR
                    )
        except exception.ParserClientStatusCodeError:
            status = Status(
                message=ex_massages.ERROR_STATUS_CODE_PARSE,
                level=messages.ERROR
            )
        except exception.ApiAnimeVostClientStatusCodeError:
            status = Status(
                message=ex_massages.ERROR_STATUS_CODE_API,
                level=messages.ERROR
            )
        except exception.ApiAnimeVostClientAttributeError:
            status = Status(
                message=ex_massages.ERROR_DATA_API,
                level=messages.ERROR
            )
        except exception.NotDataError:
            status = Status(
                message=ex_massages.ERROR_NOT_DATA,
                level=messages.ERROR
            )
        except Exception as ex:
            status = Status(
                message=ex_massages.ERROR,
                level=messages.ERROR
            )
            logger.error(str(ex))
        return status
