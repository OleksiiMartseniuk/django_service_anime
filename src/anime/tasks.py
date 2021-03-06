import logging

from config.celery import app

from .service.service_vost import ServiceAnime
from .models import Anime, Series, Statistics


logger = logging.getLogger('main')


@app.task
def parser(action: str) -> None:
    match action:
        case 'schedule':
            ServiceAnime().anime_schedule()
        case 'anons':
            ServiceAnime().anime_anons()
        case 'delete':
            ServiceAnime().delete_table()
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


@app.task
def auto_update():
    """Авто обновления данных"""
    # Обновления расписания
    if Anime.objects.count():
        ServiceAnime().anime_schedule_update()
        logger.info('Обновления успешно [schedule]')
    else:
        logger.error('Не данных для обновления [schedule]')
    # Обновления анонсов
    if Anime.objects.filter(anons=True).count():
        ServiceAnime().anime_anons_update()
        logger.info('Обновления успешно [anons]')
    else:
        logger.error('Не данных для обновления [anons]')
    # Обновления серий
    if Series.objects.count():
        ServiceAnime().series_update()
        logger.info('Обновления успешно [series]')
    else:
        logger.error('Не данных для обновления [series]')

    # Запись в статистику
    Statistics.objects.create(message='Авто обновления выполнено')
