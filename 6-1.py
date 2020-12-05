#!/usr/bin/env python3
from collections import defaultdict

def main():

    coods = []
    with open('6.input') as fp:
        for line in fp.readlines():
            x, _, y = line.partition(',')
            coods.append((int(x), int(y)))

    min_x = min(e[0] for e in coods)
    max_x = max(e[0] for e in coods)
    min_y = min(e[1] for e in coods)
    max_y = max(e[1] for e in coods)

    def find_closest(x, y):
        if (x, y) in coods:
            return (x, y), 0
        dists = defaultdict(list)
        for a, b in coods:
            d = abs(x - a) + abs(b - y)
            dists[d].append((a, b))
        m = min(dists)
        if len(dists[m]) == 1:
            return dists[m][0], m
        return None, None

    infinites = []
    dists = defaultdict(int)
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            c, d = find_closest(x, y)
            if not c:
                continue
            if y in (min_y, max_y + 1) or x in (min_x, max_x + 1):
                infinites.append(c)
            if c not in infinites:
                dists[c] += 1

    print(max(dists.values()))


if __name__ == '__main__':
    main()
