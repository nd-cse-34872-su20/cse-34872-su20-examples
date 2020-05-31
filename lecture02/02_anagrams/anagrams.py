#!/usr/bin/env python3

import collections
import sys

# Functions

def is_anagram_sorted(s, t):
    return sorted(s.lower()) == sorted(t.lower())

def is_anagram_histogram(s, t):
    sc = collections.Counter(s.lower())
    tc = collections.Counter(t.lower())
    return sc == tc

is_anagram = is_anagram_histogram

# Main Execution

if __name__ == '__main__':
    for line in sys.stdin:
        first, second = line.strip().split()
        print('Anagram' if is_anagram(first, second) else 'Not Anagram')
