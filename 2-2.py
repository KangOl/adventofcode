#!/usr/bin/env python3

def main():
    with open('2.input') as fp:
        boxes = list(fp.readlines())

    for i, box in enumerate(boxes, 1):
        #off_by_one = []
        for other in boxes[i:]:
            commons = ''.join(a for a, b in zip(box, other) if a == b)
            if len(commons) == len(box) - 1:
                print(commons)
            #countdiff = len(1 for a, b in zip(box, other) if a != b)
            #if countdiff == 1:
            #    off_by_one.append(other)
        #if len(off_by_one) == 1:
            # found our boxes


if __name__ == '__main__':
    main()
