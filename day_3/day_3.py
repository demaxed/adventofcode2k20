from typing import List

FILE_PATH = "/Users/demanenkomaksim/PycharmProjects/advent-of-code-2020/day_3/input"


def read_input() -> List[str]:
    output = []
    with open(FILE_PATH, "r") as f:
        for line in f.readlines():
            output.append(line.replace("\n", ""))

    return output


def count_trees(grid, x_offset=3, y_offset=1) -> int:
    x_dimension = len(grid[0])
    y_deminsion = len(grid)
    ix, iy, result = 0, 0, 0

    while iy < (y_deminsion - 1):
        ix = (ix + x_offset) % x_dimension
        iy += y_offset

        cell = grid[iy][ix]
        if cell == "#":
            result += 1

    return result


def part_one(grid):
    result = count_trees(grid)
    print(result)


def part_two(grid):
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    result = 1
    for x_offset, y_offset in slopes:
        result *= count_trees(grid, x_offset, y_offset)
    print(result)


def main():
    grid = read_input()
    print("Part one:")
    part_one(grid)
    print("Part two:")
    part_two(grid)


if __name__ == "__main__":
    main()
