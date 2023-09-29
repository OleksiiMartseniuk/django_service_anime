import logging

from config.celery import app
from src.anime.sync.animevost.sync import AnimeVostSync


logger = logging.getLogger('db')


@app.task
def sync_anime_vost() -> None:
    anime_vost_sync = AnimeVostSync()
    try:
        anime_vost_sync.sync()
    except Exception as ex:
        logger.error("Error AnimeVostSync", exc_info=ex)
