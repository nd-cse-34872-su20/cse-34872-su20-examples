#!/usr/bin/env python3

import sys

# Functions

def count_steps(n, cache={}):
    if n <= 2:
        return n

    if n not in cache:
        cache[n] = (count_steps(n - 1, cache) +
                    count_steps(n - 2, cache))

    return cache[n]

def main():
    for n in map(int, sys.stdin):
        print(count_steps(n))

# Main Execution

if __name__ == '__main__':
    main()
