// search.cpp

#include <algorithm>
#include <iomanip>
#include <iostream>
#include <vector>

using namespace std;

int binary_search_index(vector<int> &v, int target) {
    auto it = lower_bound(v.begin(), v.end(), target);
    return (it != v.end() && *it == target ? it - v.begin() : -1);
}

int main(int argc, char *argv[]) {
    vector<int> v = {1, 3, 6, 8, 9};

    for (int i = 0; i < 10; i++) {
    	cout << i << " " << boolalpha << binary_search(v.begin(), v.end(), i) << endl;
    	cout << i << " "              << binary_search_index(v, i) << endl;
    }

    return 0;
}
