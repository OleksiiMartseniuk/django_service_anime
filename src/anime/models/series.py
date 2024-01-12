from django.db import models


class Series(models.Model):
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

    animevost = models.ForeignKey(
        "AnimeVost",
        related_name="anime_series",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    anilibria = models.ForeignKey(
        "AniLibria",
        related_name="anime_series",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        title = f"Series[{self.id}]"
        if self.anilibria_id:
            title += f"AniLibria [{self.anilibria_id}]"
        elif self.animevost_id:
            title += f"AnimeVost [{self.animevost_id}]"
        return title

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
