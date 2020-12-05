#!/usr/bin/env python3
from itertools import cycle

def main():
    freq = 0
    seen = {0}
    with open('1.input') as fp:
        freqs = [int(x) for x in fp.readlines()]
    for f in cycle(freqs):
        freq += f
        if freq in seen:
            print(freq)
            break
        seen.add(freq)


if __name__ == '__main__':
    main()
