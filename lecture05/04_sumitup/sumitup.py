#!/usr/bin/env python3

import itertools
import sys

# Functions

def sumitup(numbers, target):
    count   = 0
    results = set()

    for length in range(1, len(numbers) + 1):
        for combination in itertools.combinations(numbers, length):
            if sum(combination) == target and combination not in results:
                results.add(combination)

    return sorted(results, reverse=True)

# Main execution

if __name__ == '__main__':
    for line in sys.stdin:
        data    = list(map(int, line.split()))
        target  = data[0]
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
