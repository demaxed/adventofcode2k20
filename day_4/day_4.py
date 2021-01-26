from typing import Dict, List, Optional
import re

from icecream import ic

FILEPATH = "/Users/demanenkomaksim/PycharmProjects/advent-of-code-2020/day_4/input"

REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def read_input() -> List[Dict[str, str]]:
    with open(FILEPATH, "r") as f:
        output = []
        passport = {}
        for line in f.readlines():
            if line == "\n":
                output.append(passport)
                passport = {}
                continue
            fields = line.split(" ")
            for field in fields:
                key, value = field.split(":")
                passport[key] = value.strip("\n")
        output.append(passport)

    return output


def validate_fields(passport: Dict) -> bool:
    fields = set(passport.keys())
    if REQUIRED_FIELDS.issubset(fields):
        return True
    return False


def part_one(data: List[Dict[str, str]]) -> List[Dict]:
    validated_passports = []
    for passport in data:
        if validate_fields(passport):
            validated_passports.append(passport)

    ic(len(validated_passports))
    return validated_passports


def part_two(data):
    patterns = {
        "byr": "19[2-9][0-9]|200[0-2]",
        "iyr": "20(1[0-9]|20)",
        "eyr": "20(2[0-9]|30)",
        "hgt": "1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in",
        "hcl": "#[0-9a-f]{6}",
        "ecl": "amb|blu|brn|gry|grn|hzl|oth",
        "pid": "[0-9]{9}",
        "cid": ".*"
    }
    result = sum((all((re.fullmatch(patterns[v], val[v]) for v in val)) for val in data))
    ic(result)


def main():
    data = read_input()
    ic("Part one:")
    validated_passports = part_one(data)
    ic("Part two:")
    part_two(validated_passports)


if __name__ == '__main__':
    main()
