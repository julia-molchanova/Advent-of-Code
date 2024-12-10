def parse_data(lines: list[str]):
    map = []
    heads = []
    for i, line in enumerate(lines):
        row = []
        for j, num in enumerate([int(x) for x in line]):
            if num == 0:
                heads.append((i, j))
            row.append(num)
        map.append(row)

    return map, heads, len(map), len(map[0])


steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def solve_part1(map: list[list[int]], heads: list[tuple[int]], m: int, n: int):
    ans = 0
    for head_i, head_j in heads:
        to_visit = [(head_i, head_j)]
        visited = set()
        visited_nines = set()
        while len(to_visit) > 0:
            i, j = to_visit.pop()

            for di, dj in steps:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= m or nj >= n:
                    continue
                if map[ni][nj] != map[i][j] + 1 or (ni, nj) in visited:
                    continue
                to_visit.append((ni, nj))
                visited.add((ni, nj))
                if map[ni][nj] == 9:
                    visited_nines.add((ni, nj))

        ans += len(visited_nines)

    return ans


def solve_part2(map: list[list[int]], heads: list[tuple[int]], m: int, n: int):
    ans = 0
    for head_i, head_j in heads:
        to_visit = [[head_i, head_j, [(head_i, head_j)]]]
        visited = set()
        visited_nines = set()
        while len(to_visit) > 0:
            i, j, path = to_visit.pop()

            for di, dj in steps:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= m or nj >= n:
                    continue
                if map[ni][nj] != map[i][j] + 1:
                    continue
                new_path = path + [(ni, nj)]
                path_tuple = tuple(new_path)
                if path_tuple in visited:
                    continue
                to_visit.append([ni, nj, new_path])
                visited.add(path_tuple)
                if map[ni][nj] == 9:
                    visited_nines.add(path_tuple)

        ans += len(visited_nines)

    return ans
