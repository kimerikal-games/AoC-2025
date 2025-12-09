"""
Advent of Code 2025 - Day 4: Printing Department
Author: kimerikal <kimerikal.games@gmail.com>
"""

import sys

ADJACENTS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def main() -> int:
    data = sys.stdin.read().replace(".", "0").replace("@", "1")
    grid = [list(map(int, line)) for line in data.splitlines()]
    rows = len(grid)
    cols = len(grid[0])

    print("Part 1:", part1(rows, cols, grid))
    print("Part 2:", part2(rows, cols, grid))

    return 0


def part1(rows: int, cols: int, grid: list[list[int]]) -> int:
    count_accessible = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                continue

            count_adjacent = 0
            for dr, dc in ADJACENTS:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue
                if grid[nr][nc] == 1:
                    count_adjacent += 1

            if count_adjacent < 4:
                count_accessible += 1

    return count_accessible


def part2(rows: int, cols: int, grid: list[list[int]]) -> int:

    count_removed = 0

    while True:
        accessible: list[tuple[int, int]] = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue

                count_adjacent = 0
                for dr, dc in ADJACENTS:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < rows and 0 <= nc < cols):
                        continue
                    if grid[nr][nc] == 1:
                        count_adjacent += 1

                if count_adjacent < 4:
                    accessible.append((r, c))

        if not accessible:
            break

        for r, c in accessible:
            grid[r][c] = 0

        count_removed += len(accessible)

    return count_removed


if __name__ == "__main__":
    sys.exit(main())
