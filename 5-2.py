#!/usr/bin/env python3
from string import ascii_lowercase

def main():

    with open('5.input') as fp:
        polymer = fp.read().strip()

    counts = dict()

    for l in ascii_lowercase:

        chain = ''
        for c in polymer:
            if c.lower() == l:
                continue
            if not chain:
                chain = c
                continue
            if abs(ord(chain[-1]) - ord(c)) != 32:
                chain += c
            else:
                chain = chain[:-1]

        counts[l] = len(chain)

    print(min(counts.values()))


if __name__ == '__main__':
    main()
