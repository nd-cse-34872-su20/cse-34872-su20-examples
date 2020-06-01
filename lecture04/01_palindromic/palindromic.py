#!/usr/bin/env python3

import collections
import sys

# Functions

def is_palindromic(s):
    ''' Counting Solution '''

    # counts = collections.Counter(s)
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1

    odds = 0
    for count in counts.values():
        odds += count % 2

    return odds <= 1

# Main Execution

if __name__ == '__main__':
    for word in sys.stdin:
        print('Yes' if is_palindromic(word.rstrip()) else 'No')
