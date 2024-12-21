from collections import deque, defaultdict
import time
import re
from functools import cache
import heapq
from itertools import product


def parse_data(lines: list[str]):
    pattern = re.compile(r"\d+")
    weights = []
    for line in lines:
        weights.append(int(pattern.findall(line)[0]))
    return weights, lines


steps = {"^": [-1, 0], "v": [1, 0], "<": [0, -1], ">": [0, 1]}
directional_keypad = ["&&&&&", "&&^A&", "&<v>&", "&&&&&"]
numerical_keypad = ["&&&&&", "&789&", "&456&", "&123&", "&&0A&", "&&&&&"]

cost_manual = {}
directional_symbols = {"^", ">", "<", "v", "A"}
for c1, c2 in product(directional_symbols, directional_symbols):
    cost_manual[(c1, c2)] = 1


def print_time(user_function):
    def decorator(*args, **kwargs):
        start = time.time()
        res = user_function(*args, **kwargs)
        print(time.time() - start)
        return res

    return decorator


def cost_to_reach(target_keypad, source_costs, start_symbol, target_symbol):
    # Dijkstra
    si, sj = None, None
    for i, line in enumerate(target_keypad):
        for j, char in enumerate(line):
            if char == start_symbol:
                si, sj = i, j

    to_visit = [(0, si, sj, "A")]
    computed_costs = {(si, sj, "A"): 0}
    answers = []
    while len(to_visit) > 0:
        cost, i, j, prev_step = heapq.heappop(to_visit)
        if cost > computed_costs[(i, j, prev_step)]:
            continue

        if target_keypad[i][j] == target_symbol:
            answers.append(cost + source_costs[(prev_step, "A")])

        for step in steps:
            di, dj = steps[step]
            ni, nj = i + di, j + dj
            if target_keypad[ni][nj] == "&":
                continue

            new_cost = cost + source_costs[(prev_step, step)]
            if (ni, nj, step) in computed_costs and computed_costs[
                (ni, nj, step)
            ] <= new_cost:
                continue
            heapq.heappush(to_visit, (new_cost, ni, nj, step))
            computed_costs[(ni, nj, step)] = new_cost

    return min(answers)


def compute_costs_for_next(target_keypad, source_costs):
    costs = {}

    target_set = set()
    for line in target_keypad:
        target_set |= set(line)
    target_set.remove("&")

    for c1, c2 in product(target_set, target_set):
        cost = cost_to_reach(target_keypad, source_costs, c1, c2)
        costs[(c1, c2)] = cost

    return costs


@cache
@print_time
def compute_costs(intermediate_keypads):
    prev_costs = cost_manual
    for _ in range(intermediate_keypads):
        prev_costs = compute_costs_for_next(directional_keypad, prev_costs)
    manual_to_numerical = compute_costs_for_next(numerical_keypad, prev_costs)
    return manual_to_numerical


def solve_part1(weights: list[int], lines: list[str]) -> int:
    costs = compute_costs(2)

    ans = 0

    for w, s in zip(weights, lines):
        full_line = "A" + s

        line_res = 0
        for c1, c2 in zip(full_line[:-1], full_line[1:]):
            line_res += costs[(c1, c2)]

        ans += w * line_res

    return ans


def solve_part2(weights: list[int], lines: list[str]):
    costs = compute_costs(25)

    ans = 0

    for w, s in zip(weights, lines):
        full_line = "A" + s

        line_res = 0
        for c1, c2 in zip(full_line[:-1], full_line[1:]):
            line_res += costs[(c1, c2)]

        ans += w * line_res

    return ans
