from collections import deque, defaultdict
import time
from itertools import product


def parse_data(lines: list[str]):
    lines = [list(x) for x in lines]
    si, sj = None, None
    ei, ej = None, None
    m, n = len(lines), len(lines[0])
    for i in range(m):
        for j in range(n):
            if lines[i][j] == "S":
                si, sj = i, j
                lines[i][j] = "."
            if lines[i][j] == "E":
                ei, ej = i, j
                lines[i][j] = "."
    return ei, ej, si, sj, m, n, lines


steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def compute_times(si: int, sj: int, m: int, n: int, lines: list[str]) -> int:
    to_visit = deque([(si, sj, 0)])
    costs = {(si, sj): 0}
    while len(to_visit) > 0:
        i, j, cost = to_visit.popleft()

        for di, dj in steps:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= m or nj >= n:
                continue

            if lines[ni][nj] == "#":
                continue

            new_el = (ni, nj, cost + 1)
            if (ni, nj) not in costs:
                to_visit.append(new_el)
                costs[(ni, nj)] = cost + 1

    return costs


def solve_part1(
    ei: int, ej: int, si: int, sj: int, m: int, n: int, lines: list[str]
) -> int:
    times_from_start = compute_times(si, sj, m, n, lines)
    times_from_end = compute_times(ei, ej, m, n, lines)
    honest = times_from_start[(ei, ej)]
    print(honest)
    skips = defaultdict(int)
    ans = 0
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if lines[i][j] != "#":
                continue
            for di1, dj1 in steps:
                for di2, dj2 in steps:
                    if di1 == di2 and dj1 == dj2:
                        continue
                    ni1, nj1 = i + di1, j + dj1
                    ni2, nj2 = i + di2, j + dj2
                    if lines[ni1][nj1] != "." or lines[ni2][nj2] != ".":
                        continue
                    res = times_from_start[(ni1, nj1)] + times_from_end[(ni2, nj2)] + 2
                    if res <= max(honest - 100, 84):
                        ans += 1
                        skips[honest - res] += 1

    if m < 100:
        print(sorted(skips.items()))

    return ans


def print_time(user_function):
    def decorator(*args, **kwargs):
        start = time.time()
        res = user_function(*args, **kwargs)
        print(time.time() - start)
        return res

    return decorator


@print_time
def solve_part2(ei: int, ej: int, si: int, sj: int, m: int, n: int, lines: list[str]):
    times_from_start = compute_times(si, sj, m, n, lines)
    times_from_end = compute_times(ei, ej, m, n, lines)
    honest = times_from_start[(ei, ej)]

    skips = defaultdict(int)
    ans = 0
    for i1, j1 in product(range(1, m - 1), range(1, n - 1)):
        if lines[i1][j1] != ".":
            continue

        for i2, j2 in product(range(i1 - 21, i1 + 21), range(j1 - 21, j1 + 21)):
            if i2 < 0 or i2 >= m or j2 < 0 or j2 >= n or lines[i2][j2] != ".":
                continue

            diff = abs(i1 - i2) + abs(j1 - j2)

            if diff > 20:
                continue

            res = times_from_start[(i1, j1)] + times_from_end[(i2, j2)] + diff
            if res <= max(honest - 100, 34):
                ans += 1
                skips[honest - res] += 1

    if m < 100:
        print(sorted(skips.items()))

    return ans
