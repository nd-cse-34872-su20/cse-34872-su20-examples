#!/usr/bin/env python3

import sys

# Classes

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left  = left
        self.right = right

    def __str__(self):
        return f'Node({self.value},{self.left},{self.right})'

class Tree(object):
    def __init__(self):
        pass

    def search(self, value):
        pass

    def search_r(self, node, value):
        pass

    def insert(self, value):
        pass

    def insert_r(self, node, value):
        pass

    def print(self):
        pass

    def print_r(self, node):
        pass

    def nodes(self):
        pass

    def nodes_r(self, node):
        pass

# Main Execution

def main():
    tree = Tree()
    for number in map(int, sys.argv[1:]):
        tree.insert(number)

    for number in map(int, sys.argv[1:]):
        print(number, tree.search(number))
        print(2*number, tree.search(number*2))

    tree.print()
    print(', '.join(map(str, tree.nodes())))

if __name__ == '__main__':
    main()
