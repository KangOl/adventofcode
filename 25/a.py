#!/usr/bin/env python3
import sys
from expecter import expect


def guess_loop_size(pkey, subject=7):
    loop = 0
    value = 1

    while value != pkey:
        value = (value * subject) % 20201227
        loop += 1

    return loop


def aoc(data):
    card_pkey, door_pkey = map(int, data.split())

    card_ls = guess_loop_size(card_pkey)

    enc_key = 1
    for _ in range(card_ls):
        enc_key = (enc_key * door_pkey) % 20201227

    return enc_key


test = "5764801\n17807724"
expect(aoc(test)) == 14897079
print(aoc(sys.stdin.read()))
