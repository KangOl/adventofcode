#!/usr/bin/env python3

import re
import sys
from expecter import expect

def aoc(data):
    rules_s, messages = data.strip().split("\n\n")

    rules = dict(re.split(": ", r, 1) for r in re.split("\n+", rules_s))

    def repl(match):
        r = rules[match.group(0)]
        if " " in r:
            return f"(?:{r})"
        return r.replace('"', "")

    r0 = rules["0"]
    while re.search(r"\d+", r0) is not None:
        r0 = re.sub(r"\d+", repl, r0)

    rx = r0.replace(" ", "")

    return len(re.findall(f"^{rx}$", messages, re.M))


test = """
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""

expect(aoc(test)) == 2
print(aoc(sys.stdin.read()))
