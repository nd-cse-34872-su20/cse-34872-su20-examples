#!/usr/bin/env python3

import sys

# Naive version

def is_happy(n, seen):
    if n in seen:                   # Base case: cycles
        return False

    if n == 1:                      # Base case: reaches 1
        return True

    seen.add(n)                     # Mark seen

    squares = sum(x * x for x in map(int, str(n)))
    return is_happy(squares, seen)  # Recurse

# Memoized version

IsHappy = {}                        # Memoization cache

def is_happy_cached(n, seen):
    if n in seen:                   # Base case: cycles
        return False

    if n == 1:                      # Base case: reaches 1
        return True
    
    seen.add(n)                     # Mark seen

    if n not in IsHappy:            # Memoize recursive call
        squares    = sum(x * x for x in map(int, str(n)))
        IsHappy[n] = is_happy_cached(squares, seen)

    return IsHappy[n]

# Main execution

for n in map(int, sys.stdin):
    print('Yes' if is_happy_cached(n, set()) else 'No')
