// continuous_array.cpp

#include <iostream>
#include <string>
#include <sstream>
#include <unordered_map>
#include <vector>

using namespace std;

// Functions

vector<bool> read_digits(string &s) {
    vector<bool> digits;
    stringstream ss(s);
    int digit;

    while (ss >> digit) {
	digits.push_back(digit);
    }

    return digits;
}

int find_maximum_contiguous_array(vector<bool> &digits) {
    // TODO: find length of maximum contiguous array
    return 0;
}

// Main execution

int main(int argc, char *argv[]) {
    string line;
    while (getline(cin, line)) {
    	auto digits = read_digits(line);
    	auto length = find_maximum_contiguous_array(digits);
    	cout << length << endl;
    }

    return 0;
}
