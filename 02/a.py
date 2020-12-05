#!/usr/bin/env python3
import re
import sys

valid = 0
for line in sys.stdin.readlines():
    min_, max_, letter, passwd = re.search(r"(\d+)-(\d+) (\w): (\w+)$", line).groups()
    if int(min_) <= passwd.count(letter) <= int(max_):
        valid += 1

print(valid)
