# import history
from .calculator import Calculator
import utils


"""фасад для моей модели - все основные главные функции вызываются отсюда"""


# слой бизнес-логики, который вызывает другие слои бизнес-логики


# две строки пришло, одна строка вернулась - с ответом или ошибкой
def get_expression_result(expression: str, x_value: str) -> str:
    """Вычисляет выражение. Возвращает строку - результат вычислений или текст ошибки.
    параметры - выражение, значениие х"""
    if utils.check_expression_valid(expression):
        return "ERROR - expression invalid"
    elif utils.check_x_value_valid(x_value):
        return "ERROR - X value invalid"
    else:
        try:
            calcs = Calculator.Calculator()  # rename
            return calcs.calculate(expression)
        except Exception as e:
            print(f'ERROR from services.py -- {e}')
            return "ERROR from services.py"


# TODO: x value увести в модель
# TODO: перед входом в модель проверять данные на валидность и потом подразумевать что все чистое
# FIXME: куда-то мб вынести и создавать класс один раз ? # + тип для калькс // calcs = calculator.Calculator()
# TODO: в модели вычисляю есть ли х и обрабатываю все ошибки тоже тут


def graph_expression_result():  # мб и не нужен будет
    pass
