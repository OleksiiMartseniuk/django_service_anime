from rest_framework.test import APITestCase
from unittest import mock

from django.contrib import messages as dj_messages

from src.anime.service.admin.service import ParserControl, Status
from src.anime.service.admin import messages


class TestParserControl(APITestCase):
    @mock.patch('src.anime.service.admin.service.ServiceAnime.anime_schedule')
    def test_control_schedule(self, mock_anime_schedule):
        message = ParserControl().control('schedule')
        mock_anime_schedule.assert_called_once()

        self.assertEqual(message, Status(messages.SCHEDULE))

    @mock.patch('src.anime.service.admin.service.ServiceAnime.anime_anons')
    def test_control_anons(self, mock_anime_anons):
        message = ParserControl().control('anons')
        mock_anime_anons.assert_called_once()

        self.assertEqual(message, Status(messages.ANONS))

    @mock.patch('src.anime.service.admin.service.ServiceAnime.delete_table')
    def test_control_delete(self, mock_delete_table):
        message = ParserControl().control('delete')
        mock_delete_table.assert_called_once()

        self.assertEqual(message, Status(messages.DElETE))

    def test_control_Nome(self):
        message = ParserControl().control('test')

        self.assertEqual(message, Status(messages.ERROR, dj_messages.ERROR))

    @mock.patch(
        'src.anime.service.admin.service.ServiceAnime.anime_schedule_update'
    )
    def test_control_schedule_update(self, mock_anime_schedule_update):
        message = ParserControl().control('schedule_update')
        mock_anime_schedule_update.assert_called_once()

        self.assertEqual(message, Status(messages.SCHEDULE_UPDATE))

    @mock.patch(
        'src.anime.service.admin.service.ServiceAnime.anime_anons_update'
    )
    def test_control_anons_update(self, mock_anime_anons_update):
        message = ParserControl().control('anons_update')
        mock_anime_anons_update.assert_called_once()

        self.assertEqual(message, Status(messages.ANONS_UPDATE))
