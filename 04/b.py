#!/usr/bin/env python3
import sys
import re

validations = {
    "byr": lambda v: 1920 <= int(v) <= 2002,
    "iyr": lambda v: 2010 <= int(v) <= 2020,
    "eyr": lambda v: 2020 <= int(v) <= 2030,
    "hgt": lambda v: {
        "cm": lambda v: 150 <= int(v) <= 193,
        "in": lambda v: 59 <= int(v) <= 76,
    }.get(v[-2:], lambda v: False)(v[:-2]),
    "hcl": lambda v: re.match("^#[0-9a-z]{6}$", v) is not None,
    "ecl": lambda v: v in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    "pid": lambda v: len(v) == 9 and v.isdigit(),
    "cid": lambda v: True,
}


count = 0

for passport in sys.stdin.read().split("\n\n"):
    passport = dict(part.split(":", 1) for part in passport.split())

    keys = set(passport.keys()) | {"cid"}
    if keys == set(validations.keys()):
        if all(validations[k](v) for k, v in passport.items()):
            count += 1

print(count)
