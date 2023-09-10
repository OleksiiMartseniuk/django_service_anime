import pytest

from src.utils.animevost.parser import ParserClient
from src.utils.animevost.api import ApiAnimeVostClient


@pytest.fixture()
def client_parser():
    client_parser = ParserClient()
    return client_parser


@pytest.fixture()
def client_api():
    client_api = ApiAnimeVostClient()
    return client_api
