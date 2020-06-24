#!/usr/bin/env python3

import collections
import sys

# Graph Structure

Graph = collections.namedtuple('Graph', 'edges degrees')

# Read Graph

def read_graph():
    edges   = collections.defaultdict(set)
    degrees = collections.defaultdict(int)

    # TODO: Read Makefile from stdin

    return Graph(edges, degrees)

# Topological Sort

def topological_sort(graph):
    # TODO: Perform topological sort
    return []

# Main Execution

def main():
    graph    = read_graph()
    ordering = topological_sort(graph)

    # TODO: Check for cycle, otherwise display ordering

if __name__ == '__main__':
    main()
