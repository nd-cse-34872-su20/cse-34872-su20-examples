#!/usr/bin/env python3

import collections

# Constants

INFINITY = float('inf')

# Structures

Node = collections.namedtuple('Node', 'value left right')

# Functions

def height_tree(root):
    ''' Use divide and conquer to compute the height of binary tree '''
    # Base case: Non-existent node
    if not root:
        return 0

    # Divide and conquer: recursively solve left and right sub-trees
    left_height  = height_tree(root.left)
    right_height = height_tree(root.right)

    # Combine: take max sub-tree height and add 1
    return max(left_height, right_height) + 1

# Main Execution

if __name__ == '__main__':
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
