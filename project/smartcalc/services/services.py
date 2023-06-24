# import history
from . import calculator

"""фасад для моей модели - все основные главные функции вызываются отсюда"""


# слой бизнес-логики, который вызывает другие слои бизнес-логики


def calculate_expression(expression: str) -> str:
    """Вычисляет результат выражения"""
    try:
        calcs = calculator.Calculator()  # куда-то мб вынести и создавать класс один раз ?
        return calcs.calculate(expression)
    except Exception as e:
        print(f'ERROR from services.py -- {e}')
        return "ERROR from services.py"
