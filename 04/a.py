#!/usr/bin/env python3
import sys

valid_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
no_cid = valid_keys - {"cid"}
count = 0

for passport in sys.stdin.read().split("\n\n"):
    passport_keys = {part.split(":")[0] for part in passport.split()}

    if passport_keys == valid_keys or passport_keys == no_cid:
        count += 1

print(count)
