// happy_number.cpp

#include <iostream>
#include <numeric>
#include <unordered_map>
#include <unordered_set>

using namespace std;

// Global variables

// Functions

bool is_happy_r(int n, unordered_set<int> &seen) {
    // TODO: Determine if n is a happy number (recursively)
    return false;
}

bool is_happy(int n) {
    // TODO: Determine if n is a happy number
    return false;
}

// Main execution

int main(int argc, char *argv[]) {
    int n;

    while (cin >> n) {
    	cout << (is_happy(n) ? "Yes" : "No") << endl;
    }

    return 0;
}
