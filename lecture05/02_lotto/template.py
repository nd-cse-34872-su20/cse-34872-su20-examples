#!/usr/bin/env python3

import itertools
import sys

# Constants

LOTTO_NUMBERS = 6

# Functions

def display_combinations(s, n=LOTTO_NUMBERS):
    # TODO Version 1: Use itertools to display combinations

def combinations(s, d, k):
    # TODO Version 2: Generate combinations recursively

    # TODO Base: have a complete subset

    # TODO Recurse: with current

    # TODO Recurse: skip current

def main():
    for line, numbers in enumerate(map(str.split, sys.stdin)):
        if len(numbers) <= 1:
            break

        # TODO: Handle blank line between cases

        # TODO Version 1: Use display_combinations

        # TODO Version 2: Convert numbers to integers, sort them, and then
        # recursively generate combinations

# Main execution

if __name__ == '__main__':
    main()
