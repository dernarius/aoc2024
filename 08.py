from collections import defaultdict
from itertools import permutations

data = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............\
"""


def find_antinode(a, b):
    diff = a[0] - b[0], a[1] - b[1]
    return b[0] - diff[0], b[1] - diff[1]


def find_all_antinodes(a, b, bounds):
    ret = set()
    diff = a[0] - b[0], a[1] - b[1]
    s, t = a
    while all((
        0 <= (s := s - diff[0]) < bounds[0],
        0 <= (t := t - diff[1]) < bounds[1],
    )):
        ret.add((s, t))

    return ret


def parse_map(data):
    antennas = defaultdict(set)
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char != ".":
                antennas[char].add((i, j))

    return antennas, (len(data), len(data[0]))


def part_one(data):
    antennas, bounds = parse_map(data)
    antinodes = set()
    for antenna, locations in antennas.items():
        for a, b in permutations(locations, 2):
            antinode = find_antinode(a, b)
            if all((
                0 <= antinode[0] < bounds[0],
                0 <= antinode[1] < bounds[1],
            )):
                antinodes.add(antinode)

    return len(antinodes)


def part_two(data):
    antennas, bounds = parse_map(data)
    antinodes = set()
    for antenna, locations in antennas.items():
        for a, b in permutations(locations, 2):
            found_antinodes = find_all_antinodes(a, b, bounds)
            antinodes = antinodes.union(found_antinodes)

    return len(antinodes)


data = data.splitlines()
print(part_one(data))
print(part_two(data))

with open("08.txt") as inf:
    data = inf.read().splitlines()
    print(part_one(data))
    print(part_two(data))
