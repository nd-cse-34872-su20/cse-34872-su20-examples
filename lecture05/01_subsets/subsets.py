#!/usr/bin/env python3

import itertools

# Constants

NUMBERS = range(0, 10)

# Functions

def main():
    count = 0
    for length in range(0, len(NUMBERS) + 1):
        for subset in itertools.combinations(NUMBERS, length):
            if sum(subset) % 3 == 0:
                count += 1

    print(count)

# Main Execution

if __name__ == '__main__':
    main()
