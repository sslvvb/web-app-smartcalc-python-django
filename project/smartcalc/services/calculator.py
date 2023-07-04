"""Model class, wrapper for C++ kernel."""

import ctypes


# мб избавлюсь от класса если он не понадобится для графика ?
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

    def graph_calculate(self, expression: str, x_min: str, x_max: str) -> list:
        # валидацию х мин х мах и всех условий добавить
        # у каждой функции только одна причина для изменений

        number_of_steps: int = 10  # 100000

        self.model_lib.GetResultForGraph.argtypes = [ctypes.c_char_p, ctypes.c_double, ctypes.c_double, ctypes.c_int,
                                                     ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
        x_values_buffer = (ctypes.c_double * number_of_steps)()
        y_values_buffer = (ctypes.c_double * number_of_steps)()

        x_buf_ptr: LP_c_double = ctypes.cast(x_values_buffer, ctypes.POINTER(ctypes.c_double))
        y_buf_ptr: LP_c_double = ctypes.cast(y_values_buffer, ctypes.POINTER(ctypes.c_double))

        self.model_lib.GetResultForGraph(expression.encode(), float(x_min), float(x_max), number_of_steps, x_buf_ptr,
                                         y_buf_ptr)

        x_result_list: list = [x_buf_ptr[i] for i in range(number_of_steps)]
        y_result_list: list = [y_buf_ptr[i] for i in range(number_of_steps)]

        return [x_result_list, y_result_list]
