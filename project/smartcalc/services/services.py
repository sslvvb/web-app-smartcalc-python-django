# import history
from . import calculator

"""фасад для моей модели - все основные главные функции вызываются отсюда"""


# слой бизнес-логики, который вызывает другие слои бизнес-логики


def get_expression_result(expression: str, x_value: str) -> str:  # x value увести в модель
    """Вычисляет выражения и
    Возвращает строку - результат вычислений выражения или текст ошибки
    параметры - выражение, значениие х"""
    try:
        calcs = calculator.Calculator()  # куда-то мб вынести и создавать класс один раз ?
        return calcs.calculate(expression)
    except Exception as e:
        print(f'ERROR from services.py -- {e}')
        return "ERROR from services.py"
