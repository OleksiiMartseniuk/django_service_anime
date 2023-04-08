import logging
import requests
import time

from config.celery import app

from .service.service_vost import ServiceAnime
from .models import Anime, Series


logger = logging.getLogger('db')


@app.task
def parser(action: str) -> None:
    try:
        match action:
            case 'schedule':
                ServiceAnime().anime_schedule()
            case 'anons':
                ServiceAnime().anime_anons()
            case 'schedule_update':
                ServiceAnime().anime_schedule_update()
            case 'anons_update':
                ServiceAnime().anime_anons_update()
            case 'series':
                ServiceAnime().series()
            case 'series_update':
                ServiceAnime().series_update()
            case 'delete_series':
                ServiceAnime().delete_series()
            case 'update_indefinite_exit':
                ServiceAnime().update_indefinite_exit()
    except requests.exceptions.RequestException as exr:
        logger.error(f"{exr.__class__}")
    except Exception as ex:
        logger.error("Exception", exc_info=ex)


@app.task
def auto_update(auth: bool = True):
    """Авто обновления данных"""
    try:
        logger.info("Полное обновления данных запущено.")
        start_time = time.time()
        # Обновления расписания
        if Anime.objects.count():
            ServiceAnime().anime_schedule_update()
        else:
            logger.error('Не данных для обновления [schedule]')
        # Обновления анонсов
        if Anime.objects.filter(anons=True).count():
            ServiceAnime().anime_anons_update()
        else:
            logger.error('Не данных для обновления [anons]')

        # Обновления аниме с неопределенным сроком выхода
        ServiceAnime().update_indefinite_exit()

        # Обновления серий
        if Series.objects.count():
            ServiceAnime().series_update()
        else:
            logger.error('Не данных для обновления [series]')

        finish = time.time() - start_time
        logger.info(f"Полное обновления данных закончено. Время [{finish}]")
    except requests.exceptions.RequestException as exr:
        logger.error(f"{exr.__class__}")
    except Exception as ex:
        logger.error("Exception", exc_info=ex)
