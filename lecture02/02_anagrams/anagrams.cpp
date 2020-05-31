// anagrams.cpp

#include <iostream>
#include <vector>

using namespace std;

// Constants

const size_t NLETTERS = 26;

// Functions

bool is_anagram(string &s, string &t) {
    size_t sc[NLETTERS] = {0};
    size_t tc[NLETTERS] = {0};

    for (auto c : s) { sc[tolower(c) - 'a']++; }
    for (auto c : t) { tc[tolower(c) - 'a']++; }

    for (size_t i = 0; i < NLETTERS; i++) {
    	if (sc[i] != tc[i]) {
    	    return false;
	}
    }

    return true;
}

// Main execution

int main(int argc, char *argv[]) {
    string first, second;

    while (cin >> first >> second) {
    	cout << (is_anagram(first, second) ? "Anagram" : "Not Anagram") << endl;
    }

    return 0;
}
