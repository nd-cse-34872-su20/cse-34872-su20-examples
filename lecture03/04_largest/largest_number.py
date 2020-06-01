#!/usr/bin/env python3

import functools
import sys

# Functions

def compare_numbers(a, b):
    ab = int(a + b)
    ba = int(b + a)
    return ab - ba

def main():
    sort_key = functools.cmp_to_key(compare_numbers)
    for line in sys.stdin:
        print(''.join(sorted(line.split(), key=sort_key, reverse=True)))

# Main execution

if __name__ == '__main__':
    main()
