from rest_framework.test import APITestCase
from rest_framework.exceptions import ValidationError

from unittest import mock

from src.bot.services import service
from src.bot.models import BotUserAnimePeriodTask
from . import config_data


class TestService(APITestCase):

    @mock.patch('src.bot.services.service.TelegramApiClient.send_photo')
    def test_write_id_images(self, mock_send_photo):
        mock_send_photo.return_value = config_data.send_photo_data

        anime = config_data.create_anime()
        self.assertIsNone(anime.telegram_id_file)
        service.write_id_images(anime)
        self.assertEqual(
            anime.telegram_id_file,
            config_data.send_photo_data['result']['photo'][-1]['file_id']
        )

    @mock.patch('src.bot.services.service.logger', mock.Mock())
    @mock.patch('src.bot.services.service.TelegramApiClient.send_photo')
    def test_write_id_images_data_none(self, mock_send_photo):
        mock_send_photo.return_value = None

        anime = config_data.create_anime()
        self.assertIsNone(anime.telegram_id_file)
        service.write_id_images(anime)
        self.assertIsNone(anime.telegram_id_file)

    @mock.patch('src.bot.services.service.logger', mock.Mock())
    @mock.patch('src.bot.services.service.TelegramApiClient.send_photo')
    def test_write_id_images_except_key_error(self, mock_send_photo):
        mock_send_photo.return_value = {'status': False}

        anime = config_data.create_anime()
        self.assertIsNone(anime.telegram_id_file)
        service.write_id_images(anime)
        self.assertIsNone(anime.telegram_id_file)

    def test_formation_list_bot_user_anime_period_task(self):
        anime = config_data.create_anime()
        user = config_data.create_bot_user()
        objects = service.formation_list_bot_user_anime_period_task(
            [anime], user
        )
        obj: BotUserAnimePeriodTask = objects[0]

        self.assertEqual(obj.anime.id, anime.id)
        self.assertEqual(obj.user.id, user.id)

    def test_add_anime(self):
        anime = config_data.create_anime()
        user = config_data.create_bot_user()
        self.assertEqual(user.track.count(), 0)
        service.add_anime([anime.id], user.user_id)
        self.assertEqual(user.track.count(), 1)

    @mock.patch('src.bot.services.service.logger', mock.Mock())
    def test_add_anime_invalid_anime(self):
        user = config_data.create_bot_user()
        self.assertEqual(user.track.count(), 0)
        self.assertRaises(
            ValidationError, service.add_anime, [1], user.user_id
        )
        self.assertEqual(user.track.count(), 0)

    @mock.patch('src.bot.services.service.logger', mock.Mock())
    def test_add_anime_invalid_user(self):
        anime = config_data.create_anime()
        self.assertRaises(ValidationError, service.add_anime, [anime.id], 1)
