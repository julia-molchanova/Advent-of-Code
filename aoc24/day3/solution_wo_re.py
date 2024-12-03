def parse_data(lines: list[str]):
    # takes lines of the input, processes data into data structures fir for the task
    string = ""
    for line in lines:
        string += line
    return string, None


def solve_part1(command: str, dummy):
    # can also do regular expressions, but it's much more fun
    numerics = {chr(a) for a in range(ord("0"), ord("9") + 1)}
    template = "mul("
    ans, i = 0, 0
    matched_from_template = 0
    while i < len(command):
        matched_from_template = (
            matched_from_template + 1
            if command[i] == template[matched_from_template]
            else 0
        )
        i += 1
        if matched_from_template < len(template):
            continue
        num1_str = ""
        while i < len(command) and command[i] in numerics:
            num1_str += command[i]
            i += 1
        if len(num1_str) == 0 or i == len(command) or command[i] != ",":
            matched_from_template = 0
            continue
        num1 = int(num1_str)
        i += 1

        num2_str = ""
        while i < len(command) and command[i] in numerics:
            num2_str += command[i]
            i += 1
        if len(num2_str) == 0 or i == len(command) or command[i] != ")":
            matched_from_template = 0
            continue
        num2 = int(num2_str)
        ans += num1 * num2
        matched_from_template = 0

    return ans


def solve_part2(command: str, dummy):
    # even more regular expressions here

    numerics = {chr(a) for a in range(ord("0"), ord("9") + 1)}
    templates = ["mul(", "do()", "don't()"]
    matches = [0, 0, 0]
    ans, i = 0, 0
    enabled = True
    while i < len(command):
        for j, t in enumerate(templates):
            matches[j] = matches[j] + 1 if command[i] == t[matches[j]] else 0
        i += 1
        for j, t in enumerate(templates):
            if matches[j] == len(t):
                matches[j] = 0
                if j == 1:
                    enabled = True
                elif j == 2:
                    enabled = False
                elif enabled:
                    num1_str = ""
                    while i < len(command) and command[i] in numerics:
                        num1_str += command[i]
                        i += 1
                    if len(num1_str) == 0 or i == len(command) or command[i] != ",":
                        continue
                    num1 = int(num1_str)
                    i += 1

                    num2_str = ""
                    while i < len(command) and command[i] in numerics:
                        num2_str += command[i]
                        i += 1
                    if len(num2_str) == 0 or i == len(command) or command[i] != ")":
                        continue
                    num2 = int(num2_str)
                    ans += num1 * num2

    return ans
