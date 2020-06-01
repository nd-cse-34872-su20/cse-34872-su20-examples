#!/usr/bin/env python3

import bisect

# Binary search

def binary_search(lst, item):
    index = bisect.bisect_left(lst, item)
    return index < len(lst) and lst[index] == item

def binary_search_index(lst, item):
    index = bisect.bisect_left(lst, item)
    return index if index < len(lst) and lst[index] == item else None

# Main execution

if __name__ == '__main__':
    data = [1, 3, 6, 8, 9]

    for i in range(10):
        print(i, binary_search(data, i))
        print(i, binary_search_index(data, i))
