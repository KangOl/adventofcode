#!/usr/bin/env python3
import re
import sys
from expecter import expect

def aoc(data):
    rules, my, tickets = data.strip().split("\n\n")

    rules = {
        name: [range(int(a), int(b)+1), range(int(c), int(d)+1)]
        for line in re.finditer(r"(.+?): (\d+)-(\d+) or (\d+)-(\d+)", rules)
        for name, a, b, c, d in [line.groups()]
    }

    tickets = [tuple(map(int, line.split(","))) for line in tickets.splitlines()[1:]]

    result = 0
    for t in tickets:
        for v in t:
            if not any(v in r1 or v in r2 for r1, r2 in rules.values()):
                result += v

    return result


test = """\
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""

expect(aoc(test)) == 71
print(aoc(sys.stdin.read()))
