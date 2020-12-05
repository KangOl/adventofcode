#!/usr/bin/env python3
import sys

map_ = [r.strip() for r in sys.stdin.readlines()]
l = len(map_[0])  # noqa
h = len(map_) - 1

def slope(right, down):
    x, y = 0, 0
    t = 0

    while y < h:
        x, y = x + right, y + down
        if map_[y][x % l] == "#":
            t += 1
    return t


print(slope(1, 1) * slope(3, 1) * slope(5, 1) * slope(7, 1) * slope(1, 2))
