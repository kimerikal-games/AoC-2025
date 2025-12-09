"""
Advent of Code 2025 - Day 8: Playground
Author: kimerikal <kimerikal.games@gmail.com>
"""

import heapq
import sys
from typing import cast

Point = tuple[int, int, int]
X, Y, Z = 0, 1, 2


class DisjointSet:
    __slots__ = ("parents",)

    def __init__(self, size: int) -> None:
        self.parents = list(range(size))

    def find(self, u: int) -> int:
        parents = self.parents

        path: list[int] = []
        while parents[u] != u:
            path.append(u)
            u = parents[u]
        for node in path:
            parents[node] = u
        return u

    def union(self, u: int, v: int) -> bool:
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        self.parents[root_u] = root_v
        return True


def main() -> int:
    junctions: list[Point] = [
        cast(Point, tuple(map(int, line.split(","))))
        for line in sys.stdin.readlines()
    ]

    part1_answer, part2_answer = parts(junctions)
    print("Part 1:", part1_answer)
    print("Part 2:", part2_answer)

    return 0


def parts(junctions: list[Point]) -> tuple[int, int]:
    # NOTE: connections_to_make is input-dependent.
    connections_to_make = 1000 if len(junctions) == 1000 else 10

    distances = [
        (distance(junctions[j1], junctions[j2]), j1, j2)
        for j1 in range(len(junctions))
        for j2 in range(j1 + 1, len(junctions))
    ]
    heapq.heapify(distances)

    ds = DisjointSet(len(junctions))
    cnt_groups = len(junctions)

    part1_answer: int | None = None
    part2_answer: int | None = None

    for i in range(len(distances)):
        _, j1, j2 = heapq.heappop(distances)

        if i == connections_to_make:
            sizes = [0] * len(junctions)
            for j in range(len(junctions)):
                root = ds.find(j)
                sizes[root] += 1
            sizes.sort()
            part1_answer = sizes[-1] * sizes[-2] * sizes[-3]

        cnt_groups -= ds.union(j1, j2)

        if cnt_groups == 1:
            part2_answer = junctions[j1][X] * junctions[j2][X]

        if part1_answer is not None and part2_answer is not None:
            break
    else:
        assert False, "Should have found both answers"

    return part1_answer, part2_answer


def distance(p1: Point, p2: Point) -> int:
    dx = p2[X] - p1[X]
    dy = p2[Y] - p1[Y]
    dz = p2[Z] - p1[Z]
    return dx * dx + dy * dy + dz * dz


if __name__ == "__main__":
    sys.exit(main())
