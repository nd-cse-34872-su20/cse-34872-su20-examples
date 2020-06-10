#!/usr/bin/env python3

import sys

# Functions

def feed_children(children, cookies):
    # TODO: Return how many children are fed with the given cookies

def main():
    while ((children := sys.stdin.readline().split()) and
           (cookies  := sys.stdin.readline().split())):
        # TODO: Sort children and cookies in reverse order

        print(feed_children(children, cookies))

# Main execution

if __name__ == '__main__':
    main()
