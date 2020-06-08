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
    int sum = accumulate(s.begin(), s.end(), 0);
    
    // Base: subset sums up to target, so display it
    if (sum == target) {
    	stringstream ss;
    	ss << s[0];
    	for (size_t i = 1; i < s.size(); i++) {
    	    ss << "+" << s[i];
	}
	r.insert(ss.str());
	return;
    }

    // Base: prune search when index is size of candidates or when subset sum
    // is greater than target
    if (k == c.size() || sum > target) {
    	return;
    }

    // Recursion: try without current number and then with it 
    sumitup(s, c, k + 1, target, r);

    s.push_back(c[k]);
    sumitup(s, c, k + 1, target, r);
    s.pop_back();
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
