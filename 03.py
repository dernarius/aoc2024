import re

p = re.compile("mul[(]([1-9][0-9]*),([1-9][0-9]*)[)]")

data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

ret = 0
with open("03.txt") as inf:
    data = inf.read()
    for a, b in re.findall(p, data):
        a, b = int(a), int(b)
        ret += a * b

    print(ret)


ret = 0
with open("03.txt") as inf:
    data = inf.read()
    segments = data.split("do()")
    for segment in segments:
        enabled = segment.split("don't()")[0]
        for a, b in re.findall(p, enabled):
            a, b = int(a), int(b)
            ret += a * b

    print(ret)
