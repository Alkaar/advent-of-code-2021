from enum import Enum
import sys


class Node(object):
    def __init__(self, risk, tentative_risk=sys.maxsize):
        self.risk = int(risk)
        self.tentative_risk = tentative_risk

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Node({self.risk}, {self.tentative_risk})"


def parse_input():
    with open("resources/day15.txt") as file:
        lines = []
        while line := file.readline().rstrip():
            lines.append(list(map(Node, list(line))))

    return lines


def check_boundaries(grid, coors):
    return True if 0 <= coors[0] < len(grid) and 0 <= coors[1] < len(grid[0]) else False


def dijkstras_algorithm(grid, start, end):
    unvisited = set()
    curr = start
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            unvisited.add((y, x))

    while (len(grid)-1, len(grid)-1) in unvisited:
        unvisited.remove(curr)

        neighbors = ((curr[0] - 1, curr[1]), (curr[0] + 1, curr[1]), (curr[0], curr[1] + 1), (curr[0], curr[1] - 1))
        valid_neighbors = list(filter(lambda c: check_boundaries(grid, c) and c in unvisited, neighbors))

        min_risk = sys.maxsize
        min_risk_node = None
        for i in valid_neighbors:
            curr_node = grid[curr[0]][curr[1]]
            neighbor = grid[i[0]][i[1]]

            if grid[i[0]][i[1]].tentative_risk > curr_node.tentative_risk + neighbor.risk:
                grid[i[0]][i[1]] = Node(neighbor.risk, curr_node.tentative_risk + neighbor.risk)
        for i in unvisited:
            if grid[i[0]][i[1]].tentative_risk < min_risk:
                min_risk = grid[i[0]][i[1]].tentative_risk
                min_risk_node = (i[0], i[1])

        curr = min_risk_node

    return grid[end[0]][end[1]].tentative_risk


def solution1():
    grid = parse_input()
    grid[0][0] = Node(0, 0)

    return dijkstras_algorithm(grid, (0, 0), (len(grid)-1, len(grid)-1))


class ExtendType(Enum):
    RIGHT = 1
    DOWN = 2


def extend_grid(orig_grid, extend_type):
    grid = orig_grid
    for i in range(0, 4):
        new_grid = build_new_grid(grid)
        for j in range(0, len(grid)):
            if extend_type == ExtendType.RIGHT:
                orig_grid[j] = orig_grid[j] + new_grid[j]
            elif extend_type == ExtendType.DOWN:
                orig_grid.append(new_grid[j])

        grid = new_grid
    return orig_grid


def build_new_grid(grid):
    new_grid = []
    for y in range(0, len(grid)):
        line = []
        for x in range(0, len(grid[0])):
            new_risk = grid[y][x].risk + 1 if grid[y][x].risk < 9 else 1
            line.append(Node(new_risk))
        new_grid.append(line)

    return new_grid


"""
This takes 4 hours to run! I could fix it by using a min heap for finding the next unvisited node to evaluate via 
heapq but didn't want to go through the effort to do that :P
"""
def solution2():
    grid = parse_input()

    grid = extend_grid(grid, ExtendType.RIGHT)
    grid = extend_grid(grid, ExtendType.DOWN)

    grid[0][0] = Node(0, 0)
    return dijkstras_algorithm(grid, (0, 0), (len(grid)-1, len(grid)-1))


print(solution1())
print(solution2())
