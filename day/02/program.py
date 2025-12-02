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
        start_len = count_digits(start)
        candidate_start_len = (start_len + 1) // 2
        candidate = 10 ** (candidate_start_len - 1)

        for candidate in count(candidate):
            doubled = duplicate(candidate, 2)
            if doubled > end:
                break
            if doubled < start:
                continue
            total += doubled

    return total


def part2(id_ranges: list[tuple[int, int]]) -> int:
    total = 0

    for start, end in id_ranges:
        visited = set()

        for candidate in count(1):
            if duplicate(candidate, 2) > end:
                break

            candidate_str = str(candidate)
            candidate_len = len(candidate_str)

            max_repetition = len(str(end)) // candidate_len
            if max_repetition == 0:
                continue
            min_repetition = -(-count_digits(start) // candidate_len)

            for repetition in range(min_repetition, max_repetition + 1):
                repeated = duplicate(candidate, repetition)
                if repeated < start:
                    continue
                if repeated > end:
                    break
                if repeated not in visited:
                    visited.add(repeated)
                    total += repeated

    return total


def count_digits(n: int) -> int:
    return len(str(n))


def duplicate(n: int, k: int) -> int:
    return int(str(n) * k)


if __name__ == "__main__":
    sys.exit(main())
