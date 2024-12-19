import functools


def parse_data(lines: list[str]):
    patterns = lines[0].split(",")
    patterns = [patterns[0]] + [x[1:] for x in patterns[1:]]

    return tuple(patterns), lines[2:]


def cache(user_function):
    history = {}

    def decorator(*args):
        t_args = tuple(args)
        if t_args not in history:
            history[t_args] = user_function(*args)
        return history[t_args]

    print("created cache for ", str(user_function))
    return decorator


@cache
def check_validity(patterns: tuple[str, ...], line: str, findall: bool = False) -> int:
    if len(line) == 0:
        return 1

    ans = 0
    for i in range(1, len(line) + 1):
        res = 0
        if line[:i] in patterns:
            res = check_validity(patterns, line[i:], findall)
        if not findall and res > 0:
            return res
        ans += res
    return ans


def solve_part1(patterns: tuple[str, ...], lines: list[str]) -> int:
    ans = 0
    for line in lines:
        ans += check_validity(patterns, line)
    return ans


def solve_part2(patterns: list[str], lines: list[str]):
    ans = 0
    for line in lines:
        ans += check_validity(patterns, line, True)
    return ans
