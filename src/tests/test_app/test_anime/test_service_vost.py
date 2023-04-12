from rest_framework.test import APITestCase
from unittest import mock

from src.anime.service.service_vost import ServiceAnime

from . import config_data


class TestServiceAnime(APITestCase):
    @mock.patch(
        'src.anime.service.service_vost.ServiceAnimeVost.get_data_anime_all')
    @mock.patch('src.anime.service.service_vost.WriteDB.write_anime_schedule')
    def test_anime_schedule(
            self,
            mock_write_anime_schedule,
            mock_get_data_anime_all
    ):
        ServiceAnime().anime_schedule()
        mock_write_anime_schedule.assert_called_once()
        mock_get_data_anime_all.assert_called_once()

    @mock.patch(
        'src.anime.service.service_vost.ServiceAnimeVost.get_data_anime_anons_all'
    )
    @mock.patch('src.anime.service.service_vost.WriteDB.write_anime_anons')
    def test_anime_anons(
            self,
            mock_write_anime_anons,
            mock_get_data_anime_anons_all
    ):
        mock_get_data_anime_anons_all.return_value = ["test"]
        ServiceAnime().anime_anons()
        mock_get_data_anime_anons_all.assert_called_once()
        mock_write_anime_anons.assert_called_once()


    @mock.patch(
        'src.anime.service.service_vost.ServiceAnimeVost.get_anime_data'
    )
    @mock.patch('src.anime.service.service_vost.WriteDB.write_anime_full')
    def test_write_anime_none(
            self,
            mock_get_anime_data,
            mock_write_anime_full
    ):
        ServiceAnime()._write_anime([])
        self.assertFalse(mock_get_anime_data.called)
        self.assertFalse(mock_write_anime_full.called)

    @mock.patch(
        'src.anime.service.service_vost.ServiceAnimeVost.get_anime_data'
    )
    @mock.patch('src.anime.service.service_vost.WriteDB.write_anime_full')
    def test_write_anime(
            self,
            mock_get_anime_data,
            mock_write_anime_full
    ):
        ServiceAnime()._write_anime([config_data.create_schemas])
        mock_get_anime_data.assert_called_once()
        mock_write_anime_full.assert_called_once()

    @mock.patch(
        'src.anime.service.service_vost.ServiceAnimeVost.get_data_anime_all'
    )
    @mock.patch(
        'src.anime.service.service_vost.UpdateDataParser.update_anime_schedule'
    )
    @mock.patch('src.anime.service.service_vost.ServiceAnime._write_anime')
    def test_anime_schedule_update(
            self,
            mock_write_anime,
            mock_update_anime_schedule,
            mock_get_data_anime_all
    ):
        ServiceAnime().anime_schedule_update()
        mock_write_anime.assert_called_once()
        mock_update_anime_schedule.assert_called_once()
        mock_get_data_anime_all.assert_called_once()

    @mock.patch(
        'src.anime.service.service_vost.ServiceAnimeVost.get_data_anime_anons_all'
    )
    @mock.patch(
        'src.anime.service.service_vost.UpdateDataParser.update_anime_anons'
    )
    @mock.patch('src.anime.service.service_vost.ServiceAnime._write_anime')
    def test_anime_anons_update(
            self,
            mock_write_anime,
            mock_update_anime_anons,
            mock_get_data_anime_anons_all
    ):
        ServiceAnime().anime_anons_update()
        mock_write_anime.assert_called_once()
        mock_update_anime_anons.assert_called_once()
        mock_get_data_anime_anons_all.assert_called_once()

    @mock.patch('src.anime.service.service_vost.WriteDB.write_series')
    @mock.patch(
        'src.anime.service.service_vost.ServiceAnimeVost.get_list_series'
    )
    def test_series(self, mock_get_list_series, mock_write_series):
        config_data.create_anime_one()
        ServiceAnime().series()
        mock_get_list_series.assert_called_once()
        mock_write_series.assert_called_once()

    @mock.patch(
        'src.anime.service.service_vost.UpdateDataParser.update_series'
    )
    @mock.patch(
        'src.anime.service.service_vost.ServiceAnimeVost.get_list_series'
    )
    def test_series_update(self, mock_get_list_series, mock_update_series):
        config_data.create_anime_one()
        ServiceAnime().series_update()
        mock_get_list_series.assert_called_once()
        mock_update_series.assert_called_once()

    @mock.patch('src.anime.service.service_vost.WriteDB.write_anime_full')
    @mock.patch('src.anime.service.service_vost.UpdateDataParser.update_indefinite_exit')
    @mock.patch('src.anime.service.service_vost.ServiceAnimeVost.get_anime_indefinite_exit')
    def test_update_indefinite_exit_none(
            self,
            mock_get_last_anime,
            mock_update_indefinite_exit,
            mock_get_anime_indefinite_exit
    ):
        mock_update_indefinite_exit.return_value = None
        ServiceAnime().update_indefinite_exit()
        mock_get_last_anime.assert_called_once()
        mock_update_indefinite_exit.assert_called_once()
        self.assertFalse(mock_get_anime_indefinite_exit.called)

    @mock.patch('src.anime.service.service_vost.get_link')
    @mock.patch('src.anime.service.service_vost.WriteDB.write_anime_full')
    @mock.patch('src.anime.service.service_vost.ServiceAnimeVost.get_anime_data')
    @mock.patch('src.anime.service.service_vost.UpdateDataParser.update_indefinite_exit')
    @mock.patch('src.anime.service.service_vost.ServiceAnimeVost.get_anime_indefinite_exit')
    def test_update_indefinite_exit_link_not(
            self,
            mock_get_anime_indefinite_exit,
            mock_update_indefinite_exit,
            mock_get_anime_data,
            mock_write_anime_full,
            mock_get_link
    ):
        mock_update_indefinite_exit.return_value = [config_data.anime_schemas]
        mock_get_link.return_value = None
        ServiceAnime().update_indefinite_exit()
        mock_get_anime_indefinite_exit.assert_called_once()
        mock_update_indefinite_exit.assert_called_once()
        self.assertFalse(mock_get_anime_data.called)
        self.assertFalse(mock_write_anime_full.called)

    @mock.patch('src.anime.service.service_vost.get_link')
    @mock.patch('src.anime.service.service_vost.WriteDB.write_anime_full')
    @mock.patch('src.anime.service.service_vost.ServiceAnimeVost.get_anime_data')
    @mock.patch('src.anime.service.service_vost.UpdateDataParser.update_indefinite_exit')
    @mock.patch('src.anime.service.service_vost.ServiceAnimeVost.get_anime_indefinite_exit')
    def test_update_indefinite_exit(
            self,
            mock_get_anime_indefinite_exit,
            mock_update_indefinite_exit,
            mock_get_anime_data,
            mock_write_anime_full,
            mock_get_link
    ):
        mock_update_indefinite_exit.return_value = [config_data.anime_schemas]
        mock_get_link.return_value = 'test-link'
        ServiceAnime().update_indefinite_exit()
        mock_get_anime_indefinite_exit.assert_called_once()
        mock_update_indefinite_exit.assert_called_once()
        mock_get_anime_data.assert_called_once()
        mock_write_anime_full.assert_called_once()
