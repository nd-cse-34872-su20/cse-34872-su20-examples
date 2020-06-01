// sort_colors.cpp

#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

// Functions

vector<int> read_colors(string &s) {
    vector<int>  colors = {0, 0, 0};
    stringstream ss(s);
    int          color;

    while (ss >> color) {
    	colors[color]++;
    }

    return colors;
}

// Main execution

int main(int argc, char *argv[]) {
    string line;

    while (getline(cin, line)) {
    	auto colors = read_colors(line);
    	bool first  = true;
    	for (size_t i = 0; i < colors.size(); i++) {
    	    for (int c = 0; c < colors[i]; c++) {
    	    	cout << (first ? "" : " ") << i;
    	    	first = false;
	    }
	}
	cout << endl;
    }

    return 0;
}
