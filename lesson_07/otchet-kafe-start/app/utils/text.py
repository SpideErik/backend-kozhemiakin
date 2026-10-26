"""Утилиты для работы с текстом."""


def _squash_spaces(value: str) -> str:
    return " ".join(value.split())


def normalize_name(name: str) -> str:
    """Удаляет лишние пробелы.
    
    Args:
        name: исходная строка
    
    Returns:
        строка без лишних пробелов
    """
    return _squash_spaces(name).title()
