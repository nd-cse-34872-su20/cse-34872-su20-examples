// sumitup.cpp

#include <algorithm>
#include <iostream>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

// Functions

int read_input(vector<int> &numbers) {
    int target, n;

    if (cin >> target >> n && !target) {
    	return target;
    }

    numbers.resize(n);
    for (int i = 0; i < n; i++) {
    	cin >> numbers[i];
    }

    sort(numbers.rbegin(), numbers.rend());
    return target;
}

void sumitup(vector<int> s, vector<int> &c, size_t k, int target, set<string> &r) {
    // TODO Base: Subset sums up to target, so display it

    // TODO Base: Prune search when index is size of candidates or when subset
    // sum is greater than target

    // TODO Recurse: Try without current number and then with it 
}

// Main execution

int main(int argc, char *argv[]) {
    int         target;
    vector<int> numbers, subset;

    while ((target = read_input(numbers))) {
        set<string> results;
    	sumitup(subset, numbers, 0, target, results);

    	cout << "Sums of " << target << ":" << endl;
    	if (results.empty()) {
    	    cout << "NONE" << endl;
	} else {
	    for (auto it = results.rbegin(); it != results.rend(); it++) {
	    	cout << *it << endl;
	    }
	}
    }
}
