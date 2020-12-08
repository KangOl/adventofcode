#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from expecter import expect


def aoc(prog):
    accumulator = 0
    ops = [x.strip().split(" ", 1) for x in prog.strip().splitlines()]

    pos = 0
    seen = set()
    changed_data = None

    while pos < len(ops):

        loop = pos in seen
        if loop:
            pos, accumulator, seen = changed_data
            changed_data = None

        seen.add(pos)

        op, arg = ops[pos]

        if op == "acc":
            accumulator += int(arg)
            pos += 1
        else:
            assert op in {"nop", "jmp"}
            if changed_data is None and not loop:
                # invert the operator
                op = "nop" if op == "jmp" else "jmp"
                changed_data = (pos, accumulator, set(seen))

            if op == "nop":
                pos += 1
            elif op == "jmp":
                pos += int(arg)

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

expect(aoc(test)) == 8
print(aoc(sys.stdin.read()))
