// cheatsheet.cpp

#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
    vector<int> v = {1, 2, 3};	    // Create dynamic array

    v.push_back(4);		    // Append to back of array
    v.insert(v.begin(), 0);	    // Prepend to front of array

    cout << v.size() << endl;	    // Display number of elements
    for (auto e : v) {		    // Traverse elements
    	cout << e << endl;
    }
				    // Traverse elements with index
    for (size_t i = 0; i < v.size(); i++) {
	cout << i << ": " << v[i] << endl;
    }

    return 0;
}
