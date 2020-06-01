#!/usr/bin/env python3

# Perfect Square

import sys

def is_perfect_square(n):
    # TODO: Use binary search to determine if n is a perfect valid square
    return False

def main():
    for n in map(int, sys.stdin):
        print('Yes' if is_perfect_square(n) else 'No')

if __name__ == '__main__':
    main()
