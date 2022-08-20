from rest_framework.test import APITestCase

from unittest import mock

from src.bot.models import BotIdImage
from src.bot.services import utils

from . import config_data


class TestUtils(APITestCase):
    @mock.patch('src.bot.services.utils.TelegramApiClient.send_photo')
    def test_write_id_images(self, mock_send_photo):
        mock_send_photo.return_value = config_data.send_photo_data

        self.assertEqual(BotIdImage.objects.count(), 0)
        utils.write_id_images(1, 'path')
        self.assertEqual(BotIdImage.objects.count(), 1)

    @mock.patch('src.bot.services.utils.TelegramApiClient.send_photo')
    def test_write_id_images_data_none(self, mock_send_photo):
        mock_send_photo.return_value = None

        self.assertEqual(BotIdImage.objects.count(), 0)
        utils.write_id_images(1, 'path')
        self.assertEqual(BotIdImage.objects.count(), 0)

    @mock.patch('src.bot.services.utils.logger', mock.Mock())
    @mock.patch('src.bot.services.utils.TelegramApiClient.send_photo')
    def test_write_id_images_except_key_error(self, mock_send_photo):
        mock_send_photo.return_value = {'status': False}

        self.assertEqual(BotIdImage.objects.count(), 0)
        utils.write_id_images(1, 'path')
        self.assertEqual(BotIdImage.objects.count(), 0)
