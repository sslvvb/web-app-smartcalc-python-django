"""Model class, wrapper for C++ kernel."""

import ctypes
import numpy as np

# Define the C++ function prototype
graph_calculate_func = ctypes.CFUNCTYPE(
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_char_p,
    ctypes.c_double,
    ctypes.c_double
)


def convert_to_list(pointer, length):
    array_type = ctypes.c_double * length
    array = array_type.from_address(ctypes.addressof(pointer.contents))
    return list(array)


# мб избавлюсь от класса если он не понадобится для графика ?
class Calculator:
    def __init__(self) -> None:
        self.model_lib = ctypes.CDLL(
            '/opt/goinfre/hjerilyn/projects/python_calc_4/my_github_calc_web/project/smartcalc/services/model.so')
        # '/Users/sslvvb/Documents/S21/Projects/Python/python_calc_4/my_github_web_calc/project/smartcalc/services'
        # '/model.so')  # относительный путь + мб в билд переложить ?

    def calculate(self, expression: str) -> str:
        self.model_lib.GetResult.argtypes = [ctypes.c_char_p]
        self.model_lib.GetResult.restype = ctypes.c_double
        try:
            return self.model_lib.GetResult(expression.encode())
        except Exception as e:
            return f"EXCEPTION ERROR FROM calculator.py: {str(e)}"
        # это все бесполезно, потому что плюсы падают при невалидном вводе.

    def graph_calculate(self, expression: str, x_min: str, x_max: str):
        # верну через double* переданные как параметры !
        print('here')
        self.model_lib.printString.argtypes = (ctypes.POINTER(ctypes.c_double), ctypes.c_size_t)
        # self.model_lib.printString.restype = ctypes.POINTER(ctypes.c_double)
        my_vector = [0.0] * 3
        self.model_lib.printString((ctypes.c_double * len(my_vector))(*my_vector), len(my_vector))
        print(my_vector)
        return 313
