from requests.exceptions import HTTPError


class AnimeVostStatusCodeError(HTTPError):
    pass


class AnimeVostAttributeError(AttributeError):
    pass


class AnimeVostDataError(Exception):
    pass
