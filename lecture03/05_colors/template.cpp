// sort_colors.cpp

#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

// Functions

vector<int> read_colors(string &s) {
    vector<int>  colors = {0, 0, 0};

    // TODO: read and count colors
    return colors;
}

// Main execution

int main(int argc, char *argv[]) {
    string line;

    while (getline(cin, line)) {
    	auto colors = read_colors(line);
    	// TODO: print colors
    }

    return 0;
}
