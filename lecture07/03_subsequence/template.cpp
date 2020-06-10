// subsequence.cpp

#include <iostream>
#include <string>

using namespace std;

// Functions

bool is_subsequence(string &s, string &t) {
    // TODO: determine if s is a subsequence of t
}

// Main execution

int main(int argc, char *argv[]) {
    string s, t;

    while (cin >> s >> t) {
    	cout << (is_subsequence(s, t) ? "True" : "False") << endl;
    }

    return 0;
}
