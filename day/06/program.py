"""
Advent of Code 2025 - Day 6: Trash Compactor
Author: kimerikal <kimerikal.games@gmail.com>
"""

import sys
from collections.abc import Iterable
from math import prod


def main() -> int:
    data = sys.stdin.read()

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))

    return 0


def part1(data: str):
    lines = data.strip().split("\n")

    grid = [list(map(int, line.split())) for line in lines[:-1]]
    operators = lines[-1].split()
    n = len(operators)

    total = 0

    for i in range(n):
        numbers = [grid[j][i] for j in range(len(grid))]
        operator = operators[i]

        total += evaluate(numbers, operator)

    return total


def part2(data: str):
    lines = data.split("\n")
    lines.pop()

    timings = [i for i, c in enumerate(lines[-1]) if c != " "]
    n = len(timings)
    timings.append(len(lines[-1]) + 1)

    total = 0

    for i in range(n):
        start, end = timings[i], timings[i + 1]
        operator = lines[-1][timings[i]]
        numbers: list[int] = []

        for col in range(end - 2, start - 1, -1):
            digits = [lines[row][col] for row in range(len(lines) - 1)]
            number = int("".join(digits))
            numbers.append(number)

        total += evaluate(numbers, operator)

    return total


def evaluate(numbers: Iterable[int], operator: str) -> int:
    match operator:
        case "+": return sum(numbers)
        case "*": return prod(numbers)
        case _: raise ValueError(f"Unknown operator: {operator}")


if __name__ == "__main__":
    sys.exit(main())
