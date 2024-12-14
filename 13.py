import re
from typing import NamedTuple

import numpy as np
from scipy.optimize import LinearConstraint, Bounds, milp

data = """\
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279\
"""

def part_one(data, part_two=False):
    pattern = re.compile("X[+=]([0-9]+), Y[+=]([0-9]+)")
    problems = data.split("\n\n")
    summ = 0
    summm = 0
    for i, problem in enumerate(problems):
        (a_x, a_y), (b_x, b_y), (p_x, p_y) = (
            (int(s), int(t))
            for s, t in re.findall(pattern, problem)
        )

        if part_two:
            p_x += 10000000000000
            p_y += 10000000000000

        c = np.array([3, 1])
        integrality = np.array([1, 1])
        # bounds = Bounds(lb=[0, 0], ub=[100, 100])
        A_eq = np.array([[a_x, b_x], [a_y, b_y]])
        b_eq = np.array([p_x, p_y])
        lc = LinearConstraint(A=A_eq, lb=b_eq, ub=b_eq)

        res = milp(
            c=c,
            integrality=integrality,
            constraints=lc,
        )
        
        if res.success:
            summ += res.fun

        if res.status not in (0, 2):
            print(f"status={res.status} msg={res.message}")

        times_b = (p_y * a_x - p_x * a_y) / (b_y * a_x - b_x * a_y)
        times_a = (p_x - b_x * times_b) / a_x

        if times_a.is_integer() and times_b.is_integer():
            summm += times_a * 3 + times_b

    return summ, summm


# print(part_one(data))
# print(part_one(data, part_two=True))

with open("13.txt") as inf:
    data = inf.read()
    print(part_one(data))
    print(part_one(data, part_two=True))
