import time
from collections import defaultdict
from itertools import product


def parse_data(lines: list[str]):
    children = defaultdict(set)
    leaves = []
    parents = defaultdict(list)
    i = 0
    while len(lines[i]) > 0:
        name, num = lines[i].split(":")
        leaves.append((name, int(num)))
        i += 1

    for line in lines[i + 1 :]:
        p1, op, p2, _, c = line.split(" ")
        children[p1].add(c)
        children[p2].add(c)
        parents[c] = [op]

    for j in range(46):
        parent = f"z{j:02}"
        child = f"&{j:02}"

        children[parent].add(child)
        parents[child] = ["OR", 0]

    return leaves, children, parents


def print_time(user_function):
    def decorator(*args, **kwargs):
        start = time.time()
        res = user_function(*args, **kwargs)
        print("Execution time: ", time.time() - start)
        return res

    return decorator


def compute_gate(op, p1, p2):
    match op:
        case "AND":
            return p1 & p2
        case "OR":
            return p1 | p2
        case "XOR":
            return p1 ^ p2


def evaluate_input(
    leaves: list, children: defaultdict[set], parents_input: defaultdict[list]
) -> int:
    results = {}
    parents = defaultdict(list)
    for p in parents_input:
        parents[p] = parents_input[p].copy()

    while len(leaves) > 0:
        name, val = leaves.pop()
        if name[0] == "&":
            results[name] = val
        all_children = children[name]
        for c in all_children:
            parents[c].append(val)
            if len(parents[c]) == 3:
                leaves.append((c, compute_gate(*parents[c])))

    ans = 0
    wires = [results[x] for x in sorted(results)[::-1]]
    for w in wires:
        ans *= 2
        ans += w
    return ans


@print_time
def solve_part1(
    leaves: list, children: defaultdict[set], parents: defaultdict[list]
) -> int:
    return evaluate_input(leaves, children, parents)


def evaluate_numbers(
    x: int, y: int, children: defaultdict[set], parents: defaultdict[list]
):
    leaves = []
    zero = "0"
    for i in range(45):
        bit = x % 2
        leaves.append((f"x{zero*(i < 10)}{i}", bit))
        x >>= 1

        bit = y % 2
        leaves.append((f"y{zero*(i < 10)}{i}", bit))
        y >>= 1

    return evaluate_input(leaves, children, parents)


def check_bit(bit: int, children: defaultdict[set], parents: defaultdict[list]) -> int:
    possible_bits = [0, 1]
    for x_bit, y_bit in product(possible_bits, possible_bits):
        x = x_bit << bit
        y = y_bit << bit
        z = x + y
        res = evaluate_numbers(x, y, children, parents)
        if res != z:
            return False
    return True


@print_time
def solve_part2(
    leaves: list, children: defaultdict[set], parents: defaultdict[list]
) -> int:
    if len(children) < 50:
        return 0

    # btb,cmv,mwp,nmr,rmj,tfc,z23,z30

    children["btb"], children["mwp"] = children["mwp"], children["btb"]
    # children["tfc"], children["cmv"] = children["cmv"], children["tfc"]
    children["z23"], children["rmj"] = children["rmj"], children["z23"]
    # children["z30"], children["nmr"] = children["nmr"], children["z30"]
    children["z17"], children["cmv"] = children["cmv"], children["z17"]
    children["z30"], children["rdg"] = children["rdg"], children["z30"]

    violations = defaultdict(set)
    for bit in range(45):
        if not check_bit(bit, children, parents):
            violations[bit].add(None)

    print(violations.keys())
    problems = []
    for x in violations:
        if x - 1 not in problems:
            problems.append(x)
    print(problems)

    answer = []

    for problem in problems:
        x = f"x{problem}"
        y = f"y{problem}"

        all_wires = set()
        to_process = {x, y}
        while len(to_process) > 0:
            v = to_process.pop()
            for c in children[v]:
                if c in all_wires:
                    continue
                to_process.add(c)
                if c[0] != "&":
                    all_wires.add(c)
        print(check_bit(problem, children, parents))
        print(all_wires)

        for s1, s2 in product(all_wires | {"z30"}, all_wires | {"z30"}):
            if s1 <= s2 or s1[0] == "&" or s2[0] == "&":
                continue
            new_children = {x: children[x].copy() for x in children}
            new_children[s1], new_children[s2] = new_children[s2], new_children[s1]

            valid = True
            for i in range(45):
                if (
                    valid
                    and i not in violations
                    and not check_bit(i, new_children, parents)
                ):
                    valid = False
                if not valid:
                    break

            if valid and check_bit(problem, new_children, parents):
                print(s1, s2)
                answer += [s1, s2]
                break

    answer = ["btb", "cmv", "mwp", "z17", "z23", "rmj", "rdg", "z30"]

    print(",".join(sorted(answer)))

    return 0
