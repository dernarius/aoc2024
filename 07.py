import itertools as it


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def concat(a, b):
    return int(str(a) + str(b))


def can_be_combined(total, operands, operators):
    combinations = it.product(operators, repeat=len(operands) - 1)
    for combination in combinations:
        subtotal = operands[0]
        for operator, operand in zip(combination, operands[1:]):
            subtotal = operator(subtotal, operand)
        if subtotal == total:
            return True
    return False


def parse_data(data):
    data = data.splitlines()
    ret = []
    for line in data:
        total, operands = line.split(":")
        total = int(total)
        operands = [int(x) for x in operands.strip().split()]
        ret.append((total, operands))

    return ret


def part_one(lines):
    return sum(
        total
        for total, operands in lines
        if can_be_combined(total, operands, (add, multiply))
    )


def part_two(lines):
    return sum(
        total
        for total, operands in lines
        if can_be_combined(total, operands, (add, multiply, concat))
    )


with open("07.txt") as inf:
    lines = parse_data(inf.read())
    print(part_one(lines))
    print(part_two(lines))
