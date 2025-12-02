"""
Advent of Code 2025 - Day 2: Gift Shop
Author: kimerikal <kimerikal.games@gmail.com>
"""

import sys
from itertools import count


def main() -> int:
    tokens = sys.stdin.read().strip().split(",")
    id_ranges: list[tuple[int, int]] = []
    for token in tokens:
        start, end = map(int, token.split("-"))
        id_ranges.append((start, end))

    print("Part 1:", part1(id_ranges))
    print("Part 2:", part2(id_ranges))

    return 0


def part1(id_ranges: list[tuple[int, int]]) -> int:
    total = 0

    for start, end in id_ranges:
        start_length = digit_length(start)

        candidate_start_length = (start_length + 1) // 2
        candidate_start = 10 ** (candidate_start_length - 1)

        for candidate in count(candidate_start):
            double_candidate = double(candidate)
            if double_candidate < start:
                continue
            if double_candidate > end:
                break
            total += double_candidate

    return total


def part2(id_ranges: list[tuple[int, int]]) -> int:
    total = 0

    for start, end in id_ranges:
        visited: set[int] = set()

        for candidate in count(1):
            if double(candidate) > end:
                break

            for repetition in count(1):
                repeat_candidate = repeat(candidate, repetition)

                if repeat_candidate < start:
                    continue
                if repeat_candidate > end:
                    break

                if repeat_candidate in visited:
                    continue
                visited.add(repeat_candidate)

                total += repeat_candidate

    return total


def digit_length(n: int) -> int:
    if n == 0:
        return 1
    length = 0
    while n > 0:
        n //= 10
        length += 1
    return length


def double(n: int) -> int:
    length = digit_length(n)
    return n * (10**length) + n


def repeat(n: int, k: int) -> int:
    length = digit_length(n)
    result = 0
    for _ in range(k):
        result = result * (10**length) + n
    return result


if __name__ == "__main__":
    sys.exit(main())
