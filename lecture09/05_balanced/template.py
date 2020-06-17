#!/usr/bin/env python3

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
    # TODO: Use divide and conquer to determine if a binary tree is balanced

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

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
