#!/usr/bin/env python3

import collections

# Functions

def permutations(p, c):
    # Base: Used all candidates, so print information
    if not c:
        print(''.join(p))
        return

    # Recurse: For each candidate, build a permutation with and without it
    for e in sorted(c):
        # Place element into permutation and remove from candidates
        p.append(e)
        c.remove(e)

        # Recurse on subset (which is now one item shorter and no longer
        # includes the previously placed element as a character)
        permutations(p, c)

        # Add element back to candidates and remove from permutation
        c.add(e)
        p.pop()

def main():
    permutations([], set(['A', 'B', 'C']))

# Main execution

if __name__ == '__main__':
    main()
