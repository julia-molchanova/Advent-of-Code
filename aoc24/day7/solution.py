def parse_data(lines: list[str]):
    # takes lines of the input, processes data into data structures for for the task
    answers, values = [], []
    for line in lines:
        ans, vals = line.split(":")
        answers.append(int(ans))
        values.append([int(x) for x in vals[1:].split(" ")])
    return answers, values


def get_possible_results(values: list[int], part: int = 1):
    if len(values) == 1:
        return [values[0]]
    shorter_res = get_possible_results(values[:-1], part)
    res = []
    for r in shorter_res:
        res.append(r * values[-1])
        res.append(r + values[-1])
        if part == 2:
            res.append(int(str(r) + str(values[-1])))
    return res


def solve_part1(answers: list[int], values: list[list[int]]):
    ans = 0

    for res, vals in zip(answers, values):
        results = get_possible_results(vals)
        if res in results:
            ans += res

    return ans


def solve_part2(answers: list[int], values: list[list[int]]):
    ans = 0

    for res, vals in zip(answers, values):
        results = get_possible_results(vals, 2)
        if res in results:
            ans += res

    return ans
