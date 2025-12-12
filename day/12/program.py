"""
Advent of Code 2025 - Day 12: Christmas Tree Farm
Author: kimerikal <kimerikal.games@gmail.com>
"""

import sys

Shape = list[list[int]]
Boardsize = tuple[int, int]
Shapecount = list[int]
Quantity = tuple[Boardsize, Shapecount]


def main() -> int:
    shapes: list[Shape] = []
    quantities: list[Quantity] = []

    parse_mode = "shapes"
    while True:
        line = sys.stdin.readline()

        if parse_mode == "shapes" and "x" in line:
            parse_mode = "quantity"

        match parse_mode:
            case "shapes":
                _ = line
                shape: Shape = []
                for _ in range(3):
                    shape.append([1 if c == "#" else 0 for c in sys.stdin.readline().strip()])
                shapes.append(shape)
                _ = sys.stdin.readline()
            case "quantity":
                if not line:
                    break
                args = line.split(": ")
                width, height = tuple(map(int, args[0].split("x")))
                shapecounts = list(map(int, args[1].split()))
                quantity = ((width, height), shapecounts)
                quantities.append(quantity)

    print("Part 1:", part1(shapes, quantities))
    print("Part 2:", part2(shapes, quantities))

    return 0


def part1(shapes: list[Shape], quantities: list[Quantity]) -> int:
    available = 0

    shapeunits = [sum(sum(row) for row in shape) for shape in shapes]

    for (width, height), shapecounts in quantities:
        area = width * height
        total_units = sum(shapeunit * count for shapeunit, count in zip(shapeunits, shapecounts))
        if total_units > area:
            continue

        max_units = sum(9 * count for count in shapecounts)
        if max_units <= area:
            available += 1
            continue

        raise NotImplementedError("Packing algorithm not implemented.")

    return available


def part2(shapes: list[Shape], quantities: list[Quantity]) -> int:
    return 0


if __name__ == "__main__":
    sys.exit(main())
