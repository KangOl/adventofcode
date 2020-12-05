#!/usr/bin/env python3

def main():

    with open('5.input') as fp:
        polymer = fp.read().strip()

    chain = ''
    for c in polymer:
        if not chain:
            chain = c
            continue
        if abs(ord(chain[-1]) - ord(c)) != 32:
            chain += c
        else:
            chain = chain[:-1]

    print(len(chain))


if __name__ == '__main__':
    main()
