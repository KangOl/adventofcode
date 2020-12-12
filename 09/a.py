#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from itertools import islice, combinations
import sys
from expecter import expect

def xmas(data, preamble):
    numbers = list(map(int, data.strip().splitlines()))
    if len(numbers) <= preamble:
        return None

    for i in range(preamble, len(numbers)):
        sums = list(map(sum, combinations(islice(numbers, i - preamble, i), 2)))
        if numbers[i] not in sums:
            return numbers[i]


test = """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""

expect(xmas(test, 5)) == 127
print(xmas(sys.stdin.read(), 25))
