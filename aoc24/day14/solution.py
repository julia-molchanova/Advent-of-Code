import re
from collections import defaultdict


def parse_data(lines: list[str]):
    pattern = re.compile(r"-?\d+\.?\d*")
    m, n = pattern.findall(lines[0])
    positions = []
    velocities = []
    for line in lines[1:]:
        nums = pattern.findall(line)
        positions.append([int(x) for x in nums[:2]])
        velocities.append([int(x) for x in nums[2:]])
    return positions, velocities, int(m), int(n)


def solve_part1(
    inp_positions: list[list[int]], velocities: list[list[int]], m: int, n: int
):
    positions = [x.copy() for x in inp_positions]
    lengths = [m, n]
    for _ in range(100):
        for i in range(len(positions)):
            for j in range(2):
                positions[i][j] = (
                    positions[i][j] + velocities[i][j] + lengths[j]
                ) % lengths[j]

    quadrants = [[0, 0], [0, 0]]
    half_sizes = [m // 2, n // 2]
    for coords in positions:
        if coords[0] == half_sizes[0]:
            continue
        if coords[1] == half_sizes[1]:
            continue
        first_ind = 0 if coords[0] < half_sizes[0] else 1
        second_ind = 0 if coords[1] < half_sizes[1] else 1
        quadrants[first_ind][second_ind] += 1

    ans = 1
    for couple in quadrants:
        for quadrant in couple:
            ans *= quadrant

    return ans


steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def solve_part2(
    positions: list[list[int]], velocities: list[list[int]], m: int, n: int
):
    if len(positions) < 100:
        return 0
    lengths = [m, n]
    for iter in range(10000):
        for i in range(len(positions)):
            for j in range(2):
                positions[i][j] = (
                    positions[i][j] + velocities[i][j] + lengths[j]
                ) % lengths[j]
        positions_set = {(x, y) for x, y in positions}
        valid_size = 0
        for x, y in positions:
            valid = False
            for dx, dy in steps:
                if (x + dx, y + dy) in positions_set:
                    valid = True
            valid_size += 1 if valid else 0
        if valid_size > len(positions) * 2 // 3:
            print(iter + 1)
            for i in range(n):
                print(
                    "".join(
                        ["." if (j, i) not in positions_set else "#" for j in range(m)]
                    )
                )
            print("\n\n\n")

    return 0
