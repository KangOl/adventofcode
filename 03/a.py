#!/usr/bin/env python3
import sys

map_ = [r.strip() for r in sys.stdin.readlines()]
l = len(map_[0])  # noqa
h = len(map_) - 1

x, y = 0, 0
t = 0

while y < h:
    x, y = x + 3, y + 1
    if map_[y][x % l] == "#":
        t += 1

print(t)
