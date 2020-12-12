#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import tee
import sys
from expecter import expect

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def aoc(data):
    bag = [0] + sorted(map(int, data.splitlines()))
    diffs = list(map(lambda p: p[1] - p[0], pairwise(bag)))

    # your device has a built-in joltage adapter rated for 3 jolts higher than the highest-rated adapter in your bag.
    diffs.append(3)
    return diffs.count(1) * diffs.count(3)


test = """\
16
10
15
5
1
11
7
19
6
12
4
"""

test2 = """\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""

expect(aoc(test)) == 7 * 5
expect(aoc(test2)) == 22 * 10
print(aoc(sys.stdin.read()))
