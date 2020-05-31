#!/usr/bin/env python3

import sys

def has_duplicates(data):
    ''' Returns True if data contains duplicate elements. '''
    for index, value in enumerate(sorted(data)[:-1], 1):
        if value == data[index]:
            return True
    return False

def find_duplicates():
    ''' For each line of numbers, determine if there is a duplicate. '''
    for index, line in enumerate(sys.stdin, 1):
        data = line.split()

        if has_duplicates(data):
            print(f'Found duplicate in line {index}')
        else:
            print(f'No duplicates in line {index}')

if __name__ == '__main__':
    find_duplicates()
