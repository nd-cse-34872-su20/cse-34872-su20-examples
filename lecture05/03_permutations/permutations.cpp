// permutations.cpp

#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

// Main execution

int main(int argc, char *argv[]) {
    string s = "ABC";

    sort(s.begin(), s.end());
    do {
    	cout << s << endl;
    } while (next_permutation(s.begin(), s.end()));

    return 0;
}
