#!/usr/bin/env python3

import collections
import sys

# Classes

class Node(object):
    ''' Binary tree Node '''
    def __init__(self, value, left, right):
        self.value = value
        self.left  = left
        self.right = right

    def __str__(self):
        return 'Node({}, {}, {})'.format(self.value, self.left, self.right)

# Functions

def bst_insert(node, value):
    # Base: node doesn't exist, so return a new one
    if not node:
        return Node(value, None, None)

    # Recursive: insert left if value is less than or equal to current Node,
    # otherwise insert right
    if value <= node.value:
        node.left  = bst_insert(node.left, value)
    else:
        node.right = bst_insert(node.right, value)

    return node

def is_balanced(root, height=0):
    ''' Use divide and conquer to determine if a binary tree is balanced '''
    # Base: reached non-existent node, so return current height and that it is
    # balanced
    if not root:
        return True, height

    # Divide and conquer: recursively compute height of left and right
    # sub-trees and if they are balanced
    left_balanced , left_height  = is_balanced(root.left)
    right_balanced, right_height = is_balanced(root.right)

    # Combine: compute height and whether or not the overall tree is balanced
    balanced = (left_balanced and right_balanced) and abs(left_height - right_height) <= 1
    height   = max(left_height, right_height) + 1
    return balanced, height

# Main Execution

def main():
    for line in sys.stdin:
        # Construct BST
        root = None
        for value in map(int, line.split()):
            root = bst_insert(root, value)

        # Determine if BST is balanced
        balanced, height = is_balanced(root)
        print('Balanced' if balanced else 'Unbalanced')

if __name__ == '__main__':
    main()
