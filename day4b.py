#!/usr/bin/env python3
from collections import defaultdict


def inc(x):
    x = str(x)
    return all(int(a) <= int(b) for a, b in zip(x[:-1], x[1:]))


def dbl(x):
    x = str(x)

    c = defaultdict(int)

    if not any(a == b for a, b in zip(x[:-1], x[1:])):
        return False

    for a, b in zip(x[:-1], x[1:]):
        if a == b:
            c[a] += 1

    return 1 in c.values()


r = range(240920, 789857)
print(len([p for p in r if inc(p) and dbl(p)]))
