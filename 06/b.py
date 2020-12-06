#!/usr/bin/env python3
from collections import Counter
import sys

from expecter import expect

def aoc(input):
    response = 0
    for group in input.split("\n\n"):
        answers = group.split()
        c = Counter()
        for ans in answers:
            c.update(ans)
        response += len([k for k, v in c.items() if v == len(answers)])
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

expect(aoc(test)) == 6
print(aoc(sys.stdin.read()))
