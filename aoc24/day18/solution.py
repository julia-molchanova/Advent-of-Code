import re


def parse_data(lines: list[str]):
    pattern = re.compile(r"-?\d+")
    size, cut = map(int, pattern.findall(lines[0]))
    bytes = []
    for line in lines[1:]:
        bytes.append([int(x) for x in pattern.findall(line)])
    bytes = [tuple(x) for x in bytes]

    return size, cut, bytes


steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def solve_part1(size: int, cut: int, bytes: list[list[int]]):
    obstacles = set(bytes[:cut])
    to_visit = [(0, 0, 0)]
    visited = {(0, 0)}
    while len(to_visit) > 0:
        i, j, cost = to_visit.pop(0)
        if (i, j) == (size - 1, size - 1):
            return cost

        for di, dj in steps:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= size or nj >= size:
                continue
            if (ni, nj) in obstacles or (ni, nj) in visited:
                continue
            to_visit.append((ni, nj, cost + 1))
            visited.add((ni, nj))

    return None


def solve_part2(size: int, cut: int, bytes: list[list[int]]):
    l, r = 0, len(bytes) + 1
    while r > l + 1:
        mid = l + (r - l) // 2
        res = solve_part1(size, mid, bytes)
        if res is None:
            r = mid
        else:
            l = mid
    print(bytes[l])
    return l
