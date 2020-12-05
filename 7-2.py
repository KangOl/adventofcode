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

    print(out)
    from pprint import pprint
    pprint(deps)
    workers = [None] * 5
    done = ''
    sec = 0

    def assign(sec):
        for s in out[len(done):]:
            if deps[s] - set(done):
                break
            if any(w[0] == s for w in workers if w):
                continue
            for i, w in enumerate(workers):
                if not w:
                    workers[i] = (s, sec)
                    break
            else:
                break

    while done != out:
        for i, w in enumerate(workers):
            if not w:
                continue
            if sec - w[1] >= ord(w[0]) - 4:
                done += w[0]
                workers[i] = None
        assign(sec)
        print([sec, workers, done])
        if not any(workers):
            print('WTF')
            break
        sec += 1

    print(done == out)
    print(sec)


if __name__ == '__main__':
    main()
