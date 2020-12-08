#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from expecter import expect

def parse(rules):
    rules = rules.strip().splitlines()

    ruledict = {}
    for rule in rules:
        name, _, content = rule.rstrip(".").partition(" bags contain ")
        if content == "no other bags":
            ruledict[name] = []
        else:
            ruledict[name] = [
                " ".join(s[1:-1])
                for c in content.split(",")
                for s in [c.split()]
            ]

    return ruledict


def aoc(rules):
    rules = parse(rules)
    canhold = lambda v: ("shiny gold" in v) or any(canhold(rules[k]) for k in v)
    return len([k for k in rules if canhold(rules[k])])


test = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

expect(aoc(test)) == 4
print(aoc(sys.stdin.read()))
