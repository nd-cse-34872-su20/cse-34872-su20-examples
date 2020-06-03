// pbbmatched.cpp

#include <iomanip>
#include <iostream>
#include <stack>
#include <string>

using namespace std;

// Functions

bool is_pbbmatched(const string &s) {
    // TODO: Process string s using a stack to determine if the symbols are balanced
    return false;
}

// Main execution

int main(int argc, char *argv[]) {
    string line;

    while (getline(cin, line)) {
    	cout << setw(10) << line << ": "<< (is_pbbmatched(line) ? "Yes" : "No") << endl;
    }

    return 0;
}
