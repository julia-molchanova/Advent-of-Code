def parse_data(lines: list[str]):
    # takes lines of the input, processes data into data structures for for the task
    m = len(lines)
    n = len(lines[0])
    r_i, r_j = None, None
    lines = [list(x) for x in lines]
    for i in range(m):
        for j in range(n):
            if lines[i][j] == "^":
                r_i, r_j = i, j
    return lines, m, n, r_i, r_j


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solve_part1(lines: list[str], m: int, n: int, r_i: int, r_j: int):
    ans = 1
    direction = 0

    while True:
        ni, nj = r_i + directions[direction][0], r_j + directions[direction][1]
        if ni < 0 or nj < 0 or ni >= m or nj >= n:
            break
        if lines[ni][nj] == "#":
            direction = (direction + 1) % len(directions)
            continue
        r_i, r_j = ni, nj
        if lines[r_i][r_j] == ".":
            ans += 1
            lines[r_i][r_j] = "X"

    return ans


def solve_part2(lines: list[str], m: int, n: int, rs_i: int, rs_j: int):
    ans = 0

    for i in range(m):
        for j in range(n):
            if lines[i][j] == "#" or lines[i][j] == "." or i == rs_i and j == rs_j:
                continue

            lines[i][j] = "#"
            cycled = True

            r_i, r_j = rs_i, rs_j
            direction = 0
            visited = {(r_i, r_j, direction)}

            while True:
                ni, nj = r_i + directions[direction][0], r_j + directions[direction][1]
                if ni < 0 or nj < 0 or ni >= m or nj >= n:
                    cycled = False
                    break

                if lines[ni][nj] == "#":
                    direction = (direction + 1) % len(directions)
                    continue
                r_i, r_j = ni, nj
                if (r_i, r_j, direction) in visited:
                    break
                visited.add((r_i, r_j, direction))

            lines[i][j] = "."
            if cycled:
                ans += 1

    return ans
