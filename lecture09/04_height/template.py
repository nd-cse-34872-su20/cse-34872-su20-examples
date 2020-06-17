#!/usr/bin/env python3

import collections

# Constants

INFINITY = float('inf')

# Structures

Node = collections.namedtuple('Node', 'value left right')

# Functions

def height_tree(root):
    # TODO: Use divide and conquer to compute the height of binary tree

# Main Execution

def main():
    # Create tree
    root = Node(7,
        Node(5,
                Node(3, Node(6, None, None), None),
                None),
        Node(4,
                None,
                Node(2, None, None),
    ))

    # Compute height of tree
    print(height_tree (root))

if __name__ == '__main__':
    main()

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
