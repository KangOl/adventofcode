#!/usr/bin/env python3
import sys
from collections import deque
from expecter import expect

def aoc(puzzle, moves):
    puzzle = puzzle.strip()
    d = deque(map(int, puzzle), maxlen=len(puzzle))

    dmax = max(d)
    dmin = min(d)

    for _ in range(moves):
        d.rotate(-1)
        pick = [d.popleft(), d.popleft(), d.popleft()]
        cup1 = d[-1] - 1
        if cup1 < dmin:
            cup1 = dmax
        while cup1 in pick:
            cup1 -= 1
            if cup1 < dmin:
                cup1 = dmax

        n = len(d) - d.index(cup1) - 1
        d.rotate(n)
        d.extend(pick)
        d.rotate(-n)

    d.rotate(-d.index(1)-1)
    d.pop()
    return "".join(map(str, d))


test = "389125467"
expect(aoc(test, 10)) == "92658374"
expect(aoc(test, 100)) == "67384529"
print(aoc(sys.stdin.read(), 100))
