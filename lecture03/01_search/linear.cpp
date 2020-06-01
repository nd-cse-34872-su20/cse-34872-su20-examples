// linear.cpp

#include <algorithm>
#include <iomanip>
#include <iostream>
#include <vector>

using namespace std;

bool linear_search(vector<int> &v, int target) {
    return find(v.begin(), v.end(), target) != v.end();
}

int linear_search_index(vector<int> &v, int target) {
    auto it = find(v.begin(), v.end(), target);
    return (it != v.end() ? it - v.begin() : -1);
}

int main(int argc, char *argv[]) {
    vector<int> v = {1, 3, 6, 8, 9};

    for (int i = 0; i < 10; i++) {
    	cout << i << " " << boolalpha << linear_search(v, i) << endl;
    	cout << i << " "              << linear_search_index(v, i) << endl;
    }

    return 0;
}
