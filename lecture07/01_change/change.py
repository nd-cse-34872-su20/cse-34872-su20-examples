#!/usr/bin/env python3

import sys

# Constants

COINS = (25, 10, 5, 1)
#COINS = (4, 3, 1)

# Functions

def make_change(n):
    change = []
    for coin in COINS:  # Start with largest coin
        while n >= coin:
            change.append(coin)
            n -= coin
    return change

def main():
    for target in map(int, sys.stdin):
        print(' + '.join(map(str, make_change(target))))

# Main execution

if __name__ == '__main__':
    main()
