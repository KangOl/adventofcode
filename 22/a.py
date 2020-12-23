#!/usr/bin/env python3

import sys
from expecter import expect

def aoc(data):

    deck1, deck2 = data.strip().split("\n\n")
    deck1 = list(map(int, deck1[9:].split()))
    deck2 = list(map(int, deck2[9:].split()))

    while deck1 and deck2:
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if card1 > card2:
            deck1 += [card1, card2]
        else:
            deck2 += [card2, card1]

    winner_deck = deck1 or deck2
    return sum(i*v for i,v in enumerate(reversed(winner_deck), 1))

test = """
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""

expect(aoc(test)) == 306
print(aoc(sys.stdin.read()))
