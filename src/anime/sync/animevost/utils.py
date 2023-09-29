from dataclasses import dataclass


@dataclass
class ReportAnime:
    created_quantity: int = 0
    created_success: int = 0
    created_errors: int = 0
    updated_quantity: int = 0
    updated_success: int = 0
    updated_errors: int = 0

    @staticmethod
    def get_items_list(items: list) -> str:
        str_items = ""
        for i, w in enumerate(items, 1):
            if not i % 10:
                str_items += "\n"
            str_items += f"{w}, "
        return str_items
