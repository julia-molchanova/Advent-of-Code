from collections import defaultdict


def parse_data(lines: list[str]):
    return [int(x) for x in lines[0].split(" ")], None


def solve_part1(nums: list[int], dummy):
    for _ in range(25):
        new_nums = []
        for n in nums:
            n_string = str(n)
            digits_num = len(n_string)
            if n == 0:
                new_nums.append(1)
            elif digits_num % 2 == 0:
                new_nums += [
                    int(n_string[: digits_num // 2]),
                    int(n_string[digits_num // 2 :]),
                ]
            else:
                new_nums.append(2024 * n)

        nums = new_nums

    return len(nums)


def solve_part2(nums: list[int], dummy):
    counts = {x: 1 for x in nums}
    for _ in range(75):
        new_counts = defaultdict(int)
        for n, cnt in counts.items():
            n_string = str(n)
            digits_num = len(n_string)
            if n == 0:
                new_counts[1] += cnt
            elif digits_num % 2 == 0:
                new_counts[int(n_string[: digits_num // 2])] += cnt
                new_counts[int(n_string[digits_num // 2 :])] += cnt
            else:
                new_counts[2024 * n] += cnt

        counts = new_counts

    return sum(counts.values())
