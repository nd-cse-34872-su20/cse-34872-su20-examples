#!/usr/bin/env python3

import sys

LINES = sys.stdin.readlines()
INDEX = 1

for line in LINES:
    data = line.split()
    data.sort()

    found = False
    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            print('Found duplicate in line ' + str(INDEX))
            found = True
            break

    if found == False:
        print('No duplicates in line ' + str(INDEX))

    INDEX += 1
