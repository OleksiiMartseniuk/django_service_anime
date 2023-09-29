import logging

from config.celery import app
from django_db_logger.models import StatusLog

from src.anime.sync.animevost.utils import ReportAnime
from src.anime.sync.animevost.sync import AnimeVostSync


logger = logging.getLogger('db')


@app.task
def sync_anime_vost() -> None:
    anime_vost_sync = AnimeVostSync()
    try:
        anime_vost_sync.sync()
    except Exception as ex:
        logger.error("Error AnimeVostSync", exc_info=ex)


@app.task()
def update_anime(anime_ids: list[int]):
    report = ReportAnime()
    sync = AnimeVostSync()
    report.updated_quantity = len(anime_ids)
    for anime_id in anime_ids:
        try:
            sync.update_anime(anime_id=anime_id)
        except Exception as ex:
            report.updated_errors += 1
            logger.error(f"Anime {anime_id} not updated", exc_info=ex)
        else:
            report.updated_success += 1
    msg = (
        f"Update Anime site admin"
        f"\n{'=' * 40}\n"
        f"- Updated {report.updated_success}/"
        f"{report.updated_quantity}\n"
        f"- Update error {report.updated_errors}\n"
        f"\n- Anime update list:\n"
        f"{ReportAnime.get_items_list(sync.report_updated)}\n"
    )
    StatusLog.objects.create(
        logger_name="db",
        level=logging.INFO,
        msg="Update admin site",
        trace=msg,
    )
