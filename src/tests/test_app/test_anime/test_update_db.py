from rest_framework.test import APITestCase
from unittest import mock

from src.anime.service.update_db import UpdateDataParser
from src.anime.models import Anime

from . import config_data


class TestUpdateDataParser(APITestCase):
    def test_update_anime(self):
        Anime.objects.create(
            id_anime=2696,
            title='test.title',
            link='test.link',
            rating=2,
            votes=2,
            description='test.description',
            director='test.director',
            url_image_preview='test.url_image_preview',
            year='test.year',
            type='as'
        )

        self.assertEqual(Anime.objects.count(), 1)

        result = UpdateDataParser()._update_anime(
            config_data.update_anime_data,
            'test'
        )
        self.assertTrue(result)

        self.assertEqual(Anime.objects.count(), 1)

        data = config_data.update_anime_data
        anime = Anime.objects.filter(id_anime=data.id).first()

        self.assertEqual(anime.title, data.title)
        self.assertEqual(anime.rating, data.rating)
        self.assertEqual(anime.votes, data.votes)
        self.assertEqual(anime.timer, data.timer)
        self.assertEqual(anime.day_week, 'test')
        self.assertFalse(anime.anons)

    def test_create_schemas(self):
        result = UpdateDataParser()._create_schemas(1, 'https://test')
        assert result == config_data.create_schemas

    @mock.patch('src.anime.service.update_db.UpdateDataParser._update_anime')
    def test_update_anime_schedule(self, mock_update_anime):
        mock_update_anime.return_value = 1
        Anime.objects.create(
            id_anime=2696,
            title='test.title',
            link='test.link',
            rating=2,
            votes=2,
            description='test.description',
            director='test.director',
            url_image_preview='test.url_image_preview',
            year='test.year',
            type='as'
        )
        self.assertEqual(Anime.objects.count(), 1)

        data = config_data.update_anime_schedule_data
        UpdateDataParser().update_anime_schedule(data)

        self.assertEqual(Anime.objects.count(), 1)

    @mock.patch('src.anime.service.update_db.UpdateDataParser._create_schemas')
    @mock.patch('src.anime.service.update_db.UpdateDataParser._update_anime')
    def test_update_anime_schedule_schemas(
            self,
            mock_update_anime,
            mock_create_schemas
    ):
        mock_update_anime.return_value = 0
        mock_create_schemas.return_value = config_data.create_schemas

        data = config_data.update_anime_schedule_data
        result = UpdateDataParser().update_anime_schedule(data)
        mock_update_anime.assert_called_once()
        self.assertEqual(result, [config_data.create_schemas])

    @mock.patch('src.anime.service.update_db.UpdateDataParser._update_anime')
    def test_update_anime_anons(self, mock_update_anime):
        mock_update_anime.return_value = 1

        data = config_data.update_anime_schedule_data['monday']
        UpdateDataParser().update_anime_anons(data)
        mock_update_anime.assert_called_once()

    @mock.patch('src.anime.service.update_db.UpdateDataParser._create_schemas')
    @mock.patch('src.anime.service.update_db.UpdateDataParser._update_anime')
    def test_update_anime_anons_write(
            self,
            mock_update_anime,
            mock_create_schemas
    ):
        mock_update_anime.return_value = 0
        mock_create_schemas.return_value = config_data.create_schemas

        data = config_data.update_anime_schedule_data['monday']
        result = UpdateDataParser().update_anime_anons(data)

        mock_update_anime.assert_called_once()
        self.assertEqual(result, [config_data.create_schemas])
