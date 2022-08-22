from src.base.animevost.schemas import AnimeData, AnimeFull, Series, Anime
from src.anime.service.update_db import AnimeMini
from src.anime import models

write_anime_shem = AnimeData(
    id=2696,
    title='Воины Пограничья / Kyoukai Senki [1-25 из 25]',
    screen_image=[
        'https://animevost.org.jpg'
    ],
    rating=3190,
    votes=888,
    description='description',
    director='Хабара Нобуёси',
    url_image_preview='https://animevost.org/uploads/posts/2021-10/1633371168_1.jpg',
    year='2021',
    genre='приключения, комедия',
    timer=0,
    type='ТВ',
    link='https://animevost.org/tip/tv/2696-kyoukai-senki.html')

write_anime_composed = [AnimeData(
        id=2696,
        title='Kyoukai Senki [1-25 из 25]',
        screen_image=[
            'https://animevost.org.jpg'
        ],
        rating=3190,
        votes=888,
        description='description',
        director='Хабара Нобуёси',
        url_image_preview='https://animevost.org/uploads/posts/2021-10/1633371168_1.jpg',
        year='2021',
        genre='спорт',
        timer=0,
        type='ТВ',
        link='https://animevost.org/tip/tv/2696-kyoukai-senki.html'
    )]

write_anime_schedule_data = {
    'monday': [
        AnimeFull(
            id=2696,
            title='Воины Пограничья / Kyoukai Senki [1-25 из 25]',
            screen_image=[
                'https://animevost.org/uploads/posts/2021-10/1633975183_4.jpg',
                'https://animevost.org/uploads/posts/2021-10/1633975182_3.jpg',
                'https://animevost.org/uploads/posts/2021-10/1633975209_2.jpg'
            ],
            rating=3190,
            votes=888,
            description='description',
            director='Хабара Нобуёси',
            url_image_preview='https://animevost.org/uploads/posts/2021-10/1633371168_1.jpg',
            year='2021',
            genre='приключения, фантастика',
            timer=0,
            type='ТВ',
            link='https://animevost.org/tip/tv/2696-kyoukai-senki.html',
            anime_composed=[AnimeData(
                id=321312,
                title='Kyoukai Senki [1-25 из 25]',
                screen_image=[
                    'https://animevost.org/uploads/posts/2021-10/456463975183_4.jpg',
                ],
                rating=3190,
                votes=888,
                description='description',
                director='Хабара Нобуёси',
                url_image_preview='https://animevost.org/uploads/posts/2021-10/1633371168_1.jpg',
                year='2021',
                genre='приключения, фантастика, меха',
                timer=0,
                type='ТВ',
                link='https://animevost.org/tip/tv/321312-kyoukai-senki.html',
            )]
        )]
}

write_anime_anons_data = [AnimeFull(

    id=2696,
    title='Воины Пограничья / Kyoukai Senki [1-25 из 25] [Анонс]',
    screen_image=[
        'https://animevost.org/uploads/posts/2021-10/1633975183_4.jpg',
        'https://animevost.org/uploads/posts/2021-10/1633975182_3.jpg',
        'https://animevost.org/uploads/posts/2021-10/1633975209_2.jpg'
    ],
    rating=3190,
    votes=888,
    description='description',
    director='Хабара Нобуёси',
    url_image_preview='https://animevost.org/uploads/posts/2021-10/1633371168_1.jpg',
    year='2021',
    genre='приключения, фантастика',
    timer=0,
    type='ТВ',
    link='https://animevost.org/tip/tv/2696-kyoukai-senki.html',
    anime_composed=[AnimeData(
        id=321312,
        title='Kyoukai Senki [1-25 из 25]',
        screen_image=[
            'https://animevost.org/uploads/posts/2021-10/456463975183_4.jpg',
        ],
        rating=3190,
        votes=888,
        description='description',
        director='Хабара Нобуёси',
        url_image_preview='https://animevost.org/uploads/posts/2021-10/1633371168_1.jpg',
        year='2021',
        genre='приключения, фантастика, меха',
        timer=0,
        type='ТВ',
        link='https://animevost.org/tip/tv/321312-kyoukai-senki.html',
    )]
)]

