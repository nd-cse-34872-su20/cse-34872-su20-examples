// permutations_backtracking.cpp

#include <algorithm>
#include <iostream>
#include <set>
#include <string>

using namespace std;

// Functions

void permutations(string &p, set<char> &c) {
    // Base: Used all candidates, so print permutation
    if (c.empty()) {
	for (auto c : p) { cout << c; }; cout << endl;
    	return;
    }

    // Recurse: For each candidate, build a permutation with and without it
    for (auto e : c) {
    	// Place element into permutation and remove from candidates
    	p.push_back(e);
    	c.erase(e);

	// Recurse on subset (which is now one item shorter and no longer
	// includes the previously placed element as a character)
    	permutations(p, c);

	// Add element back to candidates and remove from permutation
    	c.insert(e);
    	p.pop_back();
    }
}

// Main execution

int main(int argc, char *argv[]) {
    string    p = "";
    set<char> c = {'A', 'B', 'C'};

    permutations(p, c);
    return 0;
}
