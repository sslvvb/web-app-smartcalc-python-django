# import ctypes

# # Load the dynamic library
# example_lib = ctypes.CDLL('./cpp_dynamic_lib/example.so')

# # Define the function prototype for the C++ function
# example_function = example_lib.GetResult
# example_function.argtypes = [ctypes.]  # Argument types
# example_function.restype = ctypes.c_int     # Return type

# # Call the C++ function
# result = example_function(42)
# print("Result:", result)


# import ctypes

# # Load the dynamic library
# model_lib = ctypes.CDLL('./cpp_dynamic_lib/example.so')

# # Define the function prototypes
# model_lib.GetResult.argtypes = [ctypes.c_char_p]
# model_lib.GetResult.restype = ctypes.c_double

# model_lib.GetResult.argtypes = [ctypes.c_char_p, ctypes.c_double]
# model_lib.GetResult.restype = ctypes.c_double

# # Call the functions from the dynamic library
# result = model_lib.GetResult(b"2+2")
# print("Result:", result)

# result_with_x = model_lib.GetResult(b"2*x", 5.0)
# print("Result with x:", result_with_x)


import ctypes

# Load the dynamic library
model_lib = ctypes.CDLL(
    '/opt/goinfre/hjerilyn/projects/python_calc_4/my_github_calc_web/project/smartcalc/model/model.so')
# model_lib = ctypes.cdll.LoadLibrary('/opt/goinfre/hjerilyn/projects/python_calc_4/my_github_calc_web/project/smartcalc/model/model.so')

example_function = model_lib.tmp
model_lib.tmp.argtypes = [ctypes.c_int]
model_lib.tmp.restype = ctypes.c_int

# Call the C++ function
result = model_lib.tmp(42)
print("Result:", result)

example_function = model_lib.GetResult
model_lib.GetResult.argtypes = [ctypes.c_wchar_p]
model_lib.GetResult.restype = ctypes.c_double

str = "32-4"
result = model_lib.GetResult(str)
print("Result:", result)
