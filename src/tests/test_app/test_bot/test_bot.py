from unittest import mock

from rest_framework.test import APITestCase

from src.bot.services.bot import ServiceBot

from . import config_data


class TestServiceBot(APITestCase):
    @mock.patch('src.bot.services.bot.utils.write_id_images')
    def test_write_images_telegram(self, mock_write_id_images):
        config_data.create_anime()
        ServiceBot().write_images_telegram()
        mock_write_id_images.assert_called_once()

    @mock.patch('src.bot.services.bot.utils.write_id_images')
    def test_write_images_telegram_not_called(self, mock_write_id_images):
        anime = config_data.create_anime()
        config_data.create_bot_id_image(id_anime=anime.id)
        ServiceBot().write_images_telegram()
        mock_write_id_images.assert_not_called()
