from rest_framework.test import APITestCase
from unittest import mock

from src.anime.service.update_db import UpdateDataParser
from src.anime.models import Anime, Series

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
        self.assertEqual(result, config_data.create_schemas)

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

    def test_update_anime_schedule_result_id(self):
        anime = Anime.objects.create(
            id_anime=2,
            title='test.title',
            link='test.link',
            rating=2,
            votes=2,
            description='test.description',
            director='test.director',
            url_image_preview='test.url_image_preview',
            year='test.year',
            type='as',
            day_week='monday'
        )
        anime1 = Anime.objects.create(
            id_anime=2696,
            title='test.title',
            link='test.link',
            rating=2,
            votes=2,
            description='test.description',
            director='test.director',
            url_image_preview='test.url_image_preview',
            year='test.year',
            type='as',
            day_week='monday'
        )
        data = config_data.update_anime_schedule_data
        self.assertEqual(Anime.objects.count(), 2)
        self.assertEqual(anime.day_week, 'monday')
        self.assertEqual(anime1.day_week, 'monday')
        UpdateDataParser().update_anime_schedule(data)
        self.assertEqual(Anime.objects.count(), 2)
        anime_obj = Anime.objects.get(id=anime.id)
        anime_obj1 = Anime.objects.get(id=anime1.id)
        self.assertEqual(anime_obj.day_week, None)
        self.assertEqual(anime_obj1.day_week, 'monday')

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

    def test_update_series(self):
        Series.objects.create(
            id_anime=1,
            name='350 серия',
            std='http://video.animetop.info/1703961250.mp4',
            hd='http://video.animetop.info/720/1703961250.mp4'
        )
        self.assertEqual(Series.objects.count(), 1)
        UpdateDataParser().update_series(1, config_data.write_series_data)
        self.assertEqual(Series.objects.count(), 2)
        series_list = Series.objects.filter(id_anime=1)
        self.assertEqual(series_list[0].name, '350 серия')
        self.assertEqual(series_list[1].name, '937 серия')

    @mock.patch('src.anime.service.update_db.UpdateDataParser._update_anime')
    def test_update_indefinite_exit_update(self, mock_update_anime):
        config_data.create_anime_indefinite()
        result = UpdateDataParser().update_indefinite_exit(
            [config_data.anime_schemas]
        )
        mock_update_anime.assert_called_once()
        self.assertIsNone(result)

    @mock.patch('src.anime.service.update_db.UpdateDataParser._update_anime')
    def test_update_indefinite_exit_write(self, mock_update_anime):
        result = UpdateDataParser().update_indefinite_exit(
            [config_data.anime_schemas]
        )
        self.assertFalse(mock_update_anime.called)
        self.assertEqual(result, [config_data.anime_schemas])
