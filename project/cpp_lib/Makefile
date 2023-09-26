CXX = g++
CXXFLAGS = -shared -o model.so -fPIC

SRC = model.cpp wrapper.cpp

all: dynamic_lib

dynamic_lib: $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC)

clean:
	rm -f *.so
