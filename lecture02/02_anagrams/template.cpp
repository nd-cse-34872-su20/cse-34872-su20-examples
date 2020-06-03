// anagrams.cpp

#include <iostream>
#include <vector>

using namespace std;

// Constants

const size_t NLETTERS = 26;

// Functions

bool is_anagram(string &s, string &t) {
    // TODO: Return whether or not s and t are anagrams
    return false;
}

// Main execution

int main(int argc, char *argv[]) {
    string first, second;

    while (cin >> first >> second) {
    	cout << (is_anagram(first, second) ? "Anagram" : "Not Anagram") << endl;
    }

    return 0;
}
