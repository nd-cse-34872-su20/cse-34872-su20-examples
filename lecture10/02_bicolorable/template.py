#!/usr/bin/env python3

import collections
import sys

# Constants

BLUE = 0
RED  = 1

# Read Graph

def read_graph(n, m):
    ''' Construct adjacency set '''
    g = {v: set() for v in range(n)}

    for _ in range(m):
        s, t = map(int, sys.stdin.readline().split())
        g[s].add(t)
        g[t].add(s)

    return g

# Determine if Bicolorable

def is_bicolorable(g):
    ''' Determines if graphis bicolorable by walking it recursively. '''
    return walk(g, list(g.keys())[0], BLUE, {})

def walk(g, n, color, visited):
    ''' Recursively walk graph and verifying that the node has the appropriate
    color. '''

    # We have already visited this node, so verify we still have the same
    # color.

    # We have not visited this node yet, so store its color.

    # Visit each neighbor recursively with the alternate color and check that
    # they are colorable.

    return True

def walk(g, n, color, visited):
    ''' Iteratively walk graph and verifying that the node has the appropriate
    color. '''
    # Establish frontier with initial node and color

    # While there are still nodes in the frontier...

        # Pop one node from frontier

        # Check if it has been visited

        # Mark that it has been visited

        # Add neighbors to frontier

    return True

# Main execution

def main():
    n, m = map(int, sys.stdin.readline().split())
    while n and m:
        g = read_graph(n, m)
        if is_bicolorable(g):
            print('BICOLORABLE')
        else:
            print('NOT BICOLORABLE')

        n, m = map(int, sys.stdin.readline().split())

if __name__ == '__main__':
    main()

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
