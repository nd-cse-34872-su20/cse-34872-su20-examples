#!/usr/bin/env python3

import sys

# Naive version

def is_happy(n, seen):
    # TODO: Determine if n is a happy number (recursively)
    return False

# Main execution

for n in map(int, sys.stdin):
    print('Yes' if is_happy_cached(n, set()) else 'No')
