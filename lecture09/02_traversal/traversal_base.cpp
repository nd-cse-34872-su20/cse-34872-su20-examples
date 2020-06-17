// traversal.cpp

#include <iostream>
#include <queue>
#include <stack>
#include <string>
#include <vector>

using namespace std;

// Node structure

template <typename T>
struct Node {
    T	  value;
    Node *left;
    Node *right;
};

// Pre-defined Trees

Node<char> *AlgorithmTree() {
    return new Node<char>{'A',
    	new Node<char>{'L',
	    new Node<char>{'O',
		new Node<char>{'H', nullptr, nullptr},
		new Node<char>{'M', nullptr, nullptr}
	    },
	    new Node<char>{'R', nullptr, nullptr}
	},
	new Node<char>{'G',
	    new Node<char>{'I', nullptr, nullptr},
	    new Node<char>{'T', nullptr, nullptr}
	}
    };
}

Node <char> *WikipediaTree() {
    return new Node<char>{'F',
    	new Node<char>{'B',
	    new Node<char>{'A', nullptr, nullptr},
	    new Node<char>{'D',
		new Node<char>{'C', nullptr, nullptr},
		new Node<char>{'E', nullptr, nullptr}
	    }
	},
	new Node<char>{'G',
	    nullptr,
	    new Node<char>{'I', 
		new Node<char>{'H', nullptr, nullptr},
	    	nullptr
	    }
	}
    };
}

Node <char> *Reading02Tree() {
    return new Node<char>{'W',
    	new Node<char>{'Y',
	    new Node<char>{'D',
		new Node<char>{'F', nullptr, nullptr},
		new Node<char>{'U', nullptr, nullptr}
	    },
	    new Node<char>{'B',
		new Node<char>{'L', nullptr, nullptr},
		new Node<char>{'A', nullptr, nullptr}
	    }
	},
	new Node<char>{'R',
	    new Node<char>{'I',
		new Node<char>{'R', nullptr, nullptr},
		new Node<char>{'A', nullptr, nullptr}
	    },
	    new Node<char>{'O',
		new Node<char>{'E', nullptr, nullptr},
		new Node<char>{'D', nullptr, nullptr}
	    }
	}
    };
}

// Traversal: BFS

template <typename T>
void bfs(Node<T> *root) {
}

// Traversal: DFS

template <typename T>
void dfs(Node<T> *root) {
}

// Traversal: DFS (Recursive)

template <typename T>
void dfs_recursive(Node<T> *root) {
}

// Main execution

int main(int argc, char *argv[]) {
    auto tree = AlgorithmTree();
    //auto tree = WikipediaTree();
    //auto tree = Reading02Tree();

    cout << "BFS: "; bfs(tree);
    cout << "DFS: "; dfs(tree);
    cout << "DFS: "; dfs_recursive(tree); cout << endl;

    return 0;
}
