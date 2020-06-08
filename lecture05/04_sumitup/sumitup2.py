#!/usr/bin/env python3

import sys

# Functions

def sumitup_r(subset, numbers, index, target):
    # Base case: subset sums up to target, so yield it
    if sum(subset) == target:
        yield tuple(subset)

    # Base case: prune search when index is length of numbers, or sum of susbet
    # is greater than target
    if index == len(numbers) or sum(subset) > target:
        return

    # Recursive step: try with current number and without
    yield from sumitup_r(subset + [numbers[index]], numbers, index + 1, target)
    yield from sumitup_r(subset                   , numbers, index + 1, target)

def sumitup(numbers, target):
    return sorted(set(sumitup_r([], numbers, 0, target)), reverse=True)

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
