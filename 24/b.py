#!/usr/bin/env python3
import sys
from expecter import expect

def adjacents(tile):
    x, y = tile
    yield x - 0.5, y + 1
    yield x + 0.5, y + 1
    yield x + 1, y
    yield x + 0.5, y - 1
    yield x - 0.5, y - 1
    yield x - 1, y

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

    day = black
    for _ in range(100):
        next_day = set()

        for black_tile in day:
            adj_black = 0

            for adj in adjacents(black_tile):
                if adj in day:
                    adj_black += 1
                else:
                    # a white tile with at least 1 adjacent black tile
                    if len([1 for adj2 in adjacents(adj) if adj2 in day]) == 2:
                        next_day.add(adj)
            if adj_black in (1, 2):
                # 1 or 2 black adjacents, keep it black
                next_day.add(black_tile)

        day = next_day

    return len(day)


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

expect(aoc(test)) == 2208
print(aoc(sys.stdin.read()))
