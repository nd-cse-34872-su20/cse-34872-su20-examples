#!/usr/bin/env python3

# Perfect Square

import sys

def is_perfect_square(n):
    ''' Binary search '''
    low, high = 1, n

    while low <= high:
        middle = (low + high) // 2
        square = middle * middle
        
        if square == n:
            return True

        if square > n:
            high = middle - 1
        else:
            low  = middle + 1

    return False

'''
# Linear search
def is_perfect_square(n):
    for i in range(1, n):
        if i*i == n:
            return True
    return False
'''

def main():
    for n in map(int, sys.stdin):
        print('Yes' if is_perfect_square(n) else 'No')

if __name__ == '__main__':
    main()
