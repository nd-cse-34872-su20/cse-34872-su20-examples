#!/usr/bin/env python3

import sys

# Functions

def is_subsequence(s, t):
    # Check if the front of s and t are the same.  If so, then consume one
    # letter from s.  Always, consume a letter from t so we progress to the
    # next letter to consider.
    while s and t:
        if s[0] == t[0]:
            s.pop(0)

        t.pop(0)

    # If s is empty, then each letter in s was found in order in t, and so we
    # have a subsequence.
    return not s

def main():
    for line in sys.stdin:
        s, t = map(list, line.split())
        print(is_subsequence(s, t))

# Main Execution

if __name__ == '__main__':
    main()
