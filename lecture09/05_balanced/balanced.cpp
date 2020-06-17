// balanced.cpp

#include <iostream>
#include <memory>
#include <sstream>
#include <string>

using namespace std;

// Node structures

template <typename T>
struct Node {
    T     value;
    Node *left;
    Node *right;

    ~Node() { delete left; delete right; }
};

// BST class

template <typename T>
class BST {
private:
    Node<T> *root = nullptr;

    Node<T> *insert_r(Node<T> *n, T value) {
    	if (n == nullptr) {
    	    return new Node<T>{value, nullptr, nullptr};
	}

	if (value < n->value) {
	    n->left  = insert_r(n->left, value);
	} else {
	    n->right = insert_r(n->right, value);
	}

	return n;
    }

    bool is_balanced_r(Node<T> *n, long &height) const {
    	if (n == nullptr) {
    	    return true;
	}

	long lheight   = 0;
	bool lbalanced = is_balanced_r(n->left, lheight);
	long rheight   = 0;
	bool rbalanced = is_balanced_r(n->right, rheight);

	height = max(lheight, rheight) + 1;
	return (lbalanced && rbalanced) && (abs(lheight - rheight) <= 1);
    }

public:
    ~BST() { delete root; }

    void insert(T value) {
    	root = insert_r(root, value);
    }

    bool is_balanced() const {
    	long height = 0;
    	return is_balanced_r(root, height);
    }
};

// Main execution

int main(int argc, char *argv[]) {
    string line;

    while (getline(cin, line)) {
    	stringstream ss(line);
    	int value;
    	BST<int> t;

	while (ss >> value) {
	    t.insert(value);
	}

	cout << (t.is_balanced() ? "Balanced" : "Unbalanced") << endl;
    }

    return 0;
}
