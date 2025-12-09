"""
Advent of Code 2025 - Day 9: Movie Theater
Author: kimerikal <kimerikal.games@gmail.com>
"""

import sys
from typing import cast

Grid = list[list[int]]
Point = tuple[int, int]
Map = dict[int, int]

FILL = -1


def main() -> int:
    points = [
        cast(Point, tuple(map(int, line.split(","))))
        for line in sys.stdin.readlines()
    ]

    print("Part 1:", part1(points))
    print("Part 2:", part2(points))

    return 0


def part1(points: list[Point]) -> int:
    max_area = 0

    for i in range(len(points)):
        p1x, p1y = points[i]
        for j in range(i + 1, len(points)):
            p2x, p2y = points[j]

            width = abs(p1x - p2x) + 1
            height = abs(p1y - p2y) + 1
            area = width * height

            if area > max_area:
                max_area = area

    return max_area


def part2(points: list[Point]) -> int:
    xmap = {x: i for i, x in enumerate(sorted({p[0] for p in points}))}
    ymap = {y: i for i, y in enumerate(sorted({p[1] for p in points}))}

    rows, cols = len(xmap), len(ymap)
    grid = [[0] * cols for _ in range(rows)]

    for i in range(len(points)):
        x1, y1 = points[i - 1]
        x2, y2 = points[i]

        cx1, cx2 = xmap[min(x1, x2)], xmap[max(x1, x2)]
        cy1, cy2 = ymap[min(y1, y2)], ymap[max(y1, y2)]

        for x in range(cx1, cx2 + 1):
            for y in range(cy1, cy2 + 1):
                grid[x][y] = 1

    for x, y in [(0, 0), (0, cols - 1), (rows - 1, 0), (rows - 1, cols - 1)]:
        if grid[x][y] == 0:
            flood_fill(rows, cols, grid, x, y)

    max_area = 0

    for i in range(len(points)):
        p1x, p1y = points[i]
        for j in range(i + 1, len(points)):
            p2x, p2y = points[j]

            cx1, cx2 = xmap[min(p1x, p2x)], xmap[max(p1x, p2x)]
            cy1, cy2 = ymap[min(p1y, p2y)], ymap[max(p1y, p2y)]

            if any(grid[x][y] == FILL for x in (cx1, cx2) for y in range(cy1, cy2 + 1)):
                continue

            width = abs(p1x - p2x) + 1
            height = abs(p1y - p2y) + 1
            area = width * height

            if area > max_area:
                max_area = area

    return max_area


def flood_fill(rows: int, cols: int, grid: Grid, x: int, y: int) -> None:
    to_visit: list[Point] = []
    to_visit.append((x, y))

    while to_visit:
        cx, cy = to_visit.pop()
        if grid[cx][cy] != 0:
            continue
        grid[cx][cy] = FILL
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                to_visit.append((nx, ny))


if __name__ == "__main__":
    sys.exit(main())
