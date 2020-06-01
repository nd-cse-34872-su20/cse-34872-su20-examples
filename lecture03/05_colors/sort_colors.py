#!/usr/bin/env python3

import sys

def count_colors(line):
    counts = [0, 0, 0]

    for i in map(int, line.split()):
        counts[i] += 1

    return counts

def main():
    for line in sys.stdin:
        counts = count_colors(line)
        result = []

        for i, v in enumerate(counts):
            result.extend([i]*v)

        print(' '.join(map(str, result)))

if __name__ == '__main__':
    main()
