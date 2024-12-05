data = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".splitlines()

def parse_report(line):
    return [int(x) for x in line.split()]


def is_report_increasing(report):
    for a, b in zip(report[:-1], report[1:]):
        if not(1 <= b - a <= 3):
            return False
    return True


def is_report_decreasing(report):
    for a, b in zip(report[:-1], report[1:]):
        if not (1 <= a - b <= 3):
            return False
    return True


count = 0
with open("02.txt") as inf:
    for line in inf:
        report = parse_report(line)
        if not report:
            continue
        result = int(is_report_increasing(report) or is_report_decreasing(report))
        count += result

    print(count)


def is_report_increasing_skip(report):
    skip_next = False
    skips = 0
    for a, b in zip(report[:-1], report[1:]):
        if skip_next:
            skip_next = False
            continue
        if not 1 <= b - a <= 3:
            skip_next = True
            skips += 1
        if skips > 1:
            return False
    return True


def is_report_decreasing_skip(report):
    skip_next = False
    skips = 0
    for a, b in zip(report[:-1], report[1:]):
        if skip_next:
            skip_next = False
            continue
        if not 1 <= a - b <= 3:
            skip_next = True
            skips += 1
        if skips > 1:
            return False
    return True


def check_report(report):
    if is_report_decreasing(report) or is_report_increasing(report):
        return True
    for i in range(len(report)):
        cp = report.copy()
        cp.pop(i)
        if is_report_decreasing(cp) or is_report_increasing(cp):
            return True
    return False


count = 0
with open("02.txt") as inf:
    for line in inf:
        report = parse_report(line)
        if not report:
            continue
        # result = any((
        #     is_report_decreasing_skip(report),
        #     is_report_increasing_skip(report),
        #     is_report_decreasing(report[1:]),
        #     is_report_increasing(report[1:]),
        #     is_report_decreasing(report[:-1]),
        #     is_report_increasing(report[:-1]),
        # ))
        result = check_report(report)
        count += result

    print(count)

