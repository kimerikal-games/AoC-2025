"""
Advent of Code 2025 - Day 10: Factory
Author: kimerikal <kimerikal.games@gmail.com>
"""

import sys

from ortools.sat.python import cp_model

State = list[int]
Button = list[int]
Affects = list[list[int]]
Joltage = int
Case = tuple[int, State, int, Affects, list[Joltage]]


def main() -> int:
    lines = sys.stdin.readlines()
    cases: list[Case] = []

    for line in lines:
        parts = line.split()

        initial_state = list(map(int, parts[0][1:-1].replace(".", "0").replace("#", "1")))
        buttons = [list(map(int, each[1:-1].split(","))) for each in parts[1:-1]]
        joltages = list(map(int, parts[-1][1:-1].split(",")))

        num_lights = len(initial_state)
        num_buttons = len(buttons)
        affects: list[list[int]] = [[] for _ in range(num_lights)]
        for button_index, button in enumerate(buttons):
            for light_index in button:
                affects[light_index].append(button_index)

        cases.append((num_lights, initial_state, num_buttons, affects, joltages))

    print("Part 1:", part1(cases))
    print("Part 2:", part2(cases))
    return 0


def part1(cases: list[Case]) -> int:
    solver = cp_model.CpSolver()
    solver.parameters.num_workers = 1

    total_presses = 0

    for num_lights, initial_state, num_buttons, affects, _ in cases:
        model = cp_model.CpModel()
        presses = [model.new_bool_var(f"presses_{i}") for i in range(num_buttons)]

        for i in range(num_lights):
            xor_vars = [presses[j] for j in affects[i]]
            xor_vars.append(model.new_constant(not initial_state[i]))
            model.add_bool_xor(xor_vars)

        model.minimize(sum(presses))

        status = solver.solve(model)
        assert status == cp_model.OPTIMAL

        cnt_press = sum(solver.value(press) for press in presses)
        total_presses += cnt_press

    return total_presses


def part2(cases: list[Case]) -> int:
    solver = cp_model.CpSolver()
    solver.parameters.num_workers = 1

    total_presses = 0

    for num_lights, _, num_buttons, affects, joltages in cases:
        model = cp_model.CpModel()
        press_ub = sum(joltages)
        presses = [model.new_int_var(0, press_ub, f"presses_{i}") for i in range(num_buttons)]

        for i in range(num_lights):
            joltage_press = sum(presses[j] for j in affects[i])
            joltage_target = joltages[i]
            model.add(joltage_press == joltage_target)

        model.minimize(sum(presses))

        status = solver.solve(model)
        assert status == cp_model.OPTIMAL

        cnt_press = sum(solver.value(press) for press in presses)
        total_presses += cnt_press

    return total_presses


if __name__ == "__main__":
    sys.exit(main())
