// subsets.cpp

#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

// Functions

void subsets(vector<int> &s, vector<int> &d, size_t k, size_t &count) {
    if (k == d.size()) { // Base: have complete subset
    	auto sum = accumulate(s.begin(), s.end(), 0);
    	count   += (sum % 3 == 0 ? 1 : 0);

    	// for (auto e : s) { cout << " " << e; }; cout << endl;
    	return;
    }

    // Recurse: skip current
    subsets(s, d, k + 1, count);
    // Recurse: with current
    s.push_back(d[k]);
    subsets(s, d, k + 1, count);
    s.pop_back(); // Reset subset
}

// Main execution

int main(int argc, char *argv[]) {
    vector<int> numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    size_t      count   = 0;
    vector<int> subset;

    subsets(subset, numbers, 0, count);
    cout << count << endl;
    return 0;
}
