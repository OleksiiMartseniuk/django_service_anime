import pytest
from unittest import mock

from src.base.animevost.exception import (
    ApiAnimeVostClientStatusCodeError,
    ApiAnimeVostClientAttributeError
)
from . import config_data


class TestApiAnimeVostClient:

    @mock.patch('src.base.animevost.api.requests.get')
    def test_get(self, mock_get, client_api):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'data': 'test'}

        result = client_api._get('https://test')
        assert result == {'data': 'test'}

    @pytest.mark.parametrize('status_code', [500, 400, 300])
    @mock.patch('src.base.animevost.api.requests.get')
    def test__get_error(self, mock_get, status_code, client_api):
        mock_get.return_value.status_code = status_code

        with pytest.raises(ApiAnimeVostClientStatusCodeError):
            client_api._get('https://test')

    @mock.patch('src.base.animevost.api.requests.get')
    def test_get_anime(self, mock_get, client_api):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = config_data.anime_json

        result = client_api.get_anime(1)
        assert result == config_data.anime_data

    @mock.patch('src.base.animevost.api.requests.get')
    def test_get_anime_error(self, mock_get, client_api):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'data': []}

        with pytest.raises(ApiAnimeVostClientAttributeError):
            client_api.get_anime(1)

    @mock.patch('src.base.animevost.api.requests.post')
    def test_post(self, mock_post, client_api):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'data': 'test'}

        result = client_api._post('https://test')
        assert result == {'data': 'test'}

    @pytest.mark.parametrize('status_code', [500, 400, 300])
    @mock.patch('src.base.animevost.api.requests.post')
    def test_post_status(self, mock_post, status_code, client_api):
        mock_post.return_value.status_code = status_code

        with pytest.raises(ApiAnimeVostClientStatusCodeError):
            client_api._post('https://test')

    @mock.patch('src.base.animevost.api.requests.post')
    def test_post_404(self, mock_post, client_api):
        mock_post.return_value.status_code = 404
        mock_post.return_value.json.return_value = {'status': 'test'}

        with pytest.raises(ApiAnimeVostClientStatusCodeError):
            client_api._post('https://test')

    @mock.patch('src.base.animevost.api.requests.get')
    def test_get_last_anime(self, mock_get,  client_api):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = config_data.last_anime_json

        result = client_api.get_last_anime()
        assert result == config_data.last_anime_data

    @mock.patch('src.base.animevost.api.requests.get')
    def test_get_last_anime_error(self, mock_get,  client_api):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'status': 'false'}

        with pytest.raises(ApiAnimeVostClientAttributeError):
            client_api.get_last_anime(1)

    @mock.patch('src.base.animevost.api.requests.post')
    def test_search(self, mock_post, client_api):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = config_data.search_json

        result = client_api.search('name')
        assert result == config_data.search_data

    @mock.patch('src.base.animevost.api.requests.post')
    def test_search_error_name(self, mock_post, client_api):
        mock_post.return_value.status_code = 404
        mock_post.return_value.json.return_value = {'error': 'Not'}

        mock_post.return_value.json.return_value = {'data': 'Not'}
        with pytest.raises(ApiAnimeVostClientStatusCodeError):
            client_api.search('test')

    def test__create_anime_schemas(self, client_api):
        result = client_api._create_anime_schemas(
            config_data.anime_schemas_dict
        )
        assert result == config_data.anime_schemas_data

        config_data.anime_schemas_dict.update({
            'screenImage': ['', '', ''],
            'urlImagePreview': "http://uploads/posts/2022-01/1641826763_1.jpg"
        })

        result = client_api._create_anime_schemas(
            config_data.anime_schemas_dict
        )
        config_data.anime_schemas_data.screen_image = []
        new_preview = 'http://uploads/posts/2022-01/1641826763_1.jpg'
        config_data.anime_schemas_data.url_image_preview = new_preview
        assert result == config_data.anime_schemas_data

        config_data.anime_schemas_dict.update({
            'screenImage': ['img', 'img', 'img']
        })
        result = client_api._create_anime_schemas(
            config_data.anime_schemas_dict
        )
        config_data.anime_schemas_data.screen_image = ['img', 'img', 'img']
        assert result == config_data.anime_schemas_data

    @mock.patch('src.base.animevost.api.requests.post')
    def test_get_play_list(self, mock_post, client_api):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = config_data.play_list_json

        result = client_api.get_play_list(1)

        assert result == config_data.play_list_data

        mock_post.return_value.json.return_value = []
        result = client_api.get_play_list(1)
        assert result == []

        mock_post.return_value.json.return_value = [{'status': 'test'}]
        with pytest.raises(ValueError):
            client_api.get_play_list(1)
