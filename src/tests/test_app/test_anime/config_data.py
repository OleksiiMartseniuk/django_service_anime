from src.base.animevost.schemas import AnimeData, AnimeFull
from src.anime.service.update_db import AnimeMini
from src.anime.models import Anime

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
    Anime.objects.bulk_create([
        Anime(
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
        Anime(
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
