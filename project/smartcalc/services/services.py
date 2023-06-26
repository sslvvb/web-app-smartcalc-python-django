# import history
from . import calculator

"""фасад для моей модели - все основные главные функции вызываются отсюда"""
 

# слой бизнес-логики, который вызывает другие слои бизнес-логики


def get_expression_result(expression: str, x_value: str) -> str:  #  TODO: x value увести в модель
    """Вычисляет выражение. Возвращает строку - результат вычислений или текст ошибки.
    параметры - выражение, значениие х"""
    try:
        calcs = calculator.Calculator()  # FIXME: куда-то мб вынести и создавать класс один раз ? # + тип для калькс
        return calcs.calculate(expression)
    except Exception as e:
        print(f'ERROR from services.py -- {e}')
        return "ERROR from services.py"

# две строки пришло, одна строка вернулась - с ответом или ошибкой



# TODO: в модели вычисляю есть ли х
#       и обрабатываю все ошибки тоже тут
