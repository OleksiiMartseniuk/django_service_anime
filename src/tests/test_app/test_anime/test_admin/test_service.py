from rest_framework.test import APITestCase
from unittest import mock

from django.contrib import messages as dj_messages

from src.anime.service.admin.service import ParserControl, Status
from src.anime.service.admin import messages


class TestParserControl(APITestCase):
    @mock.patch('src.anime.service.admin.service.parser.delay')
    def test_control_schedule(self, mock_parser):
        message = ParserControl().control('schedule')
        mock_parser.assert_called_once()

        self.assertEqual(message, Status(messages.SCHEDULE))

    @mock.patch('src.anime.service.admin.service.parser.delay')
    def test_control_anons(self, mock_parser):
        message = ParserControl().control('anons')
        mock_parser.assert_called_once()

        self.assertEqual(message, Status(messages.ANONS))

    @mock.patch('src.anime.service.admin.service.parser.delay')
    def test_control_delete(self, mock_parser):
        message = ParserControl().control('delete')
        mock_parser.assert_called_once()

        self.assertEqual(message, Status(messages.DElETE))

    def test_control_Nome(self):
        message = ParserControl().control('test')

        self.assertEqual(message, Status(messages.ERROR, dj_messages.ERROR))

    @mock.patch('src.anime.service.admin.service.parser.delay')
    def test_control_schedule_update(self, mock_parser):
        message = ParserControl().control('schedule_update')
        mock_parser.assert_called_once()

        self.assertEqual(message, Status(messages.SCHEDULE_UPDATE))

    @mock.patch('src.anime.service.admin.service.parser.delay')
    def test_control_anons_update(self, mock_parser):
        message = ParserControl().control('anons_update')
        mock_parser.assert_called_once()

        self.assertEqual(message, Status(messages.ANONS_UPDATE))
