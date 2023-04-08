from requests.exceptions import HTTPError


class AnimeVostStatusCodeError(HTTPError):
    """Error status code"""


class AnimeVostAttributeError(AttributeError):
    """No attribute"""


class AnimeVostDataError(Exception):
    """No data"""
