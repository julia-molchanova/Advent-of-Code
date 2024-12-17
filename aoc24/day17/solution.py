import re


def parse_data(lines: list[str]):
    registers = []
    pattern = re.compile(r"-?\d+")
    for line in lines[:-2]:
        registers.append(int(pattern.findall(line)[0]))

    commands = [int(x) for x in pattern.findall(lines[-1])]

    return registers[0], registers[1], registers[2], commands


def execute_commands(a: int, b: int, c: int, commands: list[list[int]]):
    ans = []
    i = 0
    while i + 1 < len(commands):
        command, literal = commands[i], commands[i + 1]
        combo = None
        match literal:
            case 0 | 1 | 2 | 3:
                combo = literal
            case 4:
                combo = a
            case 5:
                combo = b
            case 6:
                combo = c
            case 7:
                combo = None
        di = 2
        match command:
            case 0:
                a //= 2**combo
            case 1:
                b = b ^ literal
            case 2:
                b = combo % 8
            case 3:
                if a != 0:
                    i = literal
                    di = 0
            case 4:
                b = b ^ c
            case 5:
                ans.append(combo % 8)
            case 6:
                b = a // (2**combo)
            case 7:
                c = a // (2**combo)

        i += di

    return ans


def solve_part1(a: int, b: int, c: int, commands: list[list[int]]):
    ans = execute_commands(a, b, c, commands)
    return int("".join([str(x) for x in ans]))


def solve_part2(a: int, b: int, c: int, commands: list[list[int]]):
    cur_valid_a = [[0, 9]]
    passes = 0
    for i in range(1, len(commands) + 1):
        cur_answer = commands[-i:]
        valid_a = []
        for min_a, max_a in cur_valid_a:
            for a in range(min_a, max_a):
                passes += 1
                res = execute_commands(a, b, c, commands)
                if res == cur_answer:
                    valid_a.append([8 * a, 8 * (a + 1)])
        cur_valid_a = valid_a
    # just for fun
    print(passes)
    return min([x[0] // 8 for x in cur_valid_a])
