// perfect_square.cpp: Perfect Square

#include <iostream>

using namespace std;

bool is_perfect_square(long n) {
    // TODO: Use binary search to determine if n is a perfect valid square.
    return false;
}

int main(int argc, char *argv[]) {
    long n;

    while (cin >> n) {
    	cout << (is_perfect_square(n) ? "Yes" : "No") << endl;
    }

    return 0;
}
