#!/usr/bin/env python3
import sys
from expecter import expect

def aoc(data):
    and_mask = or_mask = mask = "X"
    mem = {}

    for line in data.strip().splitlines():
        act, _, value = line.strip().partition(" = ")
        if act == "mask":
            mask = value
            and_mask = int(mask.replace("X", "1"), 2)
            or_mask = int(mask.replace("X", "0"), 2)
        elif act.startswith("mem["):
            pos = int(act[4:-1])
            value = int(value)
            mem[pos] = (value & and_mask) | or_mask

    return sum(mem.values())


test = """\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""

expect(aoc(test)) == 165
print(aoc(sys.stdin.read()))
