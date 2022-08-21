from dataclasses import dataclass

from django.contrib import messages


@dataclass
class Status:
    """Сообщения"""
    message: str
    level: int = messages.INFO
