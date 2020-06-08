#!/usr/bin/env python3

import itertools

s = 'ABC'
for p in itertools.permutations(s):
    print(''.join(p))
