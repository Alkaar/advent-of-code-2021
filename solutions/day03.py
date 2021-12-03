from enum import Enum


def parse_input():
    lines = []
    with open("resources/day03.txt") as file:
        while line := file.readline().rstrip():
            lines.append(line)

    return lines


def solution1():
    lines, gamma_rate_binary, epsilon_rate = parse_input(), "", 0

    for x in range(0, len(lines[0])):
        num_ones = 0
        for y in range(0, len(lines)):
            num_ones = num_ones + int(lines[y][x])
        if num_ones > len(lines) / 2:
            gamma_rate_binary = gamma_rate_binary + "1"
        else:
            gamma_rate_binary = gamma_rate_binary + "0"

    gamma_rate = int(gamma_rate_binary, 2)
    epsilon_rate = (gamma_rate ^ 2 ** len(gamma_rate_binary) - 1)

    return gamma_rate * epsilon_rate


class RatingType(Enum):
    OXYGEN_RATING = 1
    C02_RATING = 2


def rating_bit_criteria(num_ones, total, rating_type):
    bit_criteria = None

    if rating_type == RatingType.OXYGEN_RATING:
        if num_ones >= total / 2:
            bit_criteria = 1
        else:
            bit_criteria = 0
    if rating_type == RatingType.C02_RATING:
        if num_ones >= total / 2:
            bit_criteria = 0
        else:
            bit_criteria = 1

    return bit_criteria


def get_life_support_rating(lines, rating_type):
    x = 0
    while len(lines) > 1:
        num_ones = 0
        for y in range(0, len(lines)):
            num_ones = num_ones + int(lines[y][x])
        bad_ratings = []
        for line in lines:
            if rating_bit_criteria(num_ones, len(lines), rating_type) != int(line[x]):
                bad_ratings.append(line)
        lines = list(set(lines) - set(bad_ratings))
        x = x + 1

    return int(lines[0], 2)


def solution2():
    lines = parse_input()

    return get_life_support_rating(lines, RatingType.OXYGEN_RATING) * get_life_support_rating(lines, RatingType.C02_RATING)


print(solution1())
print(solution2())
