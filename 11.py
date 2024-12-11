data = "125 17"

CACHE_UP_TO = 100000


def memoize(func):
    cache = [[0 for _ in range(76)] for _ in range(CACHE_UP_TO)]

    def f(inp, il):
        nonlocal func
        nonlocal cache
        if inp >= CACHE_UP_TO:
            return func(inp, il)
        stored = cache[inp][il]
        if stored == 0:
            result = func(inp, il)
            cache[inp][il] = result
            return result
        else:
            return stored
    return f


def blink(li):
    i = 0
    while i < len(li):
        if li[i] == 0:
            li[i] = 1
        elif len(s := str(li[i])) % 2 == 0:
            mid = len(s) // 2
            li[i] = int(s[:mid])
            li.insert(i + 1, int(s[mid:]))
            i += 1
        else:
            li[i] *= 2024
        i += 1


@memoize
def walk(inp, il):
    if il == 0:
        return 1

    if inp == 0:
        return walk(1, il - 1)
    elif len(s := str(inp)) % 2 == 0:
        mid = len(s) // 2
        return walk(int(s[:mid]), il - 1) + walk(int(s[mid:]), il - 1)
    else:
        return walk(inp * 2024, il - 1)


def part_one(data):
    data = [int(x) for x in data.split()]
    for i in range(25):
        blink(data)
    print(len(data))


def part_two(data):
    data = [int(x) for x in data.split()]
    iters = 75
    print(sum(walk(x, iters) for x in data))

# print(part_one(data))


with open("11.txt") as inf:
    data = inf.read()
    part_one(data)
    part_two(data)
