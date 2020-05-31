// duplicates_set.cpp

#include <algorithm>
#include <climits>
#include <iostream>
#include <random>
#include <set>
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

    // For each item in vector, check if it is in our set (and thus is a
    // duplicate).
    set<int> s;
    for (auto i : v) {
    	if (s.find(i) != s.end()) {
    	    cout << i << " is duplicated" << endl;
    	    break;
	}
	s.insert(i);
    }

    return 0;
}
