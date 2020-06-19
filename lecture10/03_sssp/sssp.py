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

# Compute SSSP

def compute_sssp(g, start):
    ''' Use Dijkstra's Algorithm to compute the single-source shortest path '''
    frontier = []
    visited  = {}

    heapq.heappush(frontier, (0, start, start))

    while frontier:
        weight, source, target = heapq.heappop(frontier)

        if target in visited:
            continue

        visited[target] = source

        for neighbor, cost in g[target].items():
            heapq.heappush(frontier, (weight + cost, target, neighbor))

    return visited

def reconstruct_path(visited, source, target):
    ''' Reconstruct path from source to target '''
    path = []
    curr = target

    while curr != source:
        path.append(curr)
        curr = visited[curr]

    path.append(source)
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
