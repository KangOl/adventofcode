#!/usr/bin/env python3
import sys
from expecter import expect

def seatID(line):
    row, column = line[:7], line[7:10]
    row = int(row.translate(str.maketrans("FB", "01")), 2)
    column = int(column.translate(str.maketrans("LR", "01")), 2)
    return row * 8 + column


expect(seatID("BFFFBBFRRR")) == 567
expect(seatID("FFFBBBFRRR")) == 119
expect(seatID("BBFFBBFRLL")) == 820

print(max(map(seatID, sys.stdin.readlines())))
