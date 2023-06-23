

dynamic_lib:
	g++ -std=c++17 -shared -fPIC -o model/libcalculator.dylib model/model_c_plus_plus/model.cpp model/model_c_plus_plus/wrapper.cpp
	g++ -shared -o model.so cpp_dynamic_lib/model.cpp cpp_dynamic_lib/wrapper.cpp
	python3 calculator.py
