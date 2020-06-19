#!/usr/bin/env python3

import collections
import heapq
import sys

# Build Graph

def read_graph():
    ''' Read in undirected graph ''' 
    g = collections.defaultdict(dict)
    for line in sys.stdin:
        source, target, weight = line.split()
        g[source][target] = int(weight)
        g[target][source] = int(weight)
    return g

# Compute MST

def compute_mst(g):
    ''' Use Prim's algorithm to compute the minimum spanning tree '''
    frontier = []
    visited  = {}
    start    = list(g.keys())[0]

    heapq.heappush(frontier, (0, start, start))

    while frontier:
        weight, source, target = heapq.heappop(frontier)

        if target in visited:
            continue

        visited[target] = source

        for neighbor, cost in g[target].items():
            heapq.heappush(frontier, (cost, target, neighbor))

    return visited

# Main Execution

def main():
    # Read graph
    g = read_graph()

    # Compute MST
    m = compute_mst(g)
    e = sorted((min(s, t), max(s, t)) for s, t in m.items() if s != t)

    # Display total MST weight and edges in MST
    print(sum(g[s][t] for s, t in e))
    for s, t in e:
        print(s, t)

if __name__ == '__main__':
    main()
