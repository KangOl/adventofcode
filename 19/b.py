#!/usr/bin/env python3

import regex as re
import sys
from expecter import expect

def aoc(data):
    rules_s, messages = data.strip().split("\n\n")

    rules = dict(re.split(": ", r, 1) for r in re.split("\n+", rules_s))

    # rules["8"] = "42 | 42 8"
    # rules["11"] = "42 31 | 42 11 31"

    def repl(match):
        m = match.group(0)
        if m == "8":
            r42 = rules["42"]
            return f"(?:{r42})+?"
        elif m == "11":
            r42 = rules["42"]
            r31 = rules["31"]
            # Use recursing matching group.
            # A PCRE extension not handled by the builtin `re` module, hence the use of the `regex` package
            return f"(?P<eleven>(?:{42})(?&eleven)?(?:{r31}))"

        r = rules[m]
        if " " in r:
            return f"(?:{r})"
        return r.replace('"', "")

    r0 = rules["0"]
    while re.search(r"\d+", r0) is not None:
        r0 = re.sub(r"\d+", repl, r0)

    rx = r0.replace(" ", "")

    return len(re.findall(f"^{rx}$", messages, re.M))


test = """
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
"""

expect(aoc(test)) == 12
print(aoc(sys.stdin.read()))
