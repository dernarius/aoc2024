from queue import Queue

DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))

data = """\
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE\
"""


def parse_data(data):
    lines = data.splitlines()
    positions = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            positions[(i, j)] = char

    return positions


def find_regions(positions):
    cp = positions.copy()
    while len(cp):
        pos, looking_for = next(iter(cp.items()))
        region = set()
        queue = Queue()
        queue.put(pos)
        while queue.qsize() > 0:
            poss = queue.get()
            if poss not in cp:
                continue
            cp.pop(poss)
            region.add(poss)
            for dir in DIRECTIONS:
                next_pos = poss[0] + dir[0], poss[1] + dir[1]
                charr = cp.get(next_pos)
                # print(f"next_pos={next_pos} charr={charr} looking_for={looking_for}")
                if charr == looking_for:
                    queue.put(next_pos)

        # print(f"region={region}")
        yield region


def get_perimeter(region):
    return sum(
        (pos[0] + dir[0], pos[1] + dir[1]) not in region
        for pos in region
        for dir in DIRECTIONS
    )


def get_sides(region):
    min_i = min(i for i, j in region)
    max_i = max(i for i, j in region)
    min_j = min(j for i, j in region)
    max_j = max(j for i, j in region)

    arr = [
        [(i, j) in region for j in range(min_j - 1, max_j + 2)]
        for i in range(min_i - 1, max_i + 2)
    ]

    sides = 0
    for row_a, row_b in zip(arr[:-1], arr[1:]):
        prev = (False, False)
        for pair in zip(row_a, row_b):
            if prev != pair:
                if pair in ((True, False), (False, True)):
                    sides += 1
                prev = pair

    for col_idx_a, col_idx_b in zip(range(len(arr[0])), range(len(arr[0]))):
        col_a = [col[col_idx_a] for col in arr]
        col_b = [col[col_idx_b] for col in arr]
        prev = (False, False)
        for pair in zip(col_a, col_b):
            if prev != pair:
                if pair in ((True, False), (False, True)):
                    sides += 1
                prev = pair

    return sides



def part_one(data):
    positions = parse_data(data)
    return sum(
        get_perimeter(region) * len(region)
        for region in find_regions(positions)
    )


def part_two(data):
    positions = parse_data(data)
    return sum(
        get_sides(region) * len(region)
        for region in find_regions(positions)
    )


# print(part_one(data))
# print(part_two(data))


with open("12.txt") as inf:
    data = inf.read()
    print(part_one(data))
    print(2 * part_two(data))  # UwU
