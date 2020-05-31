#!/usr/bin/env python3

import sys

# Functions

LEFT_PBB  = ('(', '[', '{')
RIGHT_PBB = (')', ']', '}')

def is_pbbmatched(s):
    left = []

    for c in s:
        if c in LEFT_PBB:               # Push left PBB
            left.append(c)
        else:
            if not left:                # Nothing left to complete match
                return False

            index = RIGHT_PBB.index(c)  # Make sure we have a match
            if index >= 0 and left[-1] != LEFT_PBB[index]:
                return False

            left.pop(-1)

    return not left

# Main execution

if __name__ == '__main__':
    for line in sys.stdin:
        line   = line.rstrip()
        result = 'Yes' if is_pbbmatched(line) else 'No'
        print('{:>10}: {}'.format(line, result))
