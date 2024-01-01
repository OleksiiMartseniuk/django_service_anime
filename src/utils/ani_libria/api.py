import requests
import json

from .exception import RequestErrorAniLibria
from .schemas import Title, ScheduleList


class ClientAniLibria:
    def __init__(self, version: str = "v2"):
        self.base_url = f"https://api.anilibria.tv/{version}/"

    @staticmethod
    def __get(url: str, **params) -> dict:
        response = requests.get(url=url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise RequestErrorAniLibria(
                f"Request {url} status code [{response.status_code}] "
                f"kwargs[{json.dumps(params)}]"
            )

    def get_title(self, **params) -> Title:
        """
        https://github.com/anilibria/docs/blob/master/api_v2.md#-gettitle
        """
        url = f"{self.base_url}getTitle"
        title = self.__get(url, **params)
        return Title(**title)

    def get_schedule(self, **params):
        """
        https://github.com/anilibria/docs/blob/master/api_v2.md#-getschedule
        """
        url = f"{self.base_url}getSchedule"
        schedule = self.__get(url, **params)
        return ScheduleList(schedule=schedule)
