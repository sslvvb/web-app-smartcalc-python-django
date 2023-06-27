"""Model class, wrapper for C++ kernel."""

import ctypes


# типы для всех переменных в питоне тоже везде добавить


class Calculator:
    def __init__(self) -> None:
        self.model_lib = ctypes.CDLL(  # TODO: путь сделать относительно проекта + мб в билд переложить ?
            # '/opt/goinfre/hjerilyn/projects/python_calc_4/my_github_calc_web/project/smartcalc/services/model.so')
            '/Users/sslvvb/Documents/S21/Projects/Python/python_calc_4/my_github_web_calc/project/smartcalc/services/model.so')

        # example_function = self.model_lib.GetResult
        self.model_lib.GetResult.argtypes = [ctypes.c_char_p]
        self.model_lib.GetResult.argtypes = [ctypes.c_double]
        self.model_lib.GetResult.restype = ctypes.c_double

    def calculate(self, expression) -> str:
        encode_string = expression.encode()
        # try:
        # позаботиться что строки придет чистая или внутри модели проверять ее чистоту
        result: float = self.model_lib.GetResult(encode_string)
        print(type(result))

        # except:
        #     return "ERROR from calculator.py"
        return str(result)

# if __name__ == "__main__":
#     calcs = Calculator()
#     calcs.calculate("3+4-12*4")
