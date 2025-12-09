"""
Advent of Code 2025 - Day 5: Cafeteria
Author: kimerikal <kimerikal.games@gmail.com>
"""

import sys
from typing import cast

Interval = tuple[int, int]


def main() -> int:
    data1, data2 = sys.stdin.read().strip().split("\n\n")
    intervals = [
        cast(Interval, tuple(map(int, line.split("-"))))
        for line in data1.splitlines()
    ]
    ingredients = list(map(int, data2.splitlines()))

    print("Part 1:", part1(intervals, ingredients))
    print("Part 2:", part2(intervals, ingredients))

    return 0


def part1(intervals: list[Interval], ingredients: list[int]) -> int:
    return sum(
        any(start <= ingredient <= end for start, end in intervals)
        for ingredient in ingredients
    )


def part2(intervals: list[Interval], ingredients: list[int]) -> int:
    intervals.sort()

    total_length = 0
    last_end = -1

    for start, end in intervals:
        start = max(start, last_end + 1)
        if start <= end:
            total_length += end - start + 1
            last_end = end

    return total_length


if __name__ == "__main__":
    sys.exit(main())
