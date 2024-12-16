import heapq


def parse_data(lines: list[str]):
    i = 0
    grid = []
    for line in lines:
        grid.append(list(line))
        i += 1
    ri, rj = None, None
    for p in range(len(grid)):
        for j, c in enumerate(grid[p]):
            if c == "S":
                ri, rj = p, j
                grid[p][j] = "."
    return grid, len(grid), len(grid[0]), ri, rj


steps = [[0, 1], [-1, 0], [0, -1], [1, 0]]


def find_shortest_path(grid: list[list[str]], ri: int, rj: int):
    queue = [(0, ri, rj, 0)]
    costs = {(ri, rj, 0): 0}
    paths = {(ri, rj, 0): {(ri, rj)}}
    best_cost = 10**9
    best_paths = set()

    while len(queue) > 0:
        cost, i, j, d = heapq.heappop(queue)
        if cost > best_cost:
            break

        if costs[(i, j, d)] < cost:
            continue

        if grid[i][j] == "E":
            best_cost = cost
            best_paths |= paths[(i, j, d)]
            continue
        path = paths[(i, j, d)]

        ni, nj = i + steps[d][0], j + steps[d][1]
        new_path = path | {(ni, nj)}

        if grid[ni][nj] != "#" and costs.get((ni, nj, d), 10**9) >= cost + 1:

            if cost + 1 < costs.get((ni, nj, d), 10**9):
                heapq.heappush(queue, (cost + 1, ni, nj, d))
                paths[(ni, nj, d)] = new_path
                costs[(ni, nj, d)] = cost + 1
            else:
                paths[(ni, nj, d)] |= new_path

        for k in range(1, 4):
            nd = (d + k) % 4
            new_cost = cost + 1000 * min(k, 4 - k)
            if costs.get((i, j, nd), 10**9) >= new_cost:

                if new_cost < costs.get((i, j, nd), 10**9):
                    paths[(i, j, nd)] = path
                    costs[(i, j, nd)] = new_cost
                    heapq.heappush(queue, (new_cost, i, j, nd))
                else:
                    paths[(i, j, nd)] |= path

    return best_cost, best_paths


def solve_part1(input_grid: list[list[str]], m: int, n: int, ri: int, rj: int):
    return find_shortest_path(input_grid, ri, rj)[0]


def solve_part2(input_grid: list[list[str]], m: int, n: int, ri: int, rj: int):
    _, best_paths = find_shortest_path(input_grid, ri, rj)
    return len(best_paths)
