import re
from collections import defaultdict


def parse_data(lines: list[str]):
    # takes lines of the input, processes data into data structures for for the task
    data = defaultdict(list)
    pattern = re.compile(r"\d+")
    for i, line in enumerate(lines):
        numbers = pattern.findall(line)
        data[i % 4].append([int(x) for x in numbers])

    return data[0], data[1], data[2]


def solve_part1(
    buttons_a: list[list[int]], buttons_b: list[list[int]], prize: list[list[int]]
):
    ans = 0

    for (xa, ya), (xb, yb), (x, y) in zip(buttons_a, buttons_b, prize):
        if xa * yb == ya * xb:
            if x % xb == 0 and y % yb == 0 and x // xb == y // yb:
                print("Even!")
                ans += x // xb
            continue
        b = (xa * y - ya * x) // (xa * yb - ya * xb)
        if b * (xa * yb - ya * xb) != xa * y - ya * x:
            continue
        a = (x - b * xb) // xa
        if xa * a != x - b * xb:
            continue
        if a > 100 or b > 100:
            continue
        ans += b + 3 * a

    return ans


def solve_part2(
    buttons_a: list[list[int]], buttons_b: list[list[int]], prize: list[list[int]]
):
    ans = 0

    for (xa, ya), (xb, yb), (sx, sy) in zip(buttons_a, buttons_b, prize):
        x, y = sx + 10000000000000, sy + 10000000000000
        if xa * yb == ya * xb:
            if x % xb == 0 and y % yb == 0 and x // xb == y // yb:
                print("Even!")
                ans += x // xb
            continue
        b = (xa * y - ya * x) // (xa * yb - ya * xb)
        if b * (xa * yb - ya * xb) != xa * y - ya * x:
            continue
        a = (x - b * xb) // xa
        if xa * a != x - b * xb:
            continue

        ans += b + 3 * a

    return ans
