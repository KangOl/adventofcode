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
        s = sum(dodos[guard].values())
        if s > max_:
            max_ = s
            sleeper = guard
            minute = list(sorted(dodos[guard].items(), key=lambda t: t[1]))[-1][0]

    print(sleeper)
    print(minute)
    print(sleeper * minute)


if __name__ == '__main__':
    main()
