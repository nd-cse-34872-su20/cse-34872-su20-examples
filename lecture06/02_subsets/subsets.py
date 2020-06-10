#!/usr/bin/env python3

import sys

# Function

def divisible_subsets(n):
    count = 0
    for bitset in range(1<<10):
        total = sum(i for i in range(10) if bitset & (1<<i))
        if total % n == 0:
            count += 1
    return count

def main():
    for n in map(int, sys.stdin):
        print(divisible_subsets(n))

# Main execution

if __name__ == '__main__':
    main()
