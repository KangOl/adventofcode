#!/usr/bin/env python3

fuel = 0
with open("day1.input") as fp:
    for l in fp.readlines():
        fuel += (int(l) // 3) - 2

print(fuel)
