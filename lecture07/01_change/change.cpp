// change.cpp

#include <iostream>
#include <vector>

using namespace std;

// Constants

vector<int> COINS = {25, 10, 5, 1};

// Functions

vector<int> make_change(int target) {
    vector<int> change;

    for (auto coin : COINS) {
    	while (target >= coin) {
    	    change.push_back(coin);
    	    target -= coin;
	}
    }

    return change;
}

// Main execution

int main(int argc, char *argv[]) {
    int target;

    while (cin >> target) {
    	auto coins = make_change(target);
    	if (!coins.empty()) {
	    cout << coins[0];
	    for (size_t i = 1; i < coins.size(); i++) {
	    	cout << " + " << coins[i];
	    }
	    cout << endl;
	}
    }
}
