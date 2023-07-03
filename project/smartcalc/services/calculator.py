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
        верну через double* переданные как параметры !

        # self.model_lib.printString.restype = ctypes.POINTER(ctypes.c_double)
        # result_ptr = self.model_lib.printString()
        # size = 3  # 1000 ?
        # vec = [result_ptr[i] for i in range(size)]
        # print(vec)

        self.model_lib.printString.restype = ctypes.py_object
        tuple_obj = self.model_lib.printString()  # Call the function to get the tuple
        vec1_ptr, vec2_ptr = tuple_obj  # Extract the size and pointers from the tuple
        size = 3
        vec1 = np.ctypeslib.as_array(vec1_ptr, shape=(size,))
        vec2 = np.ctypeslib.as_array(vec2_ptr, shape=(size,))
        print(vec1)
        print(vec2)

        # tuple_ptr = self.model_lib.printString()
        # tuple_obj = ctypes.cast(tuple_ptr, ctypes.py_object).value  # Convert the tuple pointer to a Python tuple
        # vec1_ptr, vec2_ptr = tuple_obj  # Convert the tuple elements into Python lists
        # size = 3  # 1000 ?
        # vec1 = [vec1_ptr[i] for i in range(size)]
        # vec2 = [vec2_ptr[i] for i in range(size)]
        # print(vec1)
        # print(vec2)
        return 313

    def tmp_bind(self):
        print("done")
        pass


if __name__ == '__main__':
    calc = Calculator()
    calc.tmp_bind()
