#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from expecter import expect

def aoc(data):
    ferry = [r.strip() for r in data.strip().splitlines()]
    H = len(ferry)
    W = len(ferry[0])

    def adjacents(i, j):
        for x in range(max(0, i - 1), min(H - 1, i + 1) + 1):
            for y in range(max(0, j - 1), min(W - 1, j + 1) + 1):
                if (x, y) == (i, j):
                    continue
                dx, dy = x, y
                while 0 <= dx < H and 0 <= dy < W:
                    if ferry[dx][dy] != ".":
                        yield ferry[dx][dy]
                        break

                    dx += x - i
                    dy += y - j

    while True:
        nextferry = list(ferry)
        for i in range(H):
            for j in range(W):
                if ferry[i][j] == "L" and all(a != "#" for a in adjacents(i, j)):
                    nextferry[i] = nextferry[i][:j] + "#" + nextferry[i][j + 1:]
                elif ferry[i][j] == "#" and list(adjacents(i, j)).count("#") >= 5:
                    nextferry[i] = nextferry[i][:j] + "L" + nextferry[i][j + 1:]

        if ferry == nextferry:
            break
        ferry = nextferry

    return "".join(ferry).count("#")


test = """\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""

expect(aoc(test)) == 26
print(aoc(sys.stdin.read()))
