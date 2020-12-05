#!/usr/bin/env python3


def inc(x):
    x = str(x)
    return all(int(a) <= int(b) for a, b in zip(x[:-1], x[1:]))


def dbl(x):
    x = str(x)
    return any(a == b for a, b in zip(x[:-1], x[1:]))


r = range(240920, 789857)
print(len([p for p in r if dbl(p) and inc(p)]))
