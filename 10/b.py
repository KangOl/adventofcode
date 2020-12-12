#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import tee, groupby
import sys
from expecter import expect

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def aoc(data):
    bag = [0] + sorted(map(int, data.splitlines()))
    bag.append(bag[-1] + 3)

    diffs = list(map(lambda p: p[1] - p[0], pairwise(bag)))

    branches = 1

    for k, g in groupby(diffs):
        if k == 3:
            continue
        # I did the count of splits by explicitly enumerating them.
        # I known there is an algo to get those numbers,
        # but there should exist a math formula...
        branches *= {1: 1, 2: 2, 3: 4, 4: 7}[len(list(g))]

        # Possible horrible solution:
        # (but it's still an explicit enumeration of possibilities)
        # l = len(list(g))
        # s = [1] * l + [2] * (l//2) + [3] * (l//3)
        # len(
        #     set(
        #         tuple(x)
        #         for p in chain.from_iterable(
        #             combinations(s, r) for r in range(len(s) + 1)
        #         )
        #         if sum(p) == l
        #         for x in permutations(p)
        #     )
        # )

    return branches


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

expect(aoc(test)) == 8
expect(aoc(test2)) == 19208
print(aoc(sys.stdin.read()))
