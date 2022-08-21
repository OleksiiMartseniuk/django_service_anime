import logging

from config.celery import app

from .services.bot import ServiceBot


logger = logging.getLogger('main')


@app.task
def bot_form(action: str) -> None:
    try:
        match action:
            case 'upload':
                ServiceBot().write_images_telegram()
    except Exception as ex:
        logger.error(ex)
