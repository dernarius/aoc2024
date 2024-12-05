from collections import Counter

left, right = [], []

with open("01.txt") as inf:
    for line in inf:
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))

left.sort()
right.sort()

print(sum(abs(a - b) for a, b in zip(left, right)))

ct = Counter(right)

print(sum(x * ct.get(x, 0) for x in left))
