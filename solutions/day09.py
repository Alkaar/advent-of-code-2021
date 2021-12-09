from functools import reduce


class Spot(object):
    def __init__(self, height, visited=False):
        self.height = int(height)
        self.visited = visited

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Spot({self.height}, {self.visited})"


def parse_input():
    height_map = []
    with open("resources/day09.txt") as file:
        while row := file.readline().rstrip():
            height_map.append(list(map(Spot, row)))

    return height_map


def check_boundaries(height_map, coors):
    return True if 0 <= coors[0] < len(height_map) and 0 <= coors[1] < len(height_map[0]) else False


def find_low_point(height_map, y, x):
    queue = [(y, x)]
    low_point = None
    while queue and low_point is None:
        coors = queue.pop()
        height_map[coors[0]][coors[1]].visited = True
        adjacent = [(coors[0] + 1, coors[1]), (coors[0] - 1, coors[1]), (coors[0], coors[1] + 1),
                    (coors[0], coors[1] - 1)]
        valid_adjacent = list(filter(lambda c: check_boundaries(height_map, c), adjacent))
        if all(height_map[coors[0]][coors[1]].height < height_map[adj[0]][adj[1]].height for adj in valid_adjacent):
            low_point = coors
        else:
            queue += list(filter(lambda c: not height_map[c[0]][c[1]].visited, valid_adjacent))

    return low_point


def get_low_points(height_map):
    low_points = []
    for y in range(0, len(height_map)):
        for x in range(0, len(height_map[0])):
            if not height_map[y][x].visited and check_boundaries(height_map, (y, x)):
                coors = find_low_point(height_map, y, x)
                if coors is not None:
                    low_points.append(coors)

    return low_points


def solution1():
    height_map = parse_input()
    low_points = get_low_points(height_map)

    return sum(map(lambda coors: height_map[coors[0]][coors[1]].height, low_points)) + len(low_points)


def calc_basin_size(height_map, y, x):
    queue = [(y, x)]
    visited = {(y, x)}
    size = 0
    while queue:
        coors = queue.pop()
        size += 1
        adjacent = [(coors[0] + 1, coors[1]), (coors[0] - 1, coors[1]), (coors[0], coors[1] + 1),
                    (coors[0], coors[1] - 1)]
        valid_adjacent = list(
            filter(lambda c: c not in visited and check_boundaries(height_map, c) and height_map[c[0]][c[1]].height < 9,
                   adjacent))
        queue += valid_adjacent
        visited |= set(valid_adjacent)

    return size


def solution2():
    height_map = parse_input()
    low_points = get_low_points(height_map)

    basin_sizes = []
    for c in low_points:
        basin_sizes.append(calc_basin_size(height_map, c[0], c[1]))

    top_3 = sorted(basin_sizes, reverse=True)[:3]

    return reduce((lambda x, y: x * y), top_3)


print(solution1())
print(solution2())
