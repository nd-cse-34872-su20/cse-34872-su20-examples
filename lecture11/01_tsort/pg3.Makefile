CXX=g++
CC=gcc
CXXFLAGS=-std=c++11

all: test1 test2a test2b measure

distance.o: distance.cpp distance.hpp
	test1.o: test1.cpp bintree.hpp
test2a.o: test2a.cpp quadtree.hpp
	test2b.o: test2b.cpp quadtree.hpp

test1: test1.o distance.o
	    $(CXX) $(CXXFLAGS) $^ -o $@
test2a: test2a.o distance.o
	    $(CXX) $(CXXFLAGS) $^ -o $@
test2b: test2b.o distance.o
	    $(CXX) $(CXXFLAGS) $^ -o $@

measure: measure.c
	    $(CC) $< -o $@
clean:
	    rm -rf test1 test2a test2b measure *.exe *.o *.dSYM gmon.out *~
