#!/usr/bin/env python3
import sys

from expecter import expect

def aoc(input):
    response = 0
    for group in input.split("\n\n"):
        answers = group.split()
        d = dict()
        for ans in answers:
            d.update(dict.fromkeys(ans))
        response += len(d)
    return response


test = """\
abc

a
b
c

ab
ac

a
a
a
a

b
"""

expect(aoc(test)) == 11
print(aoc(sys.stdin.read()))
