#!/usr/bin/env python3

import sys

# Constants

COINS = (1, 3, 4)

# Functions

def compute_table(n, coins=COINS):
    # Initialize table to 0's
    table = [0] * (n + 1)

    # Initialize base cases (ie. coins)
    for coin in coins:
        table[coin] = 1

    # For each entry i in table, compute the following recurrence relation:
    #
    #   table[i] = min(table[i - coin] + 1 for coin in coins if (i - coin) >= 0)
    for i in range(1, n + 1):
        if not table[i]:
            table[i] = min(table[i - coin] + 1 for coin in coins if (i - coin) >= 0)

    return table

def compute_table_forward(n, coins=COINS):
    ''' Rather than looking backwards, we can generate the table by looking
    forwards.'''

    # Initialize table to n
    table = [n] * (n + 1)

    # Initialize base cases (ie. coins)
    for coin in coins:
        table[coin] = 1

    # For each entry i in table, generate successive values:
    #
    #   table[i + coin] = min(table[i] + 1, table[i + coin])
    for i in range(1, n - max(coins) + 1):
        for coin in coins:
            table[i + coin] = min(table[i] + 1, table[i + coin])

    return table

def compute_table_augment(n, coins=COINS):
    ''' What if we want to know what coins to use?

    In this case, we will need to store the coins in our table rather than just
    the length. '''

    # Initialize table to [1]'s
    table = [[1]*i for i in range(n + 1)]

    # Initialize base cases (ie. coins)
    for coin in coins:
        table[coin] = [coin]

    # For each entry i in table, generate successive values:
    #
    #   table[i + coin] = min(table[i] + 1, table[i + coin])
    for i in range(1, n - max(coins) + 1):
        for coin in coins:
            new_coins = table[i] + [coin]
            if len(new_coins) < len(table[i + coin]):
                table[i + coin] = new_coins

    return table

def main():
    # Pre-compute all solutions up to 100
    table = compute_table(100)

    # Lookup solutions in table
    for n in map(int, sys.stdin):
        print(f'{n} = {table[n]}')

# Main execution

if __name__ == '__main__':
    main()
