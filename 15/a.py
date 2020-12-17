#!/usr/bin/env python3
import sys
from expecter import expect


def aoc(data):
    numbers = list(map(int, data.split(",")))
    numbers.reverse()
    while len(numbers) < 2020:
        last = numbers[0]
        if last not in numbers[1:]:
            numbers.insert(0, 0)
        else:
            idx = numbers[1:].index(last) + 1
            numbers.insert(0, idx)
    assert len(numbers) == 2020
    return numbers[0]


expect(aoc("0,3,6")) == 436
expect(aoc("1,3,2")) == 1
expect(aoc("2,1,3")) == 10
expect(aoc("1,2,3")) == 27
expect(aoc("2,3,1")) == 78
expect(aoc("3,2,1")) == 438
expect(aoc("3,1,2")) == 1836

print(aoc(sys.stdin.read()))
