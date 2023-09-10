class AnimeVostException(Exception):
    pass


class AnimeVostStatusCodeError(AnimeVostException):
    pass


class AnimeVostAttributeError(AnimeVostException):
    pass


class AnimeVostDataError(AnimeVostException):
    pass
