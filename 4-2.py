#!/usr/bin/env python3
from collections import defaultdict


def main():
    dodos = defaultdict(lambda: defaultdict(int))

    with open('4.input') as fp:
        log = sorted(fp.readlines())

    guard = None
    sleep_start = 0
    for line in log:
        l = line.split()
        if l[-1] == 'shift':
            guard = int(l[-3][1:])
        elif l[-1] == 'asleep':
            sleep_start = int(l[1][3:-1])
        elif l[-1] == 'up':
            to = int(l[1][3:-1])
            for m in range(sleep_start, to):
                dodos[guard][m] += 1
        else:
            raise ValueError(line)

    sleeper = None
    max_ = 0
    minute = -1
    for guard in dodos:
        for m, c in dodos[guard].items():
            if c > max_:
                max_ = c
                sleeper = guard
                minute = m

    print(sleeper)
    print(minute)
    print(sleeper * minute)


if __name__ == '__main__':
    main()
