#!/usr/bin/env python3

import collections
import functools
import sys

# Structures

Person = collections.namedtuple('People', 'first last')

# Functions

def dump_people(people):
    for person in people:
        print('{} {}'.format(person.first, person.last))

def sort_people(people):
    #people = sorted(people, key=lambda p: p.first)
    #people = sorted(people, key=lambda p: p.last)
    people = sorted(people, key=lambda p: (p.last, p.first))
    return people

# Main execution

if __name__ == '__main__':
    people = [Person(*line.split()) for line in sys.stdin]
    dump_people(sort_people(people))
