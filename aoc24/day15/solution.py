from collections import deque


def parse_data(lines: list[str]):
    i = 0
    grid = []
    while lines[i] != "":
        grid.append(list(lines[i]))
        i += 1
    ri, rj = None, None
    for p in range(len(grid)):
        for j, c in enumerate(grid[p]):
            if c == "@":
                ri, rj = p, j
                grid[p][j] = "."
    return grid, len(grid), len(grid[0]), "".join(lines[i + 1 :]), ri, rj


steps = {"^": [-1, 0], "v": [1, 0], "<": [0, -1], ">": [0, 1]}


def solve_part1(
    input_grid: list[list[str]], m: int, n: int, commands: str, ri: int, rj: int
):
    grid = [x.copy() for x in input_grid]

    for c in commands:
        di, dj = steps[c]
        moves_num = 0
        ni, nj = ri + di, rj + dj
        while grid[ni][nj] == "O":
            moves_num += 1
            ni += di
            nj += dj
        if grid[ni][nj] == "#":
            continue
        while moves_num >= 0:
            grid[ni][nj] = grid[ni - di][nj - dj]
            ni -= di
            nj -= dj
            moves_num -= 1
        ri += di
        rj += dj

    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "O":
                ans += i * 100 + j

    return ans


brackets = {"[": 1, "]": -1}


def solve_part2(
    input_grid: list[list[str]], m: int, n: int, commands: str, ri: int, rj: int
):
    grid = []
    for line in input_grid:
        new_line = []
        for x in line:
            if x == "O":
                new_line += ["[", "]"]
            else:
                new_line.append(x)
                new_line.append(x)
        grid.append(new_line)
    rj *= 2

    for c in commands:
        di, dj = steps[c]
        ni, nj = ri + di, rj + dj
        next_line = [(ni, nj)]
        stuck = False
        to_move = []
        while not stuck and len(next_line) > 0:
            new_line = set()
            to_move_this_line = set()
            for ci, cj in next_line:
                if grid[ci][cj] == "#":
                    stuck = True
                    break
                for b in brackets:
                    if grid[ci][cj] == b:
                        shift = brackets[b]
                        if di == 0:
                            shift = 0
                        new_line.add((ci + di, cj + dj))
                        new_line.add((ci + di, cj + shift + dj))
                        to_move_this_line.add((ci, cj))
                        to_move_this_line.add((ci, cj + shift))
            next_line = list(new_line)
            to_move += list(to_move_this_line)

        if stuck:
            continue

        for i, j in to_move[::-1]:
            grid[i + di][j + dj] = grid[i][j]
            grid[i][j] = "."

        ri += di
        rj += dj
        grid[ri][rj] = "."

    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "[":
                ans += i * 100 + j

    if len(commands) < 1000:
        for line in grid:
            print("".join(line))

    return ans
