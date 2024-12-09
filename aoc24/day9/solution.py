def parse_data(lines: list[str]):
    return [int(x) for x in lines[0]], None


def solve_part1(line_inp: list[int], dummy):
    ans = 0
    line = line_inp.copy()

    cur_file_index = len(line) - 1
    cur_file_size = line[cur_file_index]
    i = 0
    ind = 0
    while i <= cur_file_index:
        num = line[i]
        if i % 2 == 0:
            for _ in range(num):
                ans += i // 2 * ind
                ind += 1
        else:
            for _ in range(num):
                ans += cur_file_index // 2 * ind
                cur_file_size -= 1
                if cur_file_size == 0:
                    line[cur_file_index] = 0
                    cur_file_index -= 2
                    cur_file_size = line[cur_file_index]
                    if cur_file_index < i:
                        break
                ind += 1
            line[cur_file_index] = cur_file_size
        i += 1

    return ans


def solve_part2(line: list[int], dummy):
    memory = []
    cur_ind = 0
    for i, num in enumerate(line):
        memory.append([cur_ind, i % 2 == 0, num, i // 2])
        cur_ind += num
    i = len(memory) - 1
    while i > 0:
        _, is_file, length, file_ind = memory[i]
        if not is_file:
            i -= 1
            continue
        moved = False
        j = 1
        space_start, _, space_length, space_ind = memory[i]
        while not moved and j < i:
            space_start, space_is_file, space_length, space_ind = memory[j]
            if space_is_file or space_length < length:
                j += 1
                continue
            moved = True
            memory[j] = [space_start, True, length, file_ind]
            if space_length > length:
                memory.insert(
                    j + 1,
                    [space_start + length, False, space_length - length, space_ind],
                )
                i += 1

        if moved:
            memory.pop(i)

        i -= 1

    ans = 0

    for start, is_file, length, file_ind in memory:
        if not is_file:
            continue

        ans += file_ind * length * (2 * start + (length - 1)) // 2

    return ans
