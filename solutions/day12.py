from enum import Enum


class CaveType(Enum):
    BIG = 1
    SMALL = 2


class Cave(object):
    def __init__(self, name, cave_type):
        self.name = name
        self.cave_type = cave_type

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Cave({self.name}, {self.cave_type})"

    def __key(self):
        return self.name, self.cave_type

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        return self.__key() == other.__key()


start_cave = Cave("start", CaveType.SMALL)


def parse_input():
    cave_system = {}

    with open("resources/day12.txt") as file:
        while cave_connection := file.readline().rstrip():
            caves = cave_connection.split("-")

            cave1 = Cave(caves[0], CaveType.SMALL) if caves[0].islower() else Cave(caves[0], CaveType.BIG)
            cave2 = Cave(caves[1], CaveType.SMALL) if caves[1].islower() else Cave(caves[1], CaveType.BIG)

            if cave2 != start_cave:
                cave_system[cave1] = [cave2] if cave1 not in cave_system else cave_system[cave1] + [cave2]
            if cave1 != start_cave:
                cave_system[cave2] = [cave1] if cave2 not in cave_system else cave_system[cave2] + [cave1]

    return cave_system


def find_paths(cave_system, cave=start_cave, visited=None):
    if visited is None:
        visited = []

    if cave == Cave("end", CaveType.SMALL):
        return 1
    else:
        new_visited = visited.copy()
        if cave.cave_type == CaveType.SMALL:
            new_visited.append(cave)

        paths = list(filter(lambda c: c not in visited, cave_system[cave]))

        return sum(list(map(lambda c: find_paths(cave_system, c, new_visited), paths)))


def solution1():
    # Can also call find_more_paths and just set visited_twice to True
    return find_paths(parse_input(), start_cave)


def find_more_paths(cave_system, cave=start_cave, visited=None, visited_twice=False):
    if visited is None:
        visited = []

    if cave == Cave("end", CaveType.SMALL):
        return 1
    else:
        new_visited = visited.copy()
        if cave.cave_type == CaveType.SMALL:
            if cave in visited:
                visited_twice = True
            else:
                new_visited.append(cave)

        paths = list(filter(lambda c: (visited_twice is False) or (visited_twice is True and c not in visited),
                            cave_system[cave]))

        return sum(list(map(lambda c: find_more_paths(cave_system, c, new_visited, visited_twice), paths)))


def solution2():
    return find_more_paths(parse_input())


print(solution1())
print(solution2())
