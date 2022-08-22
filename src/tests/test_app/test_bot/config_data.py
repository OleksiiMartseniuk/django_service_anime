from src.anime.models import Anime


send_photo_data = {
    'result':
        {'photo':
         [
             {'file_id': 'NWvwsqQAgACncExG5vjAUiWz9SUT4i1'},
             {'file_id': 'NWvwsqQAgACncExG5vjAUiWz9SUT4i2'},
             {'file_id': 'NWvwsqQAgACncExG5vjAUiWz9SUT4i3'},
         ]
         }
}


def create_anime(
        id_anime: int = 1,
        title: str = 'title',
        link: str = 'anime_data.link',
        rating: int = 1,
        votes: int = 1,
        description: str = 'anime_data.description',
        director: str = 'anime_data.director',
        url_image_preview: str = 'url_image_preview',
        url_image_preview_s: str = 'url_image_preview_s',
        telegram_id_file: str = None,
        year: str = 'anime_data.year',
        type: str = 'an',
        anons: bool = True,
        day_week: str = 'monday'
):
    return Anime.objects.create(
        id_anime=id_anime,
        title=title,
        link=link,
        rating=rating,
        votes=votes,
        description=description,
        director=director,
        url_image_preview=url_image_preview,
        url_image_preview_s=url_image_preview_s,
        telegram_id_file=telegram_id_file,
        year=year,
        type=type,
        anons=anons,
        day_week=day_week
    )
