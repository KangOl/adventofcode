#!/usr/bin/env python3

import sys
from itertools import combinations

for a, b in combinations(map(int, sys.stdin.readlines()), 2):
    if a + b == 2020:
        print(a * b)
        break
