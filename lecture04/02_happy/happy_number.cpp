// happy_number.cpp

#include <iostream>
#include <numeric>
#include <unordered_map>
#include <unordered_set>

using namespace std;

// Global variables

unordered_map<int, bool> IsHappy;

// Functions

bool is_happy_r(int n, unordered_set<int> &seen) {
    if (seen.count(n)) {	// Base case: cycles
    	return false;
    }
    
    if (n == 1) {		// Base case: reaches 1
    	return true;
    }

    seen.insert(n);		// Mark seen

    if (!IsHappy.count(n)) {	// Memoize recursive call
    	string s = to_string(n);
    	int squares = accumulate(s.begin(), s.end(), 0, [](int sum, char c) {
    	    int d = (c - '0');
    	    return sum + (d*d);
	});
	IsHappy[n]  = is_happy_r(squares, seen);
    }

    return IsHappy[n];
}

bool is_happy(int n) {
    unordered_set<int> seen;
    return is_happy_r(n, seen);
}

// Main execution

int main(int argc, char *argv[]) {
    int n;

    while (cin >> n) {
    	cout << (is_happy(n) ? "Yes" : "No") << endl;
    }

    return 0;
}
