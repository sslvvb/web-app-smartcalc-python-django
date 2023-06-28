"""Model class, wrapper for C++ kernel."""

import ctypes


# мб избавлюсь от класса если он не понадобится для графика
class Calculator:
    def __init__(self) -> None:
        self.model_lib = ctypes.CDLL(
            # '/opt/goinfre/hjerilyn/projects/python_calc_4/my_github_calc_web/project/smartcalc/services/model.so')
            '/Users/sslvvb/Documents/S21/Projects/Python/python_calc_4/my_github_web_calc/project/smartcalc/services'
            '/model.so')  # относительный путь + мб в билд переложить ?

    def calculate(self, expression: str) -> str:
        self.model_lib.GetResult.argtypes = [ctypes.c_char_p]
        self.model_lib.GetResult.restype = ctypes.c_double
        try:
            return self.model_lib.GetResult(expression.encode())
        except Exception as e:
            return f"EXCEPTION ERROR FROM calculator.py: {str(e)}"
        # это все бесполезно, потому что плюсы падают при невалидном вводе.
