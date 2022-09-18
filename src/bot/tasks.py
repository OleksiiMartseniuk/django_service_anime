import logging

from config.celery import app

from src.anime.models import Anime

from .services.telegram import TelegramApiClient


logger = logging.getLogger('main')


@app.task
def reminders(chat_id: int, anime_id: int) -> None:
    """"Отправка напоминаний о выходе аниме"""
    if Anime.objects.filter(id=anime_id).exists():
        anime = Anime.objects.get(id=anime_id)
        TelegramApiClient().send_cart(chat_id, anime)
    else:
        logger.error(f'Anime not exists id[{anime_id}]')
