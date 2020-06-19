#!/usr/bin/env python3

import collections
import heapq
import sys

# Build Graph

def read_graph():
    ''' Read in undirected graph '''
    g = collections.defaultdict(dict)
    return g

# Compute SSSP

def compute_sssp(g, start):
    ''' Use Dijkstra's Algorithm to compute the single-source shortest path '''
    frontier = []
    visited  = {}

    return visited

def reconstruct_path(visited, source, target):
    ''' Reconstruct path from source to target '''
    path = []
    return reversed(path)

# Main Execution

def main():
    # Read Graph
    g = read_graph()

    # Compute SSSP
    s = list(g.keys())[0]
    v = compute_sssp(g, s)

    # Reconstruct Path
    for t in list(g.keys())[1:]:
        print('{} -> {} = {}'.format(s, t, ' '.join(reconstruct_path(v, s, t))))

if __name__ == '__main__':
    main()

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
