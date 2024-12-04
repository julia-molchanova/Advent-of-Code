def parse_data(lines: list[str]):
    # takes lines of the input, processes data into data structures for for the task
    return lines, None


steps = [-1, 0, 1]


def solve_part1(lines: list[str], dummy):
    ans = 0

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] != "X":
                continue
            for di in steps:
                for dj in steps:
                    ni, nj = i + 3 * di, j + 3 * dj
                    if ni < 0 or nj < 0 or ni >= len(lines) or nj >= len(lines[0]):
                        continue
                    word = [lines[i + di * k][j + dj * k] for k in range(4)]
                    if "".join(word) == "XMAS":
                        ans += 1

    return ans


def solve_part2(lines: str, dummy):
    ans = 0

    cross_template = {"M", "S"}

    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[0]) - 1):
            # looking for the central A
            if lines[i][j] != "A":
                continue
            cross_line1 = {lines[i - 1][j - 1], lines[i + 1][j + 1]}
            cross_line2 = {lines[i - 1][j + 1], lines[i + 1][j - 1]}
            if cross_line1 == cross_template and cross_line2 == cross_template:
                ans += 1
    return ans
