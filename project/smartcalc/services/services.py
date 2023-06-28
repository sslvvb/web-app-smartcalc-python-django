from . import calculator
from . import utils
from . import history
from . import logging  # rename ?

"""фасад для моей модели - все основные главные функции вызываются отсюда.
Cлой бизнес-логики, который вызывает другие слои бизнес-логики"""


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
