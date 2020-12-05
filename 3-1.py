#!/usr/bin/env python3
from collections import defaultdict


def main():
    fabric = defaultdict(lambda: defaultdict(int))
    with open('3.input') as fp:
        for claim in fp.readlines():
            _, _, lt, sz = claim.split()
            l, t = map(int, lt[:-1].split(','))
            w, h = map(int, sz.split('x'))

            for x in range(l, l+w):
                for y in range(t, t+h):
                    fabric[x][y] += 1

    c = len([1 for x in fabric for y in fabric[x] if fabric[x][y] > 1])
    print(c)


if __name__ == '__main__':
    main()
