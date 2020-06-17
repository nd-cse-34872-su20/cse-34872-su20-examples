#!/usr/bin/env python3

import collections

# Constants

INFINITY = float('inf')

# Structures

Node = collections.namedtuple('Node', 'value left right')

# Functions

def minimum_tree(root):
    # TODO: Use divide and conquer to return the minimum value in the tree

# Main Execution

def main():
    # Create tree
    root = Node(7,
        Node(5,
                Node(3, None, None),
                None),
        Node(4,
                None,
                Node(2, None, None),
    ))

    # Compute minimum of tree
    print(minimum_tree(root))

if __name__ == '__main__':
    main()
