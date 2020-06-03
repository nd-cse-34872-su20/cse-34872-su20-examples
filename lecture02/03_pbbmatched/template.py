#!/usr/bin/env python3

import sys

# Functions

LEFT_PBB  = ('(', '[', '{')
RIGHT_PBB = (')', ']', '}')

def is_pbbmatched(s):
    # TODO: Process string s using a stack to determine if the symbols are balanced 
    return False

# Main execution

if __name__ == '__main__':
    for line in sys.stdin:
        line   = line.rstrip()
        result = 'Yes' if is_pbbmatched(line) else 'No'
        print('{:>10}: {}'.format(line, result))
