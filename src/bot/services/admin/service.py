from django.contrib import messages

from src.base.utils import Status
from src.base import messages as ex_massages
from src.bot.tasks import bot_form


def form_control_bot(action: str) -> Status:
    """Запуск активностей формы"""
    match action:
        case 'upload':
            bot_form.delay('upload')
            status = Status(message=ex_massages.UPLOAD_BOT_FORM)
        case _:
            status = Status(
                message=ex_massages.ERROR,
                level=messages.ERROR
            )
    return status
