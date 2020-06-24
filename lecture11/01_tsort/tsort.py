#!/usr/bin/env python3

import collections
import sys

# Graph Structure

Graph = collections.namedtuple('Graph', 'edges degrees')

# Read Graph

def read_graph():
    edges   = collections.defaultdict(set)
    degrees = collections.defaultdict(int)

    for line in sys.stdin:
        if ':' not in line:
            continue

        targets, sources = line.split(':', 1)
        targets = targets.split()
        sources = sources.split()

        for target in targets:
            for source in sources:
                edges[source].add(target)
                degrees[target] += 1
                degrees[source]

    return Graph(edges, degrees)

# Topological Sort

def topological_sort(graph):
    frontier = [v for v, d in graph.degrees.items() if d == 0]
    visited  = []

    while frontier:
        vertex = frontier.pop()
        visited.append(vertex)

        for neighbor in graph.edges[vertex]:
            graph.degrees[neighbor] -= 1
            if graph.degrees[neighbor] == 0:
                frontier.append(neighbor)

    return visited

# Main Execution
    
def main():
    graph    = read_graph()
    vertices = topological_sort(graph)

    if len(vertices) == len(graph.degrees):
        print(' '.join(vertices))
    else:
        print('There is a cycle!')

if __name__ == '__main__':
    main()
