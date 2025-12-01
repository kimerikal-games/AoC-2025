"""
Advent of Code 2025 - Day 1: Secret Entrance
Author: kimerikal <kimerikal.games@gmail.com>
"""

import sys


def main() -> int:
    instructions = sys.stdin.read().split()

    print("Part 1:", part1(instructions))
    print("Part 2:", part2(instructions))

    return 0


def part1(instructions: list[str]) -> int:
    cnt_zeros = 0
    position = 50

    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])

        match direction:
            case "L":
                position = (position - distance) % 100
            case "R":
                position = (position + distance) % 100
            case _:
                raise ValueError(f"Unknown value {direction=}")

        if position == 0:
            cnt_zeros += 1

    password = cnt_zeros
    return password


def part2(instructions: list[str]) -> int:
    cnt_turns = 0
    position = 50

    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])

        match direction:
            case "L":
                position = -position % 100
                turns, position = divmod(position + distance, 100)
                position = -position % 100
            case "R":
                turns, position = divmod(position + distance, 100)
            case _:
                raise ValueError(f"Unknown value {direction=}")

        cnt_turns += turns

    password = cnt_turns
    return password


if __name__ == "__main__":
    sys.exit(main())
