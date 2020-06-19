#!/usr/bin/env python3

import collections
import heapq
import sys

# Build Graph

def read_graph():
    ''' Read in undirected graph ''' 
    g = collections.defaultdict(dict)
    return g

# Compute MST

def compute_mst(g):
    ''' Use Prim's algorithm to compute the minimum spanning tree '''
    frontier = []
    visited  = {}
    return visited

# Main Execution

def main():
    # Read graph
    g = read_graph()

    # Compute MST
    m = compute_mst(g)
    e = sorted((min(s, t), max(s, t)) for s, t in m.items() if s != t)

    # TODO: Display total MST weight and edges in MST

if __name__ == '__main__':
    main()
