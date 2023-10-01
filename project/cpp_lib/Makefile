CXX = g++
CXXFLAGS = -shared -o model.so -fPIC

SRC = model.cpp wrapper.cpp parser.cpp

all: dynamic_lib

dynamic_lib: $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC)

clean:
	rm -f *.so
