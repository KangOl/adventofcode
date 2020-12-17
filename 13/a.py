#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from expecter import expect


def aoc(data):
    ts, bus_ids = data.split()

    ts = int(ts)
    buses = [int(b) for b in bus_ids.split(",") if b != "x"]
    bus = min(buses, key=lambda b: b - (ts % b))
    return bus * (bus - (ts % bus))


test = """
939
7,13,x,x,59,x,31,19
"""

expect(aoc(test)) == 295
print(aoc(sys.stdin.read()))
