#!/usr/bin/env python3
from collections import defaultdict
from functools import reduce
from operator import mul
import re
import sys

from expecter import expect

def aoc(data, prefix):
    rules, my, tickets = data.strip().split("\n\n")

    rules = {
        name: [range(int(a), int(b) + 1), range(int(c), int(d) + 1)]
        for line in re.finditer(r"(.+?): (\d+)-(\d+) or (\d+)-(\d+)", rules)
        for name, a, b, c, d in [line.groups()]
    }

    tickets = [tuple(map(int, line.split(","))) for line in tickets.splitlines()[1:]]

    valids = []
    for t in tickets:
        for v in t:
            if not any(v in r1 or v in r2 for r1, r2 in rules.values()):
                break
        else:
            valids.append(t)

    rulematch = {}
    ln = len(valids[0])
    while rules:
        lr = len(rules)
        candidates = defaultdict(list)

        for c in range(ln):
            if c in rulematch.values():
                continue
            for rule, (r1, r2) in rules.items():
                if all(t[c] in r1 or t[c] in r2 for t in valids):
                    candidates[rule].append(c)

        for rule, idx in candidates.items():
            if len(idx) == 1:
                rulematch[rule] = idx[0]
                del rules[rule]

        if len(rules) == lr:
            print("infinite loop", locals())
            return None

    my = tuple(map(int, my.splitlines()[1].split(",")))
    return reduce(mul, (my[i] for r, i in rulematch.items() if r.startswith(prefix)))


test = """\
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
"""
expect(aoc(test, "")) == 11 * 12 * 13

print(aoc(sys.stdin.read(), "departure"))
