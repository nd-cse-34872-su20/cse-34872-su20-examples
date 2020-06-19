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
    if n in visited:
        return visited[n] == color

    # We have not visited this node yet, so store its color.
    visited[n] = color

    # Visit each neighbor recursively with the alternate color and check that
    # they are colorable.
    for v in g[n]:
        if not walk(g, v, (color + 1) % 2, visited):
            return False

    return True

def walk(g, n, color, visited):
    ''' Iteratively walk graph and verifying that the node has the appropriate
    color. '''
    # Establish frontier with initial node and color
    frontier = [(n, color)]
    
    # While there are still nodes in the frontier...
    while frontier:
        # Pop one node from frontier
        v, c = frontier.pop()

        # Check if it has been visited
        if v in visited:
            if c != visited[v]:
                return False
            else:
                continue

        # Mark that it has been visited
        visited[v] = c

        # Add neighbors to frontier
        for u in g[v]:
            frontier.append((u, (c + 1) % 2))

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
