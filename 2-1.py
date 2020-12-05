#!/usr/bin/env python3
from collections import Counter


def main():
    two = set()
    three = set()
    with open('2.input') as fp:
        for ident in fp.readlines():
            c = Counter(ident)
            for _, count in c.items():
                if count == 2:
                    two.add(ident)
                if count == 3:
                    three.add(ident)

    print(len(two) * len(three))


if __name__ == '__main__':
    main()
