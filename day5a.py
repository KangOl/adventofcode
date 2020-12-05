#!/usr/bin/env python3
from operator import add, mul

def run(prog, noun, verb):

    prog[1] = noun
    prog[2] = verb

    pos = 0
    while prog[pos] != 99:
        if prog[pos] in (1,2):
            func = {1: add, 2: mul}[prog[pos]]
            prog[prog[pos + 3]] = func(prog[prog[pos + 1]], prog[prog[pos + 2]])
        elif prog[pos] == 3:

        pos += 4
    return prog[0]

prog = []
run(prog)
