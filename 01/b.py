#!/usr/bin/env python3

import sys
from itertools import combinations

for a, b, c in combinations(map(int, sys.stdin.readlines()), 3):
    if a + b + c == 2020:
        print(a * b * c)
        break
