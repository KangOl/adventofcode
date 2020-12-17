#!/usr/bin/env python3

from itertools import product, chain
import sys
from expecter import expect


def aoc(data):
    cubes = {
        (i, j, 0, 0)
        for i, line in enumerate(data.strip().splitlines())
        for j, state in enumerate(line)
        if state == "#"
    }

    def neighbors(x, y, z, w):
        return (
            (x + i, y + j, z + k, w + q)
            for i, j, k, q in product((-1, 0, 1), repeat=4)
            if (i, j, k, q) != (0, 0, 0, 0)
        )

    for _ in range(6):
        inactive_neighbors = (
            set(chain.from_iterable(neighbors(*c) for c in cubes)) - cubes
        )
        next_state = {
            c for c in cubes if len([n for n in neighbors(*c) if n in cubes]) in (2, 3)
        } | {
            c
            for c in inactive_neighbors
            if len([n for n in neighbors(*c) if n in cubes]) == 3
        }

        cubes = next_state

    return len(cubes)


test = """\
.#.
..#
###
"""

expect(aoc(test)) == 848
print(aoc(sys.stdin.read()))
