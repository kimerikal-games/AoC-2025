"""
Advent of Code 2025 - Day 3: Lobby
Author: kimerikal <kimerikal.games@gmail.com>
"""

import sys

PART2_RESULT_LENGTH = 12


def main() -> int:
    banks = [list(map(int, line)) for line in sys.stdin.read().split()]

    print("Part 1:", part1(banks))
    print("Part 2:", part2(banks))

    return 0


def part1(banks: list[list[int]]) -> int:
    total_joltage = 0

    for bank in banks:
        n = len(bank)
        max_joltage = -1

        for i in range(n):
            for j in range(i + 1, n):
                joltage = bank[i] * 10 + bank[j]
                if joltage > max_joltage:
                    max_joltage = joltage

        total_joltage += max_joltage

    return total_joltage


def part2(banks: list[list[int]]) -> int:
    total_joltage = 0

    for bank in banks:
        result: list[int] = []

        for digit in reversed(bank):
            result.append(digit)

            if len(result) > PART2_RESULT_LENGTH:
                to_remove = 0

                for i in range(len(result) - 1, -1, -1):
                    if result[i - 1] > result[i]:
                        to_remove = i
                        break

                result.pop(to_remove)

        joltage = 0
        for digit in reversed(result):
            joltage = joltage * 10 + digit

        total_joltage += joltage

    return total_joltage


if __name__ == "__main__":
    sys.exit(main())
