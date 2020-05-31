// pbbmatched.cpp

#include <iomanip>
#include <iostream>
#include <stack>
#include <string>

using namespace std;

// Functions

bool is_pbbmatched(const string &s) {
    stack<char> left;

    for (auto c : s) {
	if (c == '(' || c == '[' || c == '{') {
	    left.push(c);
	} else {
	    if (left.empty()) {
	    	return false;
	    }

	    if ((c == ')' && left.top() != '(') ||
	        (c == ']' && left.top() != '[') ||
	        (c == '}' && left.top() != '{')) {
	        return false;
	    }

	    left.pop();
	}
    }

    return left.empty();
}

// Main execution

int main(int argc, char *argv[]) {
    string line;

    while (getline(cin, line)) {
    	cout << setw(10) << line << ": "<< (is_pbbmatched(line) ? "Yes" : "No") << endl;
    }

    return 0;
}
