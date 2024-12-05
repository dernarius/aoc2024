from collections import defaultdict

import networkx as nx

data = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47\
"""


def part_one(data):
    rules, updates = data.split("\n\n")

    rules_dict = defaultdict(lambda: (set(), set()))

    for rule in rules.splitlines():
        before, after = rule.split('|')
        before, after = int(before), int(after)
        rules_dict[after][0].add(before)
        rules_dict[before][1].add(after)

    ret = 0
    for update in updates.splitlines():
        update = [int(x) for x in update.split(',')]
        for i in range(len(update)):
            before = set(update[:i])
            after = set(update[i + 1:])
            if any((
                before & rules_dict[update[i]][1],
                after & rules_dict[update[i]][0],
            )):
                break
        else:
            ret += update[len(update) // 2]

    return ret


def part_two(data):
    rules, updates = data.split("\n\n")

    rules_dict = defaultdict(lambda: (set(), set()))

    for rule in rules.splitlines():
        before, after = rule.split('|')
        before, after = int(before), int(after)
        rules_dict[after][0].add(before)
        rules_dict[before][1].add(after)

    ret = 0
    for update in updates.splitlines():
        update = [int(x) for x in update.split(',')]
        for i in range(len(update)):
            before = set(update[:i])
            after = set(update[i + 1:])
            if any((
                before & rules_dict[update[i]][1],
                after & rules_dict[update[i]][0],
            )):
                ret += fix_pages(rules_dict, update)
                break

    return ret


def fix_pages(rules_dict, update):
    st = set(update)
    cp = {k: (b & st, a & st) for k, (b, a) in rules_dict.items() if k in st}
    G = nx.DiGraph()
    for m, (b, a) in cp.items():
        for bb in b:
            G.add_edge(bb, m)
        for aa in a:
            G.add_edge(m, aa)

    for node in G.nodes():
        if len(nx.ancestors(G, node)) == len(nx.descendants(G, node)):
            return node


with open("05.txt") as inf:
    data = inf.read()
    print(part_one(data))
    print(part_two(data))
