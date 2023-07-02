"""Model class, wrapper for C++ kernel."""

import ctypes

# Define the C++ function prototype
graph_calculate_func = ctypes.CFUNCTYPE(
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_char_p,
    ctypes.c_double,
    ctypes.c_double
)


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

    def graph_calculate(self, expression: str, x_min: str, x_max: str):
        self.model_lib.GetResultForGraph.argtypes = [ctypes.c_char_p, ctypes.c_double, ctypes.c_double]
        self.model_lib.GetResultForGraph.restype = ctypes.POINTER(ctypes.c_double)
        print("we are here")
        return 313

        # # try:
        # result_ptr = self.model_lib.GetResultForGraph(
        #     expression.encode(),
        #     float(x_min),
        #     float(x_max)
        # )
        #
        # result_list = self.convert_result(result_ptr)
        #
        # # result = self.model_lib.GetResultForGraph(expression.encode(), float(x_min), float(x_max))
        #
        # # result_list = convert_result(result)
        #
        # print("calculator.py")
        # print(result_list)
        # print(type(result_list))
        # return result_list
        # # except Exception as e:
        # #     return f"EXCEPTION ERROR FROM calculator.py: {str(e)}"

    # Define a helper function to convert the result to Python lists
    def convert_result(result):
        # Extract the underlying C array from the pointer
        array = ctypes.cast(result, ctypes.POINTER(ctypes.c_double))

        # Determine the length of the array
        length = 0
        while array[length] != 0.0:
            length += 1

        # Convert the array to a Python list
        result_list = [array[i] for i in range(length)]

        # Free the C array
        # self.model_lib.FreeResult(result)

        return result_list


# def graph_calculate(expression: str, x_min: str, x_max: str):
#     # Call the C++ function
#     result_ptr = model_lib.GetResultForGraph(
#         expression.encode(),
#         float(x_min),
#         float(x_max)
#     )
#
#     # Convert the result to Python lists
#     result_list = convert_result(result_ptr)
#
#     return result_list
