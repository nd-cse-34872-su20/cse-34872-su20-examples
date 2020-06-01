CC=            	gcc
CFLAGS=       	-g -std=gnu99 -Wall
CXX=            g++
CXXFLAGS=       -g -std=gnu++11 -Wall

C_SOURCE=       $(wildcard *.c)
CXX_SOURCE=     $(wildcard *.cpp)
PROGRAMS=       $(C_SOURCE:.c=) $(CXX_SOURCE:.cpp=)

all:    $(PROGRAMS)

%:      %.c
	$(CC) $(CFLAGS) -o $@  $^

%:      %.cpp
	$(CXX) $(CXXFLAGS) -o $@  $^

clean:
	rm -f $(PROGRAMS)

.PHONY: all clean
