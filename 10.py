data = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732\
"""


def parse_data(data):
    return [
        [int(x) for x in line]
        for line in data.splitlines()
    ]


def find_trailheads(data):
    return [
        (i, j)
        for i, line in enumerate(data)
        for j, char in enumerate(line)
        if char == 0
    ]


def walk(data, pos):
    bounds = len(data), len(data[0])

    my_value = data[pos[0]][pos[1]]
    if my_value == 9:
        return {pos}

    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    ends = set()
    for dir in directions:
        new = pos[0] + dir[0], pos[1] + dir[1]
        if 0 <= new[0] < bounds[0] and 0 <= new[1] < bounds[1] and data[new[0]][new[1]] == my_value + 1:
            ends = ends.union(walk(data, new))

    return ends


def walk2(data, pos):
    bounds = len(data), len(data[0])

    my_value = data[pos[0]][pos[1]]
    if my_value == 9:
        return 1

    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    ends = 0
    for dir in directions:
        new = pos[0] + dir[0], pos[1] + dir[1]
        if 0 <= new[0] < bounds[0] and 0 <= new[1] < bounds[1] and data[new[0]][new[1]] == my_value + 1:
            ends += walk2(data, new)

    return ends


def part_one(data):
    data = parse_data(data)
    trailheads = find_trailheads(data)
    return sum(len(walk(data, trailhead)) for trailhead in trailheads)


def part_two(data):
    data = parse_data(data)
    trailheads = find_trailheads(data)
    return sum(walk2(data, trailhead) for trailhead in trailheads)
    

# print(part_one(data))
# print(part_two(data))

with open("10.txt") as inf:
    data = inf.read()
    print(part_one(data))
    print(part_two(data))
