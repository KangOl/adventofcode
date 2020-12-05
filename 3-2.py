#!/usr/bin/env python3
from collections import defaultdict


def main():
    fabric = defaultdict(lambda: defaultdict(set))
    claims = {}
    with open('3.input') as fp:
        for claim in fp.readlines():
            ident, _, lt, sz = claim.split()
            l, t = map(int, lt[:-1].split(','))
            w, h = map(int, sz.split('x'))
            claims[ident] = me = set()

            for x in range(l, l + w):
                for y in range(t, t + h):
                    for o in fabric[x][y]:
                        me.add(o)
                        claims[o].add(ident)
                    fabric[x][y].add(ident)

    for c in claims:
        if not claims[c]:
            print(c)


if __name__ == '__main__':
    main()
