from unittest import mock

from src.base.animevost.service import ServiceAnimeVost

from . import config_data


class TestServiceAnimeVost:
    @mock.patch('src.base.animevost.service.ApiAnimeVostClient.get_anime')
    @mock.patch('src.base.animevost.service.ParserClient.get_schedule')
    def test_get_data_anime_all(self, mock_get_schedule, mock_get_anime):
        mock_get_schedule.return_value = config_data.get_schedule_data
        mock_get_anime.return_value = config_data.get_anime_data
        result = ServiceAnimeVost().get_data_anime_all()
        assert result == config_data.get_data_anime_data

    @mock.patch('src.base.animevost.service.ApiAnimeVostClient.get_anime')
    @mock.patch('src.base.animevost.service.ParserClient.get_schedule')
    def test_get_data_anime_full(self, mock_get_schedule, mock_get_anime):
        mock_get_schedule.return_value = config_data.get_schedule_data_full
        mock_get_anime.return_value = config_data.get_anime_data

        result = ServiceAnimeVost().get_data_anime_all(True)
        assert result == config_data.get_data_anime_data_full

    @mock.patch('src.base.animevost.service.ApiAnimeVostClient.get_anime')
    def test_create_anime_full_list(self, mock_get_anime):
        mock_get_anime.return_value = config_data.get_anime_data

        result = ServiceAnimeVost()._create_anime_full_list(
            config_data.create_anime_full_list
        )
        assert result == config_data.create_anime_full_list_data

    @mock.patch('src.base.animevost.service.ApiAnimeVostClient.get_anime')
    def test_create_anime_full_list_composed(self, mock_get_anime):
        mock_get_anime.return_value = config_data.get_anime_data

        result = ServiceAnimeVost()._create_anime_full_list(
            config_data.create_anime_full_list_composed
        )
        assert result == config_data.create_anime_full_list_composed_data

    @mock.patch(
        'src.base.animevost.service.ServiceAnimeVost._create_anime_full_list'
    )
    @mock.patch('src.base.animevost.service.ParserClient.get_anons')
    def test_get_data_anime_anons(
            self, mock_get_anons,
            mock_create_anime_full_list
    ):
        mock_get_anons.return_value = config_data.create_anime_full_list
        anime_list = config_data.create_anime_full_list_data
        mock_create_anime_full_list.return_value = anime_list

        result = ServiceAnimeVost().get_data_anime_anons_all()

        assert result == config_data.create_anime_full_list_data

    @mock.patch(
        'src.base.animevost.service.ServiceAnimeVost._create_anime_full_list'
    )
    @mock.patch('src.base.animevost.service.ParserClient.get_anons')
    def test_get_data_anime_anons_full(
            self, mock_get_anons,
            mock_create_anime_full_list
    ):
        mock_anons = config_data.create_anime_full_list_composed
        mock_get_anons.return_value = mock_anons
        anime_list = config_data.create_anime_full_list_composed_data
        mock_create_anime_full_list.return_value = anime_list

        result = ServiceAnimeVost().get_data_anime_anons_all(True)

        assert result == config_data.create_anime_full_list_composed_data

    @mock.patch('src.base.animevost.service.ApiAnimeVostClient.get_anime')
    def test_create_anime(self, mock_get_anime):
        mock_get_anime.return_value = config_data.get_anime_data

        result = ServiceAnimeVost().get_anime(
            config_data.create_anime_full_list[0]
        )

        assert result == config_data.create_anime_full_list_data[0]

    @mock.patch('src.base.animevost.service.ApiAnimeVostClient.get_anime')
    def test_create_anime_full(self, mock_get_anime):
        mock_get_anime.return_value = config_data.get_anime_data

        result = ServiceAnimeVost().get_anime(
            config_data.create_anime_full_list_composed[0]
        )

        assert result == config_data.create_anime_full_list_composed_data[0]

    @mock.patch('src.base.animevost.service.ParserClient.get_anime_one')
    @mock.patch('src.base.animevost.service.ServiceAnimeVost.get_anime')
    def test_get_anime_data(self,  mock_get_anons, mock_get_anime_one):
        ServiceAnimeVost().get_anime_data(1, 'test')
        mock_get_anime_one.assert_called_once()
        mock_get_anons.assert_called_once()
