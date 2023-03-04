import logging

from django.contrib import messages

from src.anime.models import Anime, Series
from src.anime.tasks import parser, auto_update

from src.base.utils import Status
from src.base import messages as ex_massages

logger = logging.getLogger('main')


class ParserControl:
    """Контролер Parser"""

    def control(self, action: str) -> Status:
        match action:
            case 'schedule':
                is_valid = self._schedule_valid()
                if is_valid:
                    status = is_valid
                else:
                    parser.delay('schedule')
                    status = Status(message=ex_massages.SCHEDULE)
            case 'anons':
                is_valid = self._anons_valid()
                if is_valid:
                    status = is_valid
                else:
                    parser.delay('anons')
                    status = Status(message=ex_massages.ANONS)
            case 'schedule_update':
                is_valid = self._schedule_update_valid()
                if is_valid:
                    status = is_valid
                else:
                    parser.delay('schedule_update')
                    status = Status(message=ex_massages.SCHEDULE_UPDATE)
            case 'anons_update':
                is_valid = self._anons_update_valid()
                if is_valid:
                    status = is_valid
                else:
                    parser.delay('anons_update')
                    status = Status(message=ex_massages.ANONS_UPDATE)
            case 'series':
                is_valid = self._series_valid()
                if is_valid:
                    status = is_valid
                else:
                    parser.delay('series')
                    status = Status(message=ex_massages.SERIES)
            case 'series_update':
                is_valid = self._series_update_valid()
                if is_valid:
                    status = is_valid
                else:
                    parser.delay('series_update')
                    status = Status(message=ex_massages.SERIES_UPDATE)
            case 'delete_series':
                is_valid = self._delete_series_valid()
                if is_valid:
                    status = is_valid
                else:
                    parser.delay('delete_series')
                    status = Status(message=ex_massages.DElETE)
            case 'update_indefinite_exit':
                parser.delay('update_indefinite_exit')
                status = Status(message=ex_massages.UPDATE_INDEFINITE_EXIT)
            case 'write_telegram':
                is_valid = self._write_telegram_valid()
                if is_valid:
                    status = is_valid
                else:
                    parser.delay('write_telegram')
                    status = Status(
                        message=ex_massages.WRITE_TELEGRAM_BOT_FORM
                    )
            case 'full_update':
                auto_update.delay(False)
                status = Status(message=ex_massages.FULL_UPDATE)
            case _:
                status = Status(
                    message=ex_massages.ERROR,
                    level=messages.ERROR
                )
        return status

    def _schedule_valid(self) -> Status | None:
        if Anime.objects.filter(anons=False).count() >= 1:
            return Status(
                message=ex_massages.VALID_DATA_DONE_WRITE,
                level=messages.ERROR
            )

    def _anons_valid(self) -> Status | None:
        if Anime.objects.filter(anons=True).count() >= 1:
            return Status(
                message=ex_massages.VALID_DATA_DONE_WRITE,
                level=messages.ERROR
            )

    def _schedule_update_valid(self) -> Status | None:
        if not Anime.objects.count():
            return Status(
                message=ex_massages.VALID_DATA_UPDATE_NOT_EXISTS,
                level=messages.ERROR
            )

    def _anons_update_valid(self) -> Status | None:
        if not Anime.objects.filter(anons=True).count():
            return Status(
                message=ex_massages.VALID_DATA_UPDATE_NOT_EXISTS,
                level=messages.ERROR
            )

    def _series_valid(self) -> Status | None:
        if Series.objects.count() >= 1:
            return Status(
                message=ex_massages.VALID_DATA_DONE_WRITE,
                level=messages.ERROR
            )

    def _series_update_valid(self) -> Status | None:
        if not Series.objects.count():
            return Status(
                message=ex_massages.VALID_DATA_UPDATE_NOT_EXISTS,
                level=messages.ERROR
            )

    def _delete_series_valid(self) -> Status | None:
        if not Series.objects.count():
            return Status(
                message=ex_massages.VALID_DATA_DELETE_NOT_EXISTS,
                level=messages.ERROR
            )

    def _write_telegram_valid(self) -> Status | None:
        if not Anime.objects.filter(telegram_id_file=None).count():
            return Status(
                message=ex_massages.VALID_DATA_WRITE_EXISTS,
                level=messages.ERROR
            )
