from collections import defaultdict

data = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...\
"""

data_my = """\
.....
..#..
...#.
.....
..^..
.....\
"""


def next_direction(direction):
    match direction:
        case (-1, 0):
            return (0, 1)
        case (0, 1):
            return (1, 0)
        case (1, 0):
            return (0, -1)
        case (0, -1):
            return (-1, 0)


def parse_map(data):
    obstacle_map = data.splitlines()
    for i in range(len(obstacle_map)):
        for j in range(len(obstacle_map[0])):
            if obstacle_map[i][j] == "^":
                starting_pos = (i, j)

    return obstacle_map, starting_pos


def generate_positions(data, starting_pos, starting_dir=(-1, 0)):
    pos = starting_pos
    dir = starting_dir
    while 0 <= pos[0] < len(data) and 0 <= pos[1] < len(data[0]):
        yield pos, dir
        while True:
            next_pos = pos[0] + dir[0], pos[1] + dir[1]
            try:
                if data[next_pos[0]][next_pos[1]] != "#":
                    break
                else:
                    dir = next_direction(dir)
                    yield pos, dir
            except IndexError:
                break
        pos = next_pos


def obstacle_locations(data):
    obstacles = set()
    for i in range(len(data)):
        for j in range(len(data[0])):
            try:
                if data[i][j] == "#":
                    obstacles.add((i, j))
            except IndexError:
                pass

    return obstacles


def part_one(data):
    data, starting_pos = parse_map(data)
    return len({pos for pos, dir in generate_positions(data, starting_pos)})


def part_two(data):
    data, starting_pos = parse_map(data)
    pos_dir = defaultdict(set)
    existing_obstacles = obstacle_locations(data)
    obstacles = set()
    for pos, dir in generate_positions(data, starting_pos):
        # print(f"pos={pos} dir={dir}")
        pot_obstacle_pos = pos[0] + dir[0], pos[1] + dir[1]
        if pot_obstacle_pos in existing_obstacles:
            continue
        if not (0 <= pot_obstacle_pos[0] < len(data) and 0 <= pot_obstacle_pos[1] < len(data[0])):
            continue
        pos_dir[pos].add(dir)
        temp_pos_dir = defaultdict(set)
        mod_data = [list(x) for x in data]
        mod_data[pot_obstacle_pos[0]][pot_obstacle_pos[1]] = "#"
        for poss, dirr in generate_positions(mod_data, pos, starting_dir=next_direction(dir)):
            # print(f"\tpos={poss} dir={dirr}")
            if dirr in pos_dir[poss] or dirr in temp_pos_dir[poss]:
                obstacles.add(pot_obstacle_pos)
                # print(f"\tadded {pot_obstacle_pos}")
                break
            temp_pos_dir[poss].add(dirr)

    obstacles -= {starting_pos}

    return obstacles


# obstacles = part_two(data)
# print(obstacles)
# assert obstacles == {(6, 3), (7, 6), (7, 7), (8, 1), (8, 3), (9, 7)}

# part_two(data_my)

with open("06.txt") as inf:
    data = inf.read()
    print(part_one(data))
    print(len(part_two(data)))
