"""
Advent of Code 2025 - Day 7: Laboratories
Author: kimerikal <kimerikal.games@gmail.com>
"""

import sys
from collections.abc import Sequence

Grid = Sequence[Sequence[int]]


def main() -> int:
    lines = sys.stdin.read().splitlines()[0::2]
    grid = [list(map(int, line.replace(".", "0").replace("^", "1").replace("S", "9"))) for line in lines]
    rows = len(grid)
    cols = len(grid[0])

    part1_answer, part2_answer = parts(rows, cols, grid)

    print("Part 1:", part1_answer)
    print("Part 2:", part2_answer)

    return 0


def parts(rows: int, cols: int, grid: Grid) -> tuple[int, int]:
    start_col = grid[0].index(9)

    table: list[int] = [0] * cols
    beams: set[int] = set()
    cnt_splits = 0

    table[start_col] = 1
    beams.add(start_col)

    for r in range(1, rows):
        row = grid[r]

        next_beams: set[int] = set()
        next_table: list[int] = [0] * cols

        for beam in beams:
            match row[beam]:
                case 0:
                    next_beams.add(beam)
                    next_table[beam] += table[beam]
                case 1:
                    next_beams.add(beam - 1)
                    next_beams.add(beam + 1)
                    next_table[beam - 1] += table[beam]
                    next_table[beam + 1] += table[beam]
                    cnt_splits += 1
                case _:
                    assert False, "Invalid cell value"

        beams = next_beams
        table = next_table

    part1_answer = cnt_splits
    part2_answer = sum(table)

    return part1_answer, part2_answer


def part1(rows: int, cols: int, grid: Grid) -> int:
    return parts(rows, cols, grid)[0]


def part2(rows: int, cols: int, grid: Grid) -> int:
    return parts(rows, cols, grid)[1]


if __name__ == "__main__":
    sys.exit(main())
