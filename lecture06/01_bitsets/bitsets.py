#!/usr/bin/env python3

elements = (1, 2, 4)
bitset   = 0                        # 1. Initialize bitset

# Add elements to bitset
for i in elements:
    bitset = bitset | 1<<i          # 2. Add element to bitset

# Print contents of bitset
print(bitset)

# Test for elements in bitset
for i in range(6):
    if bitset & 1<<i:               # 3. Test if element is in bitset
        print(i)

# Remove elements from bitset
for i in elements:
    bitset = bitset & ~(1<<i)       # 4. Remove element from bitset

# Print contents of bitset
print(bitset)
