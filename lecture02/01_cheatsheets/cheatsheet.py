#!/usr/bin/env python3

v = [1, 2, 3]       # Create dynamic array

v.append(4)         # Append to back of array
v.insert(0, 0)      # Prepend to front of array

print(len(v))       # Display n
for e in v:         # Traverse elements
    print(e)

                    # Traverse elements with index
for i, e in enumerate(v):
    print('{}: {}'.format(i, e))
