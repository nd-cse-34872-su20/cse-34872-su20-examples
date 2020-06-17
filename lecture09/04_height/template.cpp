// height_tree.cpp

#include <iostream>
#include <memory>

using namespace std;

// Node structures

template <typename T>
struct Node {
    T value;
    struct Node *left;
    struct Node *right;
};

// Find height of tree

template <typename T>
size_t height_tree(Node<T> *root) {
    // TODO: Use divide and conquer to compute the height of binary tree
}

// Main execution

int main(int argc, char *argv[]) {
    Node<int> *root = new Node<int>{7,
    	new Node<int>{5,
    	    new Node<int>{3,
		new Node<int>{2, nullptr, nullptr},
		nullptr},
    	    nullptr
	},
    	new Node<int>{4,
    	    nullptr,
    	    new Node<int>{2, nullptr, nullptr}
	}
    };

    cout << height_tree(root) << endl;
    return 0;
}
