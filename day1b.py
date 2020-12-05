#!/usr/bin/env python3

total = 0
with open("day1.input") as fp:
    for l in fp.readlines():
        fuel = (int(l) // 3) - 2
        while fuel > 0:
            total += fuel
            fuel = (fuel // 3) - 2

print(total)
