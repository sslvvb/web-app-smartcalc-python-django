"""Фасад модели. Вывает функции всех модулей модели. Cлой бизнес-логики, который вызывает другие слои бизнес-логики"""

from . import calculator
from . import history


def read_history() -> list:
    """Вызывает функцию чтения истории введенных выражений модуля history

    Returns:
        list: Список из введенных выражений и значения x.
    """
    return history.read_file()


def write_history(string_to_write: str) -> list:
    """Вызывает функцию, добавляющую запрос в историю выражений модуля history

    Returns:
        list: Обновленный список из введенных выражений.
    """
    return history.write(string_to_write)


def clean_history() -> list:
    """Вызывает функцию очищения истории введенных выражений модуля history

    Returns:
        list: Пустой список введенных выражений.
    """
    return history.clean()


def get_expression_result(expression: str, x_value: str) -> str:
    """вызывает функцию
    Вычисляет выражение. Возвращает строку - результат вычислений или текст ошибки.
    параметры - выражение, значениие х"""

    # сохранить в историю

    if "x" in expression:
        expression = expression.replace("x", x_value)

    result = calculator.calculate(expression)
    if result is not None:
        return result
    else:
        return "Error in expression"


def graph_expression_result(expression: str, x_min: str, x_max: str) -> list:
    result = calculator.graph_calculate(expression, x_min, x_max)
    if result is not None:
        return result
    else:
        return "Error in expression"  # how handle ?
