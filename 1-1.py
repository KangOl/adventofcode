#!/usr/bin/env python3


def main():
    freq = 0
    with open('1.input') as fp:
        for r in fp.readlines():
            freq += int(r)

    print(freq)


if __name__ == '__main__':
    main()
