// largest_number.cpp

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

// Functions

bool read_numbers(vector<string> &numbers) {
    numbers.clear();

    string line;
    if (getline(cin, line)) {
    	stringstream ss(line);
    	string n;
    	while (ss >> n) {
    	    numbers.push_back(n);
	}
    }

    return numbers.size();
}

// Main Execution

int main(int argc, char *argv[]) {
    vector<string> numbers;

    // TODO: Read numbers, sort, and print

    return 0;
}
