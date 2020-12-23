#!/usr/bin/env python3

import sys
from expecter import expect

def aoc(data):

    deck1, deck2 = data.strip().split("\n\n")
    deck1 = list(map(int, deck1[9:].split()))
    deck2 = list(map(int, deck2[9:].split()))

    s1, s2 = play(deck1, deck2)
    return score(s1 or s2)

def score(deck):
    return sum(i * v for i, v in enumerate(reversed(deck), 1))

def play(deck1, deck2):
    played = set()

    while deck1 and deck2:

        td1 = tuple(deck1)
        td2 = tuple(deck2)
        if (td1, td2) in played:
            return deck1, deck2

        played.add((td1, td2))

        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        if len(deck1) >= card1 and len(deck2) >= card2:
            # recursive play
            sub_d1, sub_d2 = play(deck1[:card1], deck2[:card2])
            if sub_d1:
                deck1 += [card1, card2]
            else:
                deck2 += [card2, card1]
        else:
            if card1 > card2:
                deck1 += [card1, card2]
            else:
                deck2 += [card2, card1]

    return deck1, deck2


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

expect(aoc(test)) == 291
print(aoc(sys.stdin.read()))
