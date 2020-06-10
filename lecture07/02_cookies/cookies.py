#!/usr/bin/env python3

import sys

# Functions

def feed_children(children, cookies):
    count = 0

    while cookies and children:
        child  = children.pop(0)
        cookie = cookies[0]

        if child <= cookie:
            cookies.pop(0)
            count += 1

    return count

def main():
    while ((children := sys.stdin.readline().split()) and
           (cookies  := sys.stdin.readline().split())):
        children = sorted(map(int, children), reverse=True)
        cookies  = sorted(map(int, cookies) , reverse=True)

        print(feed_children(children, cookies))

# Main execution

if __name__ == '__main__':
    main()
