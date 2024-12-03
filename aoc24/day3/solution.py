import re


def parse_data(lines: list[str]):
    # takes lines of the input, processes data into data structures fir for the task
    string = ""
    for line in lines:
        string += line
    return string, None


def solve_part1(command: str, dummy):
    templates = [
        re.compile(r"mul\(\d+,\d+\)"),
    ]
    number = re.compile(r"\d+")
    ans = 0
    while len(command) > 0:
        best_match = None
        first_found_j = None
        for j, t in enumerate(templates):
            match = t.search(command)
            if match and (best_match is None or match.start() < best_match.start()):
                best_match = match
                first_found_j = j
        if first_found_j is None:
            break
        command = command[best_match.end() :]
        numbers = [int(x) for x in number.findall(best_match.group())]
        ans += numbers[0] * numbers[1]
    return ans


def solve_part2(command: str, dummy):
    # even more regular expressions here

    templates = [
        re.compile(r"do\(\)"),
        re.compile(r"don't\(\)"),
        re.compile(r"mul\(\d+,\d+\)"),
    ]
    number = re.compile(r"\d+")
    ans = 0
    enabled = True
    while len(command) > 0:
        best_match = None
        first_found_j = None
        for j, t in enumerate(templates):
            match = t.search(command)
            if match and (best_match is None or match.start() < best_match.start()):
                best_match = match
                first_found_j = j
        if first_found_j is None:
            break
        command = command[best_match.end() :]
        match first_found_j:
            case 0:
                enabled = True
            case 1:
                enabled = False
            case 2:
                if not enabled:
                    continue
                numbers = [int(x) for x in number.findall(best_match.group())]
                ans += numbers[0] * numbers[1]
    return ans
