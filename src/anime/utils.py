import logging
import requests
from io import BytesIO

from django.core.files import File
from django.db.models.fields.files import ImageFieldFile

logger = logging.getLogger('db')


def download_image(obj_image: ImageFieldFile, image_url: str) -> bool:
    try:
        responses = requests.get(image_url)
        if responses.status_code == 200:
            fp = BytesIO()
            fp.write(responses.content)
            file_name = image_url.split("/")[-1]
            obj_image.save(file_name, File(fp))
            return True
        else:
            logger.error(
                f'Status Code [download image] [{responses.status_code}] '
                f'url[{image_url}]'
            )
    except Exception as ex:
        logger.error("Download image", exc_info=ex)
    return False
