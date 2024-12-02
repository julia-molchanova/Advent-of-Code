def parse_data(lines: list[str]):
    # takes lines of the input, processes data into data structures fir for the task
    reports = []
    for line in lines:
        numbers = line.split(" ")
        reports.append([int(x) for x in numbers])
    return reports, None


def check_validity(a: int, b: int, positive: bool):
    if abs(a - b) > 3:
        return False
    if positive and a >= b or not positive and a <= b:
        return False
    return True


def solve_part1(reports: list[int], dummy):
    ans = 0
    for report in reports:
        valid = True
        positive = report[1] - report[0] > 0
        for a, b in zip(report[:-1], report[1:]):
            if not check_validity(a, b, positive):
                valid = False
        if valid:
            ans += 1
    return ans


def solve_part2(reports: list[int], dummy):
    ans = 0
    for report in reports:
        valid = False
        for positive in [False, True]:
            violations = []

            for i, (a, b) in enumerate(zip(report[:-1], report[1:])):
                if not check_validity(a, b, positive):
                    violations.append(i)

            if len(violations) == 0:
                valid = True
                break

            if len(violations) == 2:
                if violations[1] - violations[0] > 1:
                    # they are not adjacent
                    continue
                # try to delete the problematic element, check it's neighbors
                if violations[1] == len(report) - 1 or check_validity(
                    report[violations[0]], report[violations[1] + 1], positive
                ):
                    valid = True
                    break

            if len(violations) == 1:
                i = violations.pop()
                for candidate in [i, i + 1]:
                    # try to delete any candidate, check the remaining neighbors
                    left = candidate - 1
                    right = candidate + 1
                    if (
                        left < 0
                        or right >= len(report)
                        or check_validity(report[left], report[right], positive)
                    ):
                        valid = True
                        break
        if valid:
            ans += 1
    return ans
