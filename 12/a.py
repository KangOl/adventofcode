#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from expecter import expect


def aoc(data):
    x, y = 0, 0
    fx, fy = 1, 0  # forward
    for instruction in data.split():
        action = instruction[0]
        value = int(instruction[1:])

        if action == "N":
            y += value
        elif action == "S":
            y -= value
        elif action == "E":
            x += value
        elif action == "W":
            x -= value
        elif action == "L":
            for _ in range(value // 90):
                fx, fy = fy * -1, fx
        elif action == "R":
            for _ in range(value // 90):
                fx, fy = fy, fx * -1
        elif action == "F":
            x += value * fx
            y += value * fy

    return abs(x) + abs(y)


test = """\
F10
N3
F7
R90
F11
"""

expect(aoc(test)) == 17 + 8
print(aoc(sys.stdin.read()))
