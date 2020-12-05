#!/usr/bin/env python3
from collections import defaultdict


def main():

    deps = defaultdict(set)
    with open('7.input') as fp:
        for row in fp.readlines():
            row = row.split()
            deps[row[7]].add(row[1])
            deps[row[1]]

    out = ''
    try:
        while True:
            out += min(d for d in deps if d not in out and not (deps[d] - set(out)))
    except ValueError:
        pass

    # out = min(d for d in deps if not deps[d])

    # def min_available():
    #     return min()

    print(out)


if __name__ == '__main__':
    main()
