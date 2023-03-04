import logging
import requests
import time

from config.celery import app

from .service.service_vost import ServiceAnime
from .service import service
from .models import Anime, Series, AnimeSettings

from src.bot.services.service import update_user_tracked


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
            case 'write_telegram':
                service.write_images_telegram()

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
        # Запись картинок на сервер telegram
        settings_anime = AnimeSettings.get_solo()
        if settings_anime.send_images_telegram:
            service.write_images_telegram()

        # Обновления серий
        if Series.objects.count():
            ServiceAnime().series_update()
        else:
            logger.error('Не данных для обновления [series]')

        # Обновить список подписок telegram пользователя
        update_user_tracked()
        finish = time.time() - start_time
        logger.info(f"Полное обновления данных закончено. Время [{finish}]")
    except requests.exceptions.RequestException as exr:
        logger.error(f"{exr.__class__}")
    except Exception as ex:
        logger.error("Exception", exc_info=ex)
