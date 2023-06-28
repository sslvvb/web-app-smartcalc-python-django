"""Фасад модели. Вывает функции всех модулей модели. Cлой бизнес-логики, который вызывает другие слои бизнес-логики"""

from . import calculator
from . import utils
from . import history


def read_history() -> list:
    """Вызывает функцию чтения истории введенных выражений модуля history

    Returns:
        list: Список из введенных выражений и значения x.
    """
    return history.read_file()


def write_history(expression: str, x_value: str) -> list:
    """"""
    record_line: str = '; '.join((expression, x_value))  # TODO: collect valid line
    return history.write_history(record_line)


def clean_history() -> list:
    """Вызывает функцию очищения истории введенных выражений модуля history

    Returns:
        list: Пустой список введенных выражений.
    """
    return history.clean()


# def select_history():
#     pass


def get_expression_result(expression: str, x_value: str) -> str:
    """Вычисляет выражение. Возвращает строку - результат вычислений или текст ошибки.
    параметры - выражение, значениие х"""

    if utils.check_expression_valid(expression) is False:
        return 'Expression invalid'
    elif utils.check_x_value_valid(x_value) is False:
        return 'X value invalid'

    # сохранить в историю

    if "x" in expression:
        expression = expression.replace("x", x_value)

    try:
        calcs = calculator.Calculator()
        return calcs.calculate(expression)
    except Exception as e:
        return f"EXCEPTION ERROR FROM services.py: {str(e)}"


def graph_expression_result():  # ?
    pass
