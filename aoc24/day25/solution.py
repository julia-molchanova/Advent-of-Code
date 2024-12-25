import time
from itertools import product
from collections import defaultdict


def parse_data(lines: list[str]):
    max_length = 7
    i = 0
    locks, keys = [], []
    while i < len(lines):
        item = defaultdict(int)
        is_lock = "." not in lines[i]
        while i < len(lines) and len(lines[i]) > 0:
            for p, c in enumerate(lines[i]):
                item[p] += 1 if c == "#" else 0
            i += 1

        i += 1

        if is_lock:
            locks.append((item.values()))
        else:
            keys.append((item.values()))

    return max_length, locks, keys


def solve_part1(max_length: int, locks: list[list[int]], keys: list[list[int]]) -> int:

    ans = 0

    for lock, key in product(locks, keys):
        valid = True
        for l, k in zip(lock, key):
            if l + k > max_length:
                valid = False
        ans += 1 if valid else 0

    return ans


def solve_part2(max_length: int, locks: list[list[int]], keys: list[list[int]]):
    ans = 0
    return ans
