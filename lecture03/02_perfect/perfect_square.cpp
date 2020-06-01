// perfect_square.cpp: Perfect Square

#include <iostream>

using namespace std;

bool is_perfect_square(long n) {
    long low  = 1;
    long high = n;

    while (low <= high) {
        long middle = (low + high) / 2;
        long square = middle * middle;

        if (square == n)
            return true;

        if (middle * middle > n)
            high = middle - 1;
	else
            low  = middle + 1;
    }

    return false;
}

/* linear search
bool is_perfect_square(long n) {
    for (long i = 0; i < n; i++)
    	if (i*i == n)
    	    return true;
    return false;
}
*/

int main(int argc, char *argv[]) {
    long n;

    while (cin >> n) {
    	cout << (is_perfect_square(n) ? "Yes" : "No") << endl;
    }

    return 0;
}
