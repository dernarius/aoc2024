import re


def part_one(data):
    i_max = 103
    j_max = 101

    quadrants = [0, 0, 0, 0]

    pattern = re.compile(r"p=(-?[0-9]+),(-?[0-9]+) v=(-?[0-9]+),(-?[0-9]+)")
    bots = re.findall(pattern, data)

    for bot in bots:
        p_j, p_i, v_j, v_i = (int(x) for x in bot)

        p_j_final = (p_j + v_j * 100) % j_max
        p_i_final = (p_i + v_i * 100) % i_max

        quadrant = 0
        if 0 <= p_j_final <= 49 and 0 <= p_i_final <= 50:
            quadrants[0] += 1
        if 0 <= p_j_final <= 49 and 52 <= p_i_final <= 102:
            quadrants[1] += 1
        if 51 <= p_j_final <= 100 and 0 <= p_i_final <= 50:
            quadrants[2] += 1
        if 51 <= p_j_final <= 100 and 52 <= p_i_final <= 102:
            quadrants[3] += 1

    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


with open("14.txt") as inf:
    data = inf.read()
    print(part_one(data))
