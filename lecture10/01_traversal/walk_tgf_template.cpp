// walk_tgf.cpp: read TGF and walk it

#include <iostream>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <sstream>
#include <unordered_map>

using namespace std;

// WalkType Constants

typedef enum {
    DFS_REC,
    DFS_ITER,
    BFS_ITER,
} WalkType;

// Graph structure

struct Graph {
    unordered_map<int, string>	    labels;
    unordered_map<int, set<int>>    edges;
};

// Load graph from standard input

void load_graph(Graph &g) {
    // Read labels (vertices)

    // Read edges (vertices)
}

// Depth-First-Search (recursive)

void walk_graph_dfs_rec(Graph &g, int v, set<int> &marked) {
    // TODO
}

// Depth-First-Search (iterative)

void walk_graph_dfs_iter(Graph &g, int v) {
    // TODO
}

// Breadth-First-Search (iterative)

void walk_graph_bfs_iter(Graph &g, int v) {
    // TODO
}

// Walk graph dispatch function

void walk_graph(Graph &g, int root, WalkType w) {
    set<int> marked;

    switch (w) {
        case DFS_REC:
            walk_graph_dfs_rec(g, root, marked);
            break;
        case DFS_ITER:
            walk_graph_dfs_iter(g, root);
            break;
        case BFS_ITER:
            walk_graph_bfs_iter(g, root);
            break;
        default:
            cerr << "Unknown WalkType: " << w << endl;
            break;
    }
}


// Main execution

int main(int argc, char *argv[]) {
    Graph g;

    if (argc != 3) {
        cerr << "Usage: " << argv[0] << " root [0 = DFS_REC | 1 = DFS_ITER | 2 = BFS_ITER]" << endl;
        return EXIT_FAILURE;
    }

    int root = atoi(argv[1]);
    int walk = atoi(argv[2]);

    load_graph(g);
    walk_graph(g, root, static_cast<WalkType>(walk));

    return EXIT_SUCCESS;
}
