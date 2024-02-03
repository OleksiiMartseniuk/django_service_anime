from django.db import models


class SeriesAnimeVost(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField(
        blank=True,
        null=True,
    )
    serial_number = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    anime = models.ForeignKey(
        "AnimeVost",
        related_name="anime_series",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"[{self.id}]Series  [{self.anime_id}]AnimeVost"

    @property
    def get_anime_vost_preview(self) -> str:
        return f"http://media.aniland.org/img/{self.serial_number}.jpg"

    def get_anime_vost_quality(
        self,
        quality: str,
        is_prefix: bool = False,
    ) -> str | None:
        url = f"https://{'f' if is_prefix else ''}hd.trn.su/"
        quality_dict = {
            "sd": f"{url}{self.serial_number}.mp4",
            "hd": f"{url}720/{self.serial_number}.mp4",
            "fhd": f"{url}1080/{self.serial_number}.mp4"
        }
        return quality_dict.get(quality)
