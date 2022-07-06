import pytest
from unittest import mock

from . import config_data
from src.base.animevost.exception import (
    ParserClientStatusCodeError,
    NotDataError
)


class TestParseClient:

    @mock.patch('src.base.animevost.parser.requests.get')
    def test__get(self, mock_get, client_parser):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '<html></html>'

        result = client_parser._get('https://test')
        assert result == '<html></html>'

    @pytest.mark.parametrize('status_code', [500, 400, 300])
    @mock.patch('src.base.animevost.parser.requests.get')
    def test__get_error(self, mock_get, status_code, client_parser):
        mock_get.return_value.status_code = status_code

        with pytest.raises(ParserClientStatusCodeError):
            client_parser._get('https://test')

    @mock.patch('src.base.animevost.parser.ParserClient.get_composed')
    @mock.patch('src.base.animevost.parser.requests.get')
    def test_get_schedule_full_true(self, mock_get, get_composed, client_parser):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = config_data.schedule_html

        get_composed.return_value = []

        result = client_parser.get_schedule(full=True)
        assert result == config_data.schedule_data

    @pytest.mark.parametrize('data', [config_data.schedule_html_error_day,
                                      config_data.schedule_html_error_id])
    @mock.patch('src.base.animevost.parser.requests.get')
    def test_get_schedule_full_error_data(self, mock_get, data, client_parser):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = data

        with pytest.raises(NotDataError):
            client_parser.get_anons(full=True)

    @mock.patch('src.base.animevost.parser.requests.get')
    def test_get_schedule_full_false(self, mock_get,
                                     client_parser):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = config_data.schedule_html

        result = client_parser.get_schedule()
        assert result == config_data.schedule_data_false

    @mock.patch('src.base.animevost.parser.requests.get')
    def test_get_schedule_full_not_id(self, mock_get,
                                      client_parser):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = config_data.schedule_html_not_id

        result = client_parser.get_schedule()

        assert len(result['wednesday']) == 5

    @mock.patch('src.base.animevost.parser.requests.get')
    def test_get_composed(self, mock_get, client_parser):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = config_data.anime_composed_html

        result = client_parser.get_composed('https://test', 1)
        assert result == config_data.anime_composed_data

    @mock.patch('src.base.animevost.parser.requests.get')
    def test_get_composed_id(self, mock_get, client_parser):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = config_data.anime_composed_html

        result = client_parser.get_composed('https://test', '109')
        assert result == config_data.anime_composed_data_id

    @mock.patch('src.base.animevost.parser.requests.get')
    def test_get_composed_error(self, mock_get, client_parser):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '<html></html>'

        result = client_parser.get_composed('https://test', 1)
        assert result == []

    @mock.patch('src.base.animevost.parser.requests.get')
    def test_get_count_page(self, mock_get, client_parser):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = config_data.count_page_html

        result = client_parser._get_count_page()
        assert result == 2

    @pytest.mark.parametrize('data', [config_data.count_page_not_html,
                                      config_data.count_page_html_not_int])
    @mock.patch('src.base.animevost.parser.requests.get')
    def test_get_count_page_error(self, mock_get, data, client_parser):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = data

        result = client_parser._get_count_page()
        assert result is None

    @mock.patch('src.base.animevost.parser.ParserClient.get_composed')
    @mock.patch('src.base.animevost.parser.ParserClient._get_count_page')
    @mock.patch('src.base.animevost.parser.requests.get')
    def test_get_anons(self, mock_get, _get_count_page,
                       get_composed, client_parser):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = config_data.anons_html

        _get_count_page.return_value = 1
        get_composed.return_value = []

        result = client_parser.get_anons(full=True)

        assert result == config_data.anons_data

    @mock.patch('src.base.animevost.parser.ParserClient.get_composed')
    @mock.patch('src.base.animevost.parser.ParserClient._get_count_page')
    @mock.patch('src.base.animevost.parser.requests.get')
    def test_get_anons_error_count(self, mock_get, _get_count_page,
                       get_composed, client_parser):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = config_data.anons_html

        _get_count_page.return_value = None
        get_composed.return_value = []

        with pytest.raises(NotDataError):
            client_parser.get_anons(full=True)

    @mock.patch('src.base.animevost.parser.ParserClient.get_composed')
    @mock.patch('src.base.animevost.parser.ParserClient._get_count_page')
    @mock.patch('src.base.animevost.parser.requests.get')
    def test_get_anons_error_count(self, mock_get, _get_count_page,
                                   get_composed, client_parser):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '<html></html>'

        _get_count_page.return_value = 1
        get_composed.return_value = []

        result = client_parser.get_anons(full=True)

        assert result == []

        mock_get.return_value.status_code = 200
        _get_count_page.return_value = 0

        with pytest.raises(NotDataError):
            client_parser.get_anons(full=True)

    @mock.patch('src.base.animevost.parser.ParserClient.get_composed')
    @mock.patch('src.base.animevost.parser.ParserClient._get_count_page')
    @mock.patch('src.base.animevost.parser.requests.get')
    def test_get_anons_error_attribute(self, mock_get, _get_count_page,
                                       get_composed, client_parser):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = config_data.anons_error_attribute

        _get_count_page.return_value = 1
        get_composed.return_value = []

        with pytest.raises(NotDataError):
            client_parser.get_anons(full=True)

    @mock.patch('src.base.animevost.parser.ParserClient._get_count_page')
    @mock.patch('src.base.animevost.parser.requests.get')
    def test_get_anons_false(self, mock_get, _get_count_page, client_parser):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = config_data.anons_html

        _get_count_page.return_value = 1

        result = client_parser.get_anons()

        assert result == config_data.anons_data_false
