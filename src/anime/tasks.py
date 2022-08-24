import logging
import requests

from config.celery import app

from .service.service_vost import ServiceAnime
from .service import service
from .models import Anime, Series, Statistics


logger = logging.getLogger('main')


@app.task
def parser(action: str) -> None:
    try:
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
            case 'update_indefinite_exit':
                ServiceAnime().update_indefinite_exit()
            case 'write_telegram':
                service.write_images_telegram()

    except requests.exceptions.RequestException as exr:
        logger.error(exr)
        Statistics.objects.create(message=f'Произошла ошибка #{exr.__class__}')
    except Exception as ex:
        logger.error(ex)
        Statistics.objects.create(message=f'Произошла ошибка #{ex.__class__}')


@app.task
def auto_update():
    """Авто обновления данных"""
    try:
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

        # Обновления аниме с неопределенным сроком выхода
        ServiceAnime().update_indefinite_exit()
        # Запись картинок на сервер telegram
        service.write_images_telegram()

        # Обновления серий
        if Series.objects.count():
            ServiceAnime().series_update()
            logger.info('Обновления успешно [series]')
        else:
            logger.error('Не данных для обновления [series]')

        # Запись в статистику
        Statistics.objects.create(message='Авто обновления выполнено')

    except requests.exceptions.RequestException as exr:
        logger.error(exr)
        Statistics.objects.create(message=f'Произошла ошибка #{exr.__class__}')
    except Exception as ex:
        logger.error(ex)
        Statistics.objects.create(message=f'Произошла ошибка #{ex.__class__}')
