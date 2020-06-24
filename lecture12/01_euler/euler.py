#!/usr/bin/env python3

import collections
import sys

# Read Graph

def read_graph():
    graph = collections.defaultdict(dict)

    for edge, line in enumerate(sys.stdin):
        s, t = map(int, line.split())
        graph[s][t] = edge
        graph[t][s] = edge

    return graph

# Find Circuit

def find_circuit(graph, start, vertex, visited, path):
    ''' Recursive DFS traversal '''
    # If we have returned to start, return path
    if path and start == vertex:
        return path

    # Visit each unvisited outgoing edge
    for neighbor in graph[vertex]:
        if graph[vertex][neighbor] in visited:
            continue

        # Mark visited
        visited.add(graph[vertex][neighbor])

        # Add to path
        path.append((vertex, neighbor))

        # Recurse
        if find_circuit(graph, start, neighbor, visited, path):
            return path

        # Remove from path
        path.pop(-1)

        # Unmark visited
        visited.remove(graph[vertex][neighbor])

    # No circuit found, so return nothing (should never happen!)
    return []

# Find Eulerian Circuit

def find_euler_circuit(graph):
    ''' Iteratively compute subcircuit until all edges have been travsrsed or
    no circuit is possible '''
    start    = list(graph.keys())[0] # Starting vertex
    visited  = set()                 # Visited edges (set of edge ordinals)
    circuit  = []                    # Eulerian circuit (list of edges)
    index    = 0                     # Where in circuit to insert subcircuit

    while start:
        # Find subcircuit and insert it after current component
        path    = find_circuit(graph, start, start, visited, [])
        circuit = circuit[0:index] + path + circuit[index:]

        # Check if any nodes in current circuit have an unused edge, if so, set
        # start so we search for subcircuit beginning at that vertex
        start = None
        for index, vertex in enumerate(source for source, target in circuit):
            for neighbor, edge in graph[vertex].items():
                if edge not in visited:
                    start = vertex
                    break

    return circuit

# Main Execution

def main():
    graph   = read_graph()
    circuit = find_euler_circuit(graph)

    for source, target in circuit:
        print(source, target)

if __name__ == '__main__':
    main()
