import logging

from config.celery import app

from src.anime.models import Statistics

from .services.bot import ServiceBot


logger = logging.getLogger('main')


@app.task
def bot_form(action: str) -> None:
    try:
        match action:
            case 'upload':
                ServiceBot().write_images_telegram()
    except Exception as ex:
        Statistics.objects.create(
            message=f'Произошла ошибка[telegram-bot] #{ex.__class__}'
        )
        logger.error(ex)


@app.task
def auto_write_img() -> None:
    """Авто запись картинок на сервис телеграм"""
    try:
        ServiceBot().write_images_telegram()
        # Запись в статистику
        Statistics.objects.create(
            message='Авто запись картинок на сервис телеграм'
        )
    except Exception as ex:
        Statistics.objects.create(
            message=f'Произошла ошибка[telegram-bot] #{ex.__class__}'
        )
        logger.error(ex)
