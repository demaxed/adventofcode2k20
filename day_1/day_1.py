from typing import List

YEAR = 2020


def read_input() -> List[int]:
    with open("day_1/input", "r") as file:
        input_ = [int(line) for line in file.readlines()]
    return input_


def part_one():
    """
    Find the two entries that sum to 2020; what do you get if you multiply them together?
    """
    input_ = read_input()
    input_.sort()
    size = len(input_)

    i = 0
    j = size - 1
    result = None
    while i < j:
        if input_[i] + input_[j] == YEAR:
            result = input_[i] * input_[j]
            break
        elif input_[i] + input_[j] < YEAR:
            i += 1
        else:
            j -= 1
    print(f"part one result: {result}")


def part_two():
    """
    find three numbers in your expense report that meet the same criteria.
    """
    input_ = read_input()
    input_.sort()
    size = len(input_)

    for el in input_:
        target = YEAR - el
        i = 0
        j = size - 1
        while i < j:
            if input_[i] + input_[j] == target:
                result = input_[i] * input_[j] * el
                print(f"part two result: {result}")
                return
            elif input_[i] + input_[j] < target:
                i += 1
            else:
                j -= 1


def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
