#!/usr/bin/env python3
import sys
from expecter import expect

def aoc(data):
    black = set()
    for line in data.strip().split("\n"):
        way = line.replace("nw", "u").replace("ne", "U").replace("sw", "d").replace("se", "D")

        x, y = 0, 0
        for direction in way:
            if direction == "u":
                x -= 0.5
                y += 1
            elif direction == "U":
                x += 0.5
                y += 1
            elif direction == "e":
                x += 1
            elif direction == "D":
                x += 0.5
                y -= 1
            elif direction == "d":
                x -= 0.5
                y -= 1
            elif direction == "w":
                x -= 1
            else:
                assert not direction

        if (x, y) in black:
            black.discard((x, y))
        else:
            black.add((x, y))

    return len(black)


test = """
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
"""

expect(aoc(test)) == 10
print(aoc(sys.stdin.read()))
