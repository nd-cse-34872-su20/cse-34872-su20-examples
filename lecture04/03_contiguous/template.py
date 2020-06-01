#!/usr/bin/env python3

import collections
import sys

# Functions


def find_maximum_contiguous_array(array):
    # TODO: find length of maximum contiguous array
    return 0
        
# Main execution

if __name__ == '__main__':
    for line in sys.stdin:
        digits = map(int, line.split())
        print(find_maximum_contiguous_array(digits))
