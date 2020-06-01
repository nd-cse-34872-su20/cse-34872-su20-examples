// palindromic.cpp

#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

// Functions

bool is_palindromic(string &s) {
    // TODO: Determine if string s contains a palindromic permutation
    return false;
}

// Main execution

int main(int argc, char *argv[]) {
    string word;

    while (cin >> word) {
    	cout << (is_palindromic(word) ? "Yes" : "No") << endl;
    }

    return 0;
}
