"""
Advent of Code 2025 - Day 11: Reactor
Author: kimerikal <kimerikal.games@gmail.com>
"""

import sys

Node = str
Graph = dict[Node, list[Node]]


def main() -> int:
    data = sys.stdin.readlines()
    graph: Graph = {}

    for line in data:
        args = line.split()

        source = args[0][:-1]
        destinations = args[1:]
        graph[source] = destinations

    print("Part 1:", part1(graph))
    print("Part 2:", part2(graph))

    return 0


def part1(graph: Graph) -> int:
    return count_paths(graph, "you", "out")


def part2(graph: Graph) -> int:
    c11 = count_paths(graph, "svr", "dac")
    c12 = count_paths(graph, "dac", "fft")
    c13 = count_paths(graph, "fft", "out")

    c21 = count_paths(graph, "svr", "fft")
    c22 = count_paths(graph, "fft", "dac")
    c23 = count_paths(graph, "dac", "out")

    return c11 * c12 * c13 + c21 * c22 * c23


def count_paths(graph: Graph, start: Node, end: Node) -> int:
    memo: dict[Node, int] = {end: 1}
    stack: list[tuple[Node, bool]] = [(start, False)]

    while stack:
        node, processed = stack.pop()

        if processed:
            total_paths = 0

            for neighbor in graph.get(node, []):
                total_paths += memo.get(neighbor, 0)

            memo[node] = total_paths

        else:
            stack.append((node, True))

            for neighbor in graph.get(node, []):
                if neighbor not in memo:
                    stack.append((neighbor, False))

    path_count = memo.get(start, 0)
    return path_count


if __name__ == "__main__":
    sys.exit(main())
