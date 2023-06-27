.PHONY: compile_arm64

rebuild:
	g++ -shared -o model.so cpp_dynamic_lib/model.cpp cpp_dynamic_lib/wrapper.cpp
	python3 calculator.py

run:
	python3 calculator.py

compile_arm64:
    g++-12 -arch arm64 -shared -o model.so cpp_dynamic_lib/model.cpp cpp_dynamic_lib/wrapper.cpp
