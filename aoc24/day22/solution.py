import time
from functools import cache


def parse_data(lines: list[str]):
    return [int(x) for x in lines], None


def print_time(user_function):
    def decorator(*args, **kwargs):
        start = time.time()
        res = user_function(*args, **kwargs)
        print(time.time() - start)
        return res

    return decorator


def prune(x: int):
    return x % 16777216


def get_next_number(x: int):
    x ^= x << 6
    x = prune(x)
    x ^= x >> 5
    x = prune(x)
    x ^= x << 11
    return prune(x)


@print_time
def solve_part1(numbers: list[int], dummy: None) -> int:
    ans = 0
    for secret_number in numbers:
        for _ in range(2000):
            secret_number = get_next_number(secret_number)
        ans += secret_number

    return ans


@print_time
def solve_part2(numbers: list[int], dummy: None):
    all_sales = []
    all_diffs = set()

    for secret_number in numbers:
        prev_price = secret_number % 10
        cur_sale = {}
        cur_diffs = []

        for _ in range(2000):
            secret_number = get_next_number(secret_number)
            cur_price = secret_number % 10

            price_diff = cur_price - prev_price
            cur_diffs += (price_diff,)
            cur_diffs = tuple(cur_diffs[-4:])
            if len(cur_diffs) == 4:
                if cur_diffs not in cur_sale:
                    cur_sale[cur_diffs] = cur_price
                all_diffs.add(cur_diffs)

            prev_price = cur_price
        all_sales.append(cur_sale)

    ans = 0
    for diff in all_diffs:
        cur_res = 0
        for cur_sale in all_sales:
            if diff in cur_sale:
                cur_res += cur_sale[diff]

        ans = max(ans, cur_res)

    return ans
