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

    # def find_closest(x, y):
    #     if (x, y) in coods:
    #         return (x, y), 0
    #     dists = defaultdict(list)
    #     for a, b in coods:
    #         d = abs(x - a) + abs(b - y)
    #         dists[d].append((a, b))
    #     m = min(dists)
    #     if len(dists[m]) == 1:
    #         return dists[m][0], m
    #     return None, None

    # infinites = []
    # dists = defaultdict(int)
    area = 0
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            d = sum(abs(x - a) + abs(b - y) for a, b in coods)
            if d < 10000:
                area += 1

    print(area)


if __name__ == '__main__':
    main()
