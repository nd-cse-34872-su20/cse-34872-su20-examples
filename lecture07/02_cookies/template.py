#!/usr/bin/env python3

import sys

# Functions

def feed_children(children, cookies):
    # TODO: Return how many children are fed with the given cookies

def main():
    while ((children := sys.stdin.readline().split()) and
           (cookies  := sys.stdin.readline().split())):
        children = sorted(map(int, children), reverse=True)
        cookies  = sorted(map(int, cookies) , reverse=True)

        print(feed_children(children, cookies))

# Main execution

if __name__ == '__main__':
    main()
