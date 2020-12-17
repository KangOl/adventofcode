#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from expecter import expect


def aoc(data):
    _, bus_ids = data.split()
    buses = [(int(b), t) for t, b in enumerate(bus_ids.split(",")) if b != "x"]

    ts = 0
    step = 1
    while True:
        for b, i in buses:
            if (ts + i) % b == 0:
                if step % b != 0:
                    step *= b
            else:
                break

        else:
            return ts
        ts += step


test = """
939
7,13,x,x,59,x,31,19
"""

expect(aoc(test)) == 1068781
expect(aoc("_\n17,x,13,19")) == 3417
expect(aoc("_\n67,7,59,61")) == 754018
expect(aoc("_\n67,x,7,59,61")) == 779210
expect(aoc("_\n67,7,x,59,61")) == 1261476
expect(aoc("_\n1789,37,47,1889")) == 1202161486

print(aoc(sys.stdin.read()))
