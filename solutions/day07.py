from enum import Enum
import sys


def parse_input():
    return list(map(int, open("resources/day07.txt", "r").readline().rstrip().split(",")))


class FuelConsumptionType(Enum):
    LINEAR = 1
    GAUSS_FORMULA = 2


def lowest_fuel(fuel_consumption_type):
    crabs = parse_input()

    min_fuel = sys.maxsize
    for i in range(min(crabs), max(crabs)):
        calc_fuel = 0
        for j in crabs:
            fuel_used = 0
            if fuel_consumption_type == FuelConsumptionType.LINEAR:
                fuel_used = abs(i - j)
            elif fuel_consumption_type == FuelConsumptionType.GAUSS_FORMULA:
                fuel_used = (abs(i - j) * (abs(i - j) + 1))/2

            calc_fuel = calc_fuel + fuel_used
        min_fuel = calc_fuel if calc_fuel < min_fuel else min_fuel

    return min_fuel


def solution1():
    return lowest_fuel(FuelConsumptionType.LINEAR)


def solution2():
    return lowest_fuel(FuelConsumptionType.GAUSS_FORMULA)


print(solution1())
print(solution2())
