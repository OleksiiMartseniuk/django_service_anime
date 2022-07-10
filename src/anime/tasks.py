from config.celery import app

from .service.service import ServiceAnime


@app.task
def parser(action: str) -> None:
    match action:
        case 'schedule':
            ServiceAnime().anime_schedule()
        case 'anons':
            ServiceAnime().anime_anons()
        case 'delete':
            ServiceAnime().delete_table()
        case 'schedule_update':
            ServiceAnime().anime_schedule_update()
        case 'anons_update':
            ServiceAnime().anime_anons_update()
