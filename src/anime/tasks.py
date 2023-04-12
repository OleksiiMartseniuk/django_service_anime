import logging
import time

from config.celery import app

from .service.service_vost import ServiceAnime
from .models import Anime, Series


logger = logging.getLogger('db')


@app.task
def parser(action: str) -> None:
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
        case 'update_indefinite_exit':
            ServiceAnime().update_indefinite_exit()


@app.task
def auto_update(auth: bool = True):
    """Авто обновления данных"""
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
