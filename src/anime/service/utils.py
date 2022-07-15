import re


def get_number(name: str) -> int | None:
    """Получение номера серии"""
    number = re.search(r'^\d*', name).group()
    return int(number) if number else None
