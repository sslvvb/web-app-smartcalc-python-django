
all: down build

build:
	docker-compose build
	docker-compose up

down:
	docker-compose down
	- docker rmi my_git_web_calc_web

logs:
	docker-compose logs -f

dynamic_lib:
	g++ -std=c++17 -shared -fPIC -o model/libcalculator.dylib model/model_c_plus_plus/model.cpp model/model_c_plus_plus/wrapper.cpp
	g++ -shared -o model.so cpp_dynamic_lib/model.cpp cpp_dynamic_lib/wrapper.cpp
	python3 calculator.py

clean:
	rm -f project/cpp_lib/model.so
