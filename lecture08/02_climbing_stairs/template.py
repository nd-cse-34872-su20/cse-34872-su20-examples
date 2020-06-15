#!/usr/bin/env python3

import sys

# Functions

def count_steps(n, cache={}):
    # TODO: Determine number of distinct ways to climb n steps using only
    # increments of 1 or 2 steps at a time.
    return 0

def main():
    for n in map(int, sys.stdin):
        print(count_steps(n))

# Main Executio

if __name__ == '__main__':
    main()

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
