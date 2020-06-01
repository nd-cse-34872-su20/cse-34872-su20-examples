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
    unordered_map<int, int> totals = {{0, 0}};
    int    cur_total  = 0;
    size_t max_length = 0;

    for (size_t i = 0; i < digits.size(); i++) {
    	cur_total += (digits[i] ? 1 : -1);

	if (totals.count(cur_total)) {
	    max_length = max(max_length, i - totals[cur_total] + 1);
	} else {
	    totals[cur_total] = i + 1; 
	}
    }

    return max_length;
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
