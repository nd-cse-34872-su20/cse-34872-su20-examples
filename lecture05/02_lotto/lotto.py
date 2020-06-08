#!/usr/bin/env python3

import itertools
import sys

# Constants

LOTTO_NUMBERS = 6

# Functions

def display_combinations(s, n=LOTTO_NUMBERS):
    # Use itertools to display combinations
    for combination in sorted(itertools.combinations(s, n)):
        print(' '.join(map(str, combination)))

def combinations(s, d, k):
    # Base: have a complete subset
    if len(d) == k:
        if len(s) == LOTTO_NUMBERS:
            print(' '.join(map(str, s)))
        return

    # Recurse: with current
    combinations(s + [d[k]], d, k + 1)

    # Recurse: skip current
    combinations(s, d, k + 1)

def main():
    for line, numbers in enumerate(map(str.split, sys.stdin)):
        if len(numbers) <= 1:
            break

        if line:
            print()

        # display_combinations(map(int, numbers[1:]))
        numbers = sorted(map(int, numbers[1:]))
        combinations([], numbers, 0)

# Main execution

if __name__ == '__main__':
    main()
