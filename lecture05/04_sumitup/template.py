#!/usr/bin/env python3

import itertools
import sys

# Functions

def sumitup_r(subset, numbers, index, target):
    # TODO Base case: subset sums up to target, so yield it

    # TODO Base case: prune search when index is length of numbers, or sum of susbet
    # is greater than target

    # TODO Recursive step: try with current number and without

def sumitup(numbers, target):
    # TODO: Recursively generate sums, collect results into set, and return
    # sorted results

def main():
    for line in sys.stdin:
        data    = list(map(int, line.split()))
        target  = data[0]
        n       = data[1]
        numbers = data[2:]

        if target == 0:
            break

        print('Sums of {}:'.format(target))
        results = sumitup(numbers, target)
        if results:
            for result in results:
                print('+'.join(map(str, result)))
        else:
            print('NONE')

# Main execution

if __name__ == '__main__':
    main()
