// names.cpp: Sort by multiple factors

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Name {
    string  first_name;
    string  last_name;
};

int main(int argc, char *argv[]) {
    vector<Name> names;
    Name	 name;

    while (cin >> name.first_name >> name.last_name) {
    	names.push_back(name);
    }
    
    /*
    stable_sort(names.begin(), names.end(), [](const Name &a, const Name &b) {
    	return a.first_name < b.first_name;
    });
    stable_sort(names.begin(), names.end(), [](const Name &a, const Name &b) {
    	return a.last_name < b.last_name;
    });
    */

    sort(names.begin(), names.end(), [](const Name &a, const Name &b) {
    	if (a.last_name == b.last_name)
	    return a.first_name < b.first_name;
	else
	    return a.last_name < b.last_name;
    });

    for (auto n : names) {
    	cout << n.first_name << " " << n.last_name << endl;
    }

    return 0;
}
