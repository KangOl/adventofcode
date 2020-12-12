#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from itertools import islice, combinations
import sys
from expecter import expect

def xmas(data, preamble):
    numbers = list(map(int, data.strip().splitlines()))
    if len(numbers) <= preamble:
        return None

    invalid = None
    for i in range(preamble, len(numbers)):
        sums = list(map(sum, combinations(islice(numbers, i - preamble, i), 2)))
        if numbers[i] not in sums:
            invalid = numbers[i]
            break

    assert invalid is not None

    for setlength in range(2, len(numbers) - 2):
        for i in range(len(numbers) - setlength):
            j = i + setlength
            subset = numbers[i:j]
            assert len(subset) == setlength
            if sum(subset) == invalid:
                return min(subset) + max(subset)


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

expect(xmas(test, 5)) == 62
print(xmas(sys.stdin.read(), 25))
