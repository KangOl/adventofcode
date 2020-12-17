#!/usr/bin/env python3
from collections import defaultdict
import sys
from expecter import expect


def aoc(data, nth):
    spoken = defaultdict(int)
    init = list(map(int, data.split(",")))
    for i, j in enumerate(init[:-1], 1):
        spoken[j] = i

    last = init[-1]
    for cpt in range(len(init), nth):
        idx = spoken[last]
        spoken[last] = cpt
        last = cpt - idx if idx != 0 else 0

    return last


puzzle = sys.stdin.read()

nth = 2020
expect(aoc("0,3,6", nth)) == 436
expect(aoc("1,3,2", nth)) == 1
expect(aoc("2,1,3", nth)) == 10
expect(aoc("1,2,3", nth)) == 27
expect(aoc("2,3,1", nth)) == 78
expect(aoc("3,2,1", nth)) == 438
expect(aoc("3,1,2", nth)) == 1836
print(aoc(puzzle, nth))

nth = 30000000
expect(aoc("0,3,6", nth)) == 175594
expect(aoc("1,3,2", nth)) == 2578
expect(aoc("2,1,3", nth)) == 3544142
expect(aoc("1,2,3", nth)) == 261214
expect(aoc("2,3,1", nth)) == 6895259
expect(aoc("3,2,1", nth)) == 18
expect(aoc("3,1,2", nth)) == 362
print(aoc(puzzle, nth))
