#!/usr/bin/env python3

import collections
import sys

# Functions

def find_maximum_contiguous_array(array):
    max_length = 0
    for i in range(0, len(array)):
        for j in range(1, len(array) + 1):
            subarray = array[i:j]
            subcount = collections.Counter(subarray)
            if subcount[0] == subcount[1] and len(subarray) > max_length:
                max_length = len(subarray)
    return max_length

'''
The idea is to model the series of binary digits as a curve and keep track of
the current total.

For instance, given the sequence 0 0 0 0 1 1

    Every time we have a 0, we decrement our current total.
    Every time we have a 1, we increment our current total.

    Digit   | Total
    ---------------
    0       | -1
    0       | -2        <---------------|
    0       | -3        <-|             |
    0       | -4          | Balanced    | Balanced 
    1       | -3        <-|             |
    1       | -2        <---------------|

What we can observe is that anytime we return to a previous total, we have gone
through a balanced series of ups and downs (increments and decrements, 0's and
1's).

Therefore, our strategy is to iterate through our sequence of digits, track the
current total, and check if we have ever seen the current total before.  If we
have, then we can compute the length of the series of ups and downs (ie. number
of balanced digits) by subtracting the first time we have seen this length with
our current index.  We then can compare this length to our current maximum
length and update it appropriately.
'''

def find_maximum_contiguous_array(array):
    totals     = {0: 0} # Totals -> Index where we first achieved this total
    cur_total  = 0      # Current total
    max_length = 0      # Maximum length

    for index, digit in enumerate(array, 1):
        # Update current total so we move up on 1 and down on 0
        cur_total += 1 if digit == 1 else -1

        # If we have seen this current total before, then we have found a
        # balanced sequence.  We can compute the length of this balanced
        # sequence by taking our index and subtracting the index of the first
        # time we saw this sequence.  Otherwise, if this is the first time we
        # have seen this current total, we simply store the index in our table.
        if cur_total in totals:
            max_length = max(max_length, index - totals[cur_total])
        else:
            totals[cur_total] = index

    return max_length
        
# Main execution

if __name__ == '__main__':
    for line in sys.stdin:
        digits = map(int, line.split())
        print(find_maximum_contiguous_array(digits))
