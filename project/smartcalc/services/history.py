"""Модуль для работы с историей выражений."""

from pathlib import Path

HISTORY_PATH: str = "smartcalc/data/history.txt"


def read_file() -> list:
    """Чистает историю запросов из файла history.txt

    Returns:
        list: Список из введенных выражений и значения x.
    """
    Path(HISTORY_PATH).touch(exist_ok=True)
    with open(HISTORY_PATH, 'r', encoding='utf-8') as file:
        return file.readlines()


def clean() -> list:
    """Очищает историю запросов в файле history.txt

    Returns:
        list: Пустой список введенных выражений.
    """
    Path(HISTORY_PATH).touch(exist_ok=True)
    with open(HISTORY_PATH, 'r+', encoding='utf-8') as file:
        file.truncate(0)
        return file.readlines()


def write_history(record_line: str) -> list:
    """Чистает историю запросов из файла history.txt

    Returns:
        list: Список из введенных выражений и значения x.
        """
    # Path(HISTORY_PATH).touch(exist_ok=True)
    with open(HISTORY_PATH, 'a+', encoding='utf-8') as file:
        print(record_line, file=file)
        file.seek(0)
        return file.readlines()
