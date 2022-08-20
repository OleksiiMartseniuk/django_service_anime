from src.bot.models import BotIdImage
from src.anime.models import Anime

from django.db.models import Q

from . import utils


class ServiceBot:
    def write_images_telegram(self):
        """Запись картинки на сервер telegram"""
        bot_id_list = BotIdImage.objects.values_list('id_anime', flat=True)
        anime_list = Anime.objects.filter(~Q(pk__in=bot_id_list)).\
            only('id', 'url_image_preview_s')
        for anime in anime_list:
            utils.write_id_images(anime.id, anime.url_image_preview_s.path)
