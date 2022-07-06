from requests.exceptions import HTTPError


class ParserClientStatusCodeError(HTTPError):
    """Неверный статус код ответа"""


class ApiAnimeVostClientStatusCodeError(HTTPError):
    """Неверный статус код ответа"""


class ApiAnimeVostClientAttributeError(AttributeError):
    """Пришедшие дынные с api animevost не верны"""


class NotDataError(Exception):
    """Нет данных"""