update_anime_data = AnimeData(
        id=2696,
        title='Kyoukai Senki [1-25 из 25]',
        screen_image=[
            'https://animevost.org/uploads/posts/2021-10/456463975183_4.jpg',
        ],
        rating=3190,
        votes=888,
        description='description',
        director='Хабара Нобуёси',
        url_image_preview='https://animevost.org/uploads/posts/2021-10/1633371168_1.jpg',
        year='2021',
        genre='приключения, фантастика, меха',
        timer=0,
        type='ТВ',
        link='https://animevost.org/tip/tv/321312-kyoukai-senki.html',
    )

update_anime_schedule_data = {
    'monday': [
        AnimeFull(
            id=2696,
            title='Воины Пограничья / Kyoukai Senki [1-25 из 25]',
            screen_image=[
                'https://animevost.org/uploads/posts/2021-10/1633975183_4.jpg',
                'https://animevost.org/uploads/posts/2021-10/1633975182_3.jpg',
                'https://animevost.org/uploads/posts/2021-10/1633975209_2.jpg'
            ],
            rating=3190,
            votes=888,
            description='description',
            director='Хабара Нобуёси',
            url_image_preview='https://animevost.org/uploads/posts/2021-10/1633371168_1.jpg',
            year='2021',
            genre='приключения, фантастика',
            timer=0,
            type='ТВ',
            link='https://animevost.org/tip/tv/2696-kyoukai-senki.html',
            anime_composed=[AnimeData(
                id=321312,
                title='Kyoukai Senki [1-25 из 25]',
                screen_image=[
                    'https://animevost.org/uploads/posts/2021-10/456463975183_4.jpg',
                ],
                rating=3190,
                votes=888,
                description='description',
                director='Хабара Нобуёси',
                url_image_preview='https://animevost.org/uploads/posts/2021-10/1633371168_1.jpg',
                year='2021',
                genre='приключения, фантастика, меха',
                timer=0,
                type='ТВ',
                link='https://animevost.org/tip/tv/321312-kyoukai-senki.html',
            )]
        )]
}

create_schemas = AnimeMini(id=1, link='https://test')


def create_anime():
    models.Anime.objects.bulk_create([
        models.Anime(
            id_anime=1,
            title='title',
            link='anime_data.link',
            rating=1,
            votes=1,
            description='anime_data.description',
            director='anime_data.director',
            url_image_preview='url_image_preview',
            year='anime_data.year',
            type='an',
            anons=True,
            day_week='monday'
        ),
        models.Anime(
            id_anime=2,
            title='title1',
            link='anime_data.link',
            rating=1,
            votes=1,
            description='anime_data.description',
            director='anime_data.director',
            url_image_preview='url_image_preview1',
            year='anime_data.year1',
            type='an',
            anons=True,
            day_week='monday'
        )
    ])

write_series_data = [
    Series(
        name='350 серия',
        std='http://video.animetop.info/1703961250.mp4',
        hd='http://video.animetop.info/720/1703961250.mp4'
    ),
    Series(
        name='937 серия',
        std='http://video.animetop.info/2147416130.mp4',
        hd='http://video.animetop.info/720/2147416130.mp4'
    )
]


def create_anime_one():
    models.Anime.objects.create(
        id_anime=1,
        title='title',
        link='anime_data.link',
        rating=1,
        votes=1,
        description='anime_data.description',
        director='anime_data.director',
        url_image_preview='url_image_preview',
        year='anime_data.year',
        type='an',
        anons=True,
        day_week='monday'
    )


def create_anime_indefinite():
    models.Anime.objects.create(
        id_anime=1,
        title='title',
        link='anime_data.link',
        rating=1,
        votes=1,
        description='anime_data.description',
        director='anime_data.director',
        url_image_preview='url_image_preview',
        year='anime_data.year',
        type='an',
        indefinite_exit=True
    )


anime_schemas = Anime(
    id=1,
    title='Воины Пограничья / Kyoukai Senki [1-25 из 25]',
    screen_image=[
        'https://animevost.org.jpg'
    ],
    rating=3190,
    votes=888,
    description='description',
    director='Хабара Нобуёси',
    url_image_preview='https://animevost.org/uploads/posts/2021-10/1633371168_1.jpg',
    year='2021',
    genre='приключения, комедия',
    timer=0,
    type='ТВ')


def create_anime_kwargs(
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
) -> models.Anime:
    return models.Anime.objects.create(
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
