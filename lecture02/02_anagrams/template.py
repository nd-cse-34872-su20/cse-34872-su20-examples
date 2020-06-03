#!/usr/bin/env python3

import collections
import sys

# Functions

def is_anagram(s, t):
    # TODO: Return whether or not s and t are anagrams
    return False

# Main Execution

if __name__ == '__main__':
    for line in sys.stdin:
        first, second = line.strip().split()
        print('Anagram' if is_anagram(first, second) else 'Not Anagram')
