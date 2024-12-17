from pathlib import Path
from day17.solution import parse_data, solve_part1, solve_part2


def read_data(path: str):
    with Path.open(path, "r") as f:
        lines = f.readlines()
    lines = [x[:-1] for x in lines[:-1]] + [lines[-1]]
    return lines


def read_correct_answer(path: str):
    lines = read_data(path)
    if len(lines) == 1:
        return int(lines[0]), None
    return int(lines[0]), int(lines[1])


task = 17

if __name__ == "__main__":

    data_path = Path(f"aoc24/day{task}")
    example_correct_ans1, example_correct_ans2 = read_correct_answer(
        data_path / "example_answers.txt"
    )

    example_lines = read_data(data_path / "example.txt")
    example_data = parse_data(example_lines)

    for solver, correct_answer in zip(
        [solve_part1, solve_part2], [example_correct_ans1, example_correct_ans2]
    ):
        example_answer = solver(*example_data)

        if correct_answer is not None and example_answer != correct_answer:
            print(
                f"Answered {example_answer}, correct answer for this example: {correct_answer}"
            )

    print("Tests completed")

    input_lines = read_data(data_path / "input.txt")
    input_data = parse_data(input_lines)

    for part_num, solver in zip([1, 2], [solve_part1, solve_part2]):
        input_answer = solver(*input_data)
        print(f"Answer for part {part_num}: {input_answer}")
