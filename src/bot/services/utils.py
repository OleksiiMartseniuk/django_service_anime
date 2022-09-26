import logging
import re

from datetime import datetime

from src.anime.models import Anime

from ..models import BotUser, BotUserAnimePeriodTask


logger = logging.getLogger('main')


def get_cart(anime: Anime) -> str:
    """Вывод аниме"""
    if anime.timer:
        date = datetime.utcfromtimestamp(anime.timer)
        date = date.strftime('%H:%M')
    else:
        date = 'В течении дня'
    time = f'<b>Время выхода</b> 🕜️ ({date}) \n'
    return f"<b>{anime.title.split('/')[0]}</b> \n\n" \
           f"{time}" \
           f"<b>Рейтинг</b> 📊 {anime.rating}\n" \
           f"<b>Голоса</b> 🗳️ {anime.votes}\n\n" \
           f"<a href='{anime.link}'>Смотреть на animevost.org</a>\n" \
           f"<a href='{get_link_mirror(anime.link)}'>Зеркало v2.vost.pw</a>"


def get_link_mirror(link: str) -> str | None:
    """Генерация ссылки зеркала"""
    if not link:
        # Ссылки нет
        return link
    result = re.sub(r'/animevost.org/', '/v2.vost.pw/', link)
    return result


def get_image(url_image_preview: str, telegram_id_file: str | None) -> str:
    """Получения доступной картинки"""
    return telegram_id_file if telegram_id_file else url_image_preview
