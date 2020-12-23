#!/usr/bin/env python3
import math
import sys
import numpy as np
from expecter import expect


def find(tiles, side, expected):
    for key, tile in tiles.items():
        for turn in range(8):
            if np.all(tile[side] == expected):
                return key, tile
            tile = np.rot90(tile)
            if turn == 3:
                tile = tile.T


def aoc(data, print_monsters=False):
    tiles = {}

    for rawtile in data.strip().split("\n\n"):
        title, *tile = rawtile.splitlines()
        # title = "Tile 2311:"
        tiles[title] = np.array([
            [1 if x == "#" else 0 for x in line]
            for line in tile
        ], dtype=int)

    grid_sz = int(math.sqrt(len(tiles)))

    _, grid = tiles.popitem()

    tile_sz, _ = grid.shape

    left = (slice(0, tile_sz), -1)
    right = (slice(0, tile_sz), 0)
    bottom = (-1, slice(0, tile_sz))
    top = (0, slice(0, tile_sz))

    while True:
        match = find(tiles, side=left, expected=grid[right])
        if not match:
            # reach left side
            break
        del tiles[match[0]]
        grid = np.hstack((match[1], grid))

    while True:
        match = find(tiles, side=right, expected=grid[left])
        if not match:
            # reach right side
            break
        del tiles[match[0]]
        grid = np.hstack((grid, match[1]))

    assert grid.shape == (tile_sz, tile_sz * grid_sz)

    while True:
        match = find(tiles, side=bottom, expected=grid[top])
        if not match:
            # reach the top
            break
        del tiles[match[0]]
        row = match[1]

        for step in range(1, grid_sz):
            match = find(tiles, side=right, expected=row[left])
            del tiles[match[0]]
            row = np.hstack((row, match[1]))

        grid = np.vstack((row, grid))

    while True:
        match = find(tiles, side=top, expected=grid[bottom])
        if not match:
            # reach bottom
            break
        del tiles[match[0]]
        row = match[1]

        for step in range(1, grid_sz):
            match = find(tiles, side=right, expected=row[left])
            del tiles[match[0]]
            row = np.hstack((row, match[1]))

        grid = np.vstack((grid, row))

    assert grid.shape == (tile_sz * grid_sz, tile_sz * grid_sz)
    assert not tiles

    monster = """\
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """  # noqa
    amonster = np.array([[c == "#" for c in line] for line in monster.split("\n")], dtype=int)

    mh, mw = amonster.shape

    img = np.vstack(
        [
            np.hstack(
                [
                    grid[x + 1:x + tile_sz - 1, y + 1:y + tile_sz - 1]
                    for y in range(0, tile_sz * grid_sz, tile_sz)
                ]
            )
            for x in range(0, tile_sz * grid_sz, tile_sz)
        ]
    )
    img_sz, _ = img.shape

    for turn in range(8):
        monster_found = []
        for i in range((img_sz - mh) + 1):
            for j in range((img_sz - mw) + 1):
                s = img[i:i + mh, j:j + mw]
                if np.all(s & amonster == amonster):
                    monster_found.append((i, j))

        if monster_found:
            for i, j in monster_found:
                img[i:i + mh, j:j + mw] += amonster

            if print_monsters:
                print(
                    np.array2string(
                        img,
                        img_sz * 5,
                        separator="",
                        threshold=img_sz * img_sz,
                        formatter={"int": lambda x: {0: " ", 1: "·"}.get(x, f"\033[1;31m{x:X}\033[0m")},
                    )
                )
            bc = np.bincount(img.flatten())
            return bc[1]

        img = np.rot90(img)
        if turn == 3:
            img = img.T

    return 0


test = """
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
"""


expect(aoc(test)) == 273
print(aoc(sys.stdin.read(), print_monsters=True))
