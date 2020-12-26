#!/usr/bin/env python3
import sys
from expecter import expect


def aoc(puzzle, size, moves):
    # use a dict as linked list
    # so moving elements is just changing who's next
    puzzle = puzzle.strip()
    assert len(puzzle) == 9
    start = list(map(int, puzzle))

    cups = dict()
    for i in range(8):
        cups[start[i]] = start[i + 1]

    if size > 9:
        cups[start[-1]] = 10
        for n in range(10, size):
            cups[n] = n + 1

        cups[size] = start[0]  # ring
    else:
        cups[start[-1]] = start[0]

    current = start[0]
    for rnd in range(moves):
        """
            From        To
            =======     ===
            A -> B      A -> E
            B -> C
            C -> D
            D -> E

            I -> J      I -> B
                        D -> J

            ==================
            current = A
            next1 = B
            next2 = C
            next3 = D
            insert = I
        """

        next1 = cups[current]
        next2 = cups[next1]
        next3 = cups[next2]

        insert = current - 1
        if insert == 0:
            insert = size
        while insert in {next1, next2, next3}:
            insert -= 1
            if insert == 0:
                insert = size

        cups[current] = cups[next3]
        cups[next3] = cups[insert]
        cups[insert] = next1

        current = cups[current]

    after_one = cups[1]
    return after_one * cups[after_one]


test = "389125467"

size = 1_000_000
moves = 10_000_000
expect(aoc(test, size, moves)) == 149245887792
print(aoc(sys.stdin.read(), size, moves))
