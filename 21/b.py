#!/usr/bin/env python3
from functools import reduce
import operator
import sys

from expecter import expect

def aoc(data):

    foods = {}
    for line in data.strip().splitlines():
        menu, _, alergens = line.partition(" (contains ")
        foods[frozenset(menu.split())] = set(alergens[:-1].split(", "))

    alergens = reduce(operator.or_, foods.values())
    matches = {}
    loop = set()
    while alergens:
        alergen = alergens.pop()

        common_ingredients = reduce(operator.and_, (m for m, a in foods.items() if alergen in a))
        if len(common_ingredients) == 1:
            matches[alergen] = list(common_ingredients)[0]
            foods = {
                m - common_ingredients: a - {alergen}
                for m, a
                in foods.items()
            }
            loop = set()
        else:
            if alergen in loop:
                break
            loop.add(alergen)
            alergens.add(alergen)

    return ",".join(matches[a] for a in sorted(matches))


test = """\
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
"""

expect(aoc(test)) == "mxmxvkd,sqjhc,fvjkl"
print(aoc(sys.stdin.read()))
