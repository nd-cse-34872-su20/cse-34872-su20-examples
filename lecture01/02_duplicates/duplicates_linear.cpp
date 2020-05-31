// duplicates_linear.cpp

#include <algorithm>
#include <climits>
#include <iostream>
#include <random>
#include <vector>

using namespace std;

// Constants

const int N = 1<<15;

// Functions

vector<int> generate_random_numbers(size_t n) {
    default_random_engine	    g;
    uniform_int_distribution<int>   d(1, INT_MAX);  // Demo: switch to N
    vector<int>			    v(n);

    for (size_t i = 0; i < n; i++) {
    	v[i] = d(g);
    }

    return v;
}

// Main execution

int main(int argc, char *argv[]) {
    vector<int> v = generate_random_numbers(N);

    // For each item in vector, perform a linear search to determine if
    // duplicate is contained in remainder of vector.
    for (auto it = v.begin(); it != v.end(); it++) {
    	if (find(it + 1, v.end(), *it) != v.end()) {
    	    cout << *it << " is duplicated" << endl;
    	    break;
	}
    }

    return 0;
}
