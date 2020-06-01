// palindromic.cpp

#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

// Functions

bool is_palindromic(string &s) {
    unordered_set<char> seen;

    // History approach: keep track of whether or not we have seen this
    // character before.
    for (auto c : s) {
    	if (seen.count(c)) {
    	    seen.erase(c);
	} else {
	    seen.insert(c);
	}
    }

    return seen.size() <= 1;
}

// Main execution

int main(int argc, char *argv[]) {
    string word;

    while (cin >> word) {
    	cout << (is_palindromic(word) ? "Yes" : "No") << endl;
    }

    return 0;
}
