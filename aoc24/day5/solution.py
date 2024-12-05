from collections import defaultdict


def parse_data(lines: list[str]):
    # takes lines of the input, processes data into data structures fit for the task
    rules = defaultdict(set)
    i = 0
    while lines[i] != "":
        a, b = lines[i].split("|")
        rules[int(b)].add(int(a))
        i += 1
    update = []
    for line in lines[i + 1 :]:
        numbers = [int(x) for x in line.split(",")]
        update.append(numbers)
    return rules, update


def solve_part1(rules: dict, updates: list[list[int]]):
    ans = 0

    for update in updates:
        # just checking if any rule is violated
        already_printed = set()
        will_be_printed = set(update)
        valid = True

        for num in update:
            already_printed.add(num)
            if num not in rules:
                continue
            to_visit = [num]
            visited = {num}
            while valid and len(to_visit) > 0:
                v = to_visit.pop(0)
                if v not in rules:
                    continue
                for prev in rules[v]:
                    if prev in will_be_printed and prev not in already_printed:
                        valid = False
                        break
                    if v not in visited:
                        to_visit.append(v)

        ans += update[len(update) // 2] if valid else 0
    return ans


def solve_part2(rules: dict, updates: list[list[int]]):
    ans = 0

    for update in updates:
        # actually the first part
        already_printed = set()
        will_be_printed = set(update)
        valid = True

        for num in update:
            already_printed.add(num)
            if num not in rules:
                continue
            to_visit = [num]
            visited = {num}
            while valid and len(to_visit) > 0:
                v = to_visit.pop(0)
                if v not in rules:
                    continue
                for prev in rules[v]:
                    if prev in will_be_printed and prev not in already_printed:
                        valid = False
                        break
                    if v not in visited:
                        to_visit.append(v)

        if valid:
            continue

        # second part starts here in case the pages order is invalid
        # topological sort

        correct_order = []
        limited_rules = {x: rules[x] & will_be_printed for x in update}
        valid_next = [x for x in limited_rules if len(limited_rules[x]) == 0]
        while len(valid_next) > 0:
            for x in valid_next:
                if x in limited_rules:
                    del limited_rules[x]
            next_page = valid_next.pop()
            correct_order.append(next_page)
            for x in limited_rules:
                limited_rules[x] -= {next_page}
                if len(limited_rules[x]) == 0:
                    valid_next.append(x)

        ans += correct_order[len(correct_order) // 2]

    return ans
