// lotto.cpp

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

// Functions

void combinations(vector<int> &s, vector<int> &d, size_t k) {
    // Base: have complete subset
    if (k == d.size()) {
    	if (s.size() == 6) {
	    cout << s[0];
	    for (size_t i = 1; i < s.size(); i++) {
		cout << " " << s[i]; 
	    } 
	    cout << endl;
	}
    	return;
    }
    
    // Recurse: with current
    s.push_back(d[k]);
    combinations(s, d, k + 1);
    s.pop_back(); // Reset subset

    // Recurse: skip current
    combinations(s, d, k + 1);
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
	sort(numbers.begin(), numbers.end());

	// TODO: Handle blank space between test cases
	if (test_case) {
	    cout << endl;
	}

	// TODO: Generate combinations recursively
	vector<int> combination;
	combinations(combination, numbers, 0);
    }

    return 0;
}
