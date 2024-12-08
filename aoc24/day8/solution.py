from collections import defaultdict


def parse_data(lines: list[str]):
    # takes lines of the input, processes data into data structures for for the task
    antennas = defaultdict(set)

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == ".":
                continue
            antennas[c].add((i, j))

    return antennas, len(lines), len(lines[0])


def solve_part1(antennas: dict, m: int, n: int):
    antinodes = set()

    for c in antennas:
        for i1, j1 in antennas[c]:
            for i2, j2 in antennas[c]:
                if i1 == i2 and j1 == j2:
                    continue
                ni = i1 - (i2 - i1)
                nj = j1 - (j2 - j1)
                if ni < 0 or nj < 0 or ni >= m or nj >= n:
                    continue
                antinodes.add((ni, nj))

    return len(antinodes)


def solve_part2(antennas: dict, m: int, n: int):
    antinodes = set()

    for c in antennas:
        for i1, j1 in antennas[c]:
            for i2, j2 in antennas[c]:
                if i1 == i2 and j1 == j2:
                    continue
                di = i2 - i1
                dj = j2 - j1
                ni = i1
                nj = j1
                while not (ni < 0 or nj < 0 or ni >= m or nj >= n):
                    antinodes.add((ni, nj))
                    ni -= di
                    nj -= dj

    return len(antinodes)
