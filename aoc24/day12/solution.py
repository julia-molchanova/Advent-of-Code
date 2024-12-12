from collections import defaultdict


def parse_data(lines: list[str]):
    return lines, len(lines), len(lines[0])


steps = [[0, -1], [0, 1], [-1, 0], [1, 0]]


def solve_part1(garden: list[str], m: int, n: int):
    ans = 0
    visited = set()
    for i in range(m):
        for j in range(n):
            if (i, j) in visited:
                continue
            region = {(i, j)}
            to_visit = [(i, j)]
            plant = garden[i][j]
            perimeter = 0

            while len(to_visit) > 0:
                ci, cj = to_visit.pop()

                for di, dj in steps:
                    ni, nj = ci + di, cj + dj
                    if ni < 0 or ni >= m or nj < 0 or nj >= n:
                        perimeter += 1
                        continue
                    if (ni, nj) in region:
                        continue
                    if garden[ni][nj] == plant:
                        to_visit.append((ni, nj))
                        region.add((ni, nj))
                    else:
                        perimeter += 1

            ans += perimeter * len(region)
            visited |= region

    return ans


def solve_part2(garden: list[str], m: int, n: int):
    ans = 0

    visited = set()
    for i in range(m):
        for j in range(n):
            if (i, j) in visited:
                continue
            region = {(i, j)}
            to_visit = [(i, j)]
            plant = garden[i][j]
            sides = defaultdict(set)

            while len(to_visit) > 0:
                ci, cj = to_visit.pop()

                for di, dj in steps:
                    ni, nj = ci + di, cj + dj
                    if ni < 0 or ni >= m or nj < 0 or nj >= n:
                        sides[(di, dj)].add((ci, cj))
                        continue
                    if (ni, nj) in region:
                        continue
                    if garden[ni][nj] == plant:
                        to_visit.append((ni, nj))
                        region.add((ni, nj))
                    else:
                        sides[(di, dj)].add((ci, cj))

            sides_num = 0
            for di, dj in steps:
                side_type = sides[(di, dj)]
                while len(side_type) > 0:
                    sides_num += 1
                    ci, cj = side_type.pop()

                    for si, sj in steps:
                        # remove everything that forms a line
                        if abs(si) == abs(di):
                            continue
                        ti, tj = ci, cj

                        while (ti + si, tj + sj) in side_type:
                            side_type.remove((ti + si, tj + sj))
                            ti += si
                            tj += sj

            ans += sides_num * len(region)
            visited |= region

    return ans
