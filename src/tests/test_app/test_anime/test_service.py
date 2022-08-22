from unittest import mock

from rest_framework.test import APITestCase

from src.anime.service import service

from . import config_data


class TestService(APITestCase):
    @mock.patch('src.anime.service.service.write_id_images')
    def test_write_images_telegram(self, mock_write_id_images):
        config_data.create_anime_kwargs()

        service.write_images_telegram()
        mock_write_id_images.assert_called_once()

    @mock.patch('src.anime.service.service.write_id_images')
    def test_write_images_telegram_filled(self, mock_write_id_images):
        config_data.create_anime_kwargs(telegram_id_file='Test')

        service.write_images_telegram()
        mock_write_id_images.assert_not_called()
