#!/usr/bin/env python3
from itertools import chain, combinations
import sys
from expecter import expect

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def aoc(data):
    mask = ""
    x_mask = []
    mem = {}

    for line in data.strip().splitlines():
        act, _, value = line.strip().partition(" = ")
        if act == "mask":
            mask = value
            x_mask = [i for i, v in enumerate(mask) if v == "X"]
        elif act.startswith("mem["):
            addr = int(act[4:-1])
            value = int(value)

            baddr = f"{addr:036b}"
            fmask = ""
            for i, v in enumerate(mask):
                fmask += "X" if v == "X" else str(int(baddr[i]) | int(v))

            for ones in powerset(x_mask):
                addr = int(fmask.replace("X", "0"), 2)
                for o in ones:
                    addr |= 1 << (35 - o)

                mem[addr] = value

    return sum(mem.values())


test = """\
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""

expect(aoc(test)) == 208
print(aoc(sys.stdin.read()))
