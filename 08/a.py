#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from expecter import expect


def aoc(prog):
    accumulator = 0
    ops = [x.strip() for x in prog.strip().splitlines()]
    pos = 0
    seen = set()
    while pos not in seen:
        seen.add(pos)
        op, _, arg = ops[pos].partition(" ")
        if op == "nop":
            pos += 1
        elif op == "acc":
            accumulator += int(arg)
            pos += 1
        elif op == "jmp":
            pos += int(arg)
        else:
            assert False

    return accumulator


test = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

expect(aoc(test)) == 5
print(aoc(sys.stdin.read()))
