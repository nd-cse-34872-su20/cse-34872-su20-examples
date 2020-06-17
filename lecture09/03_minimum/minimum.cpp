// minimum_tree.cpp

#include <iostream>
#include <memory>

using namespace std;

// Node structures

template <typename T>
struct Node {
    T     value;
    Node *left;
    Node *right;
};

// Find minimum of tree

template <typename T>
T minimum_tree(Node<T> *root) {
    T minimum = root->value;

    if (root->left) {
    	minimum = min(minimum, minimum_tree(root->left));
    }

    if (root->right) {
    	minimum = min(minimum, minimum_tree(root->right));
    }

    return minimum;
}

// Main execution

int main(int argc, char *argv[]) {
    Node<int> *root = new Node<int>{7,
    	new Node<int>{5,
    	    new Node<int>{3, nullptr, nullptr},
    	    nullptr
	},
    	new Node<int>{4,
    	    nullptr,
    	    new Node<int>{2, nullptr, nullptr}
	}
    };

    cout << minimum_tree(root) << endl;
    return 0;
}
