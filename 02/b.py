#!/usr/bin/env python3
import re
import sys

valid = 0
for line in sys.stdin.readlines():
    a, b, letter, passwd = re.search(r"(\d+)-(\d+) (\w): (\w+)$", line).groups()
    if (passwd[int(a) - 1] == letter) ^ (passwd[int(b) - 1] == letter):
        valid += 1

print(valid)
