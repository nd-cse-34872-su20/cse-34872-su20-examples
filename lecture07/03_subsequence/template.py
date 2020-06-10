#!/usr/bin/env python3

import sys

# Functions

def is_subsequence(s, t):
    # TODO: determine if s is a subsequence of t

def main():
    for line in sys.stdin:
        s, t = map(list, line.split())
        print(is_subsequence(s, t))

# Main Execution

if __name__ == '__main__':
    main()
