// lotto.cpp

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

// Functions

void combinations(vector<int> &s, vector<int> &d, size_t k) {
    // TODO: Base: have complete subset
    
    // TODO: Recurse: with current

    // TODO: Recurse: skip current
}

int read_numbers(vector<int> &v) {
    // Read line
    string line;
    if (!getline(cin, line)) {
    	return 0;
    }

    // Read k (first number)
    stringstream ss(line);
    size_t k;
    ss >> k;
    if (!k) {
    	return 0;
    }

    // Read numbers
    v.resize(k);
    for (size_t i = 0; i < k; i++) {
    	ss >> v[i];
    }

    return v.size();
}

// Main execution

int main(int argc, char *argv[]) {
    vector<int> numbers;

    for (size_t test_case = 0; read_numbers(numbers); test_case++) {
    	// TODO: Sort numbers

	// TODO: Handle blank space between test cases

	// TODO: Generate combinations recursively
    }

    return 0;
}
