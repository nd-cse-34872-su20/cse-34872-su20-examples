#!/usr/bin/env python3

# Linear search

def linear_search(lst, item):
    return item in lst

def linear_search_index(lst, item):
    try:
        return lst.index(item)
    except ValueError:
        return None

# Main execution

if __name__ == '__main__':
    data = [1, 3, 6, 8, 9]

    for i in range(10):
        print(i, linear_search(data, i))
        print(i, linear_search_index(data, i))
