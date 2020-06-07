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

def is_perfect_square_r(low, high, n):
    ''' Binary search '''
    if low > high:
        return False

    middle = (low + high) // 2
    square = middle * middle
        
    if square == n:
        return True

    if square > n:
        return is_perfect_square_r(low, middle - 1, n)
    else:
        return is_perfect_square_r(middle + 1, high, n)

def is_perfect_square(n):
    return is_perfect_square_r(1, n, n)

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
