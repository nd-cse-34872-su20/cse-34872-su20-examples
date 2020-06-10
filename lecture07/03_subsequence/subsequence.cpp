// subsequence.cpp

#include <iostream>
#include <string>

using namespace std;

// Functions

bool is_subsequence(string &s, string &t) {
    size_t si = 0;
    for (size_t ti = 0; si < s.size() && ti < t.size(); ti++) {
    	if (s[si] == t[ti]) {
    	    si++;
	}
    }

    return si >= s.size();
}

// Main execution

int main(int argc, char *argv[]) {
    string s, t;

    while (cin >> s >> t) {
    	cout << (is_subsequence(s, t) ? "True" : "False") << endl;
    }

    return 0;
}
