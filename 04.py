data = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX\
""".splitlines()


def try_xmas(data, i, j, dir_i, dir_j):
    idxs = [(i + x * dir_i, j + x * dir_j) for x in range(4)]
    if all(
        0 <= i < len(data) and 0 <= j < len(data[0])
        for i, j in idxs
    ):
        return all(
            data[i][j] == x
            for (i, j), x in zip(idxs, "XMAS")
        )
    else:
        return False


def try_crossmas(data, i, j):
    valid = {"MMSS", "MSSM", "SSMM", "SMMS"}
    string = str.join('', (
        data[i - 1][j - 1],
        data[i - 1][j + 1],
        data[i + 1][j + 1],
        data[i + 1][j - 1],
    ))
    return string in valid


with open("04.txt") as inf:
    data = inf.read().splitlines()[:-1]
    ret = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "X":
                ret += try_xmas(data, i, j, -1, -1)
                ret += try_xmas(data, i, j, -1, 0)
                ret += try_xmas(data, i, j, -1, 1)
                ret += try_xmas(data, i, j, 0, -1)
                ret += try_xmas(data, i, j, 0, 1)
                ret += try_xmas(data, i, j, 1, -1)
                ret += try_xmas(data, i, j, 1, 0)
                ret += try_xmas(data, i, j, 1, 1)

    print(ret)

    ret = 0
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[0]) - 1):
            if data[i][j] == "A":
                ret += try_crossmas(data, i, j)

    print(ret)
