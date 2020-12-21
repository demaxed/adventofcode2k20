import re


def read_input():
    with open("input", "r") as file:
        for line in file.readlines():
            yield line.split(":")


def is_valid_part_one(policy, password):
    interval = re.findall(r"\d+", policy)
    letter = re.findall(r"[a-zA-Z]", policy)[0]
    if int(interval[0]) <= password.count(letter) <= int(interval[1]):
        return True
    return False


def is_valid_part_two(policy, password):
    interval = re.findall(r"\d+", policy)
    letter = re.findall(r"[a-zA-Z]", policy)[0]
    first_index = int(interval[0])
    second_index = int(interval[1])
    print(password[first_index], password[second_index], letter)
    if (password[first_index] == letter) != (password[second_index] == letter):
        print(1)
        return True
    print(0)
    return False


def part_one():
    numbers_valid_pass = 0
    for input_ in read_input():
        if is_valid_part_one(policy=input_[0], password=input_[1]):
            numbers_valid_pass += 1
    print(numbers_valid_pass)


def part_two():
    numbers_valid_pass = 0
    for input_ in read_input():
        if is_valid_part_two(policy=input_[0], password=input_[1]):
            numbers_valid_pass += 1
    print(numbers_valid_pass)


def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
