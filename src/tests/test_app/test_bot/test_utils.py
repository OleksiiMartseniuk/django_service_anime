from rest_framework.test import APITestCase

from unittest import mock

from src.bot.services import utils

from . import config_data


class TestUtils(APITestCase):
    @mock.patch('src.bot.services.utils.TelegramApiClient.send_photo')
    def test_write_id_images(self, mock_send_photo):
        mock_send_photo.return_value = config_data.send_photo_data

        anime = config_data.create_anime()
        self.assertIsNone(anime.telegram_id_file)
        utils.write_id_images(anime)
        self.assertEqual(
            anime.telegram_id_file,
            config_data.send_photo_data['result']['photo'][-1]['file_id']
        )

    @mock.patch('src.bot.services.utils.logger', mock.Mock())
    @mock.patch('src.bot.services.utils.TelegramApiClient.send_photo')
    def test_write_id_images_data_none(self, mock_send_photo):
        mock_send_photo.return_value = None

        anime = config_data.create_anime()
        self.assertIsNone(anime.telegram_id_file)
        utils.write_id_images(anime)
        self.assertIsNone(anime.telegram_id_file)

    @mock.patch('src.bot.services.utils.logger', mock.Mock())
    @mock.patch('src.bot.services.utils.TelegramApiClient.send_photo')
    def test_write_id_images_except_key_error(self, mock_send_photo):
        mock_send_photo.return_value = {'status': False}

        anime = config_data.create_anime()
        self.assertIsNone(anime.telegram_id_file)
        utils.write_id_images(anime)
        self.assertIsNone(anime.telegram_id_file)
