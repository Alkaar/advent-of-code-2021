import itertools


def parse_input():
    lines = []
    with open("resources/day11.txt") as file:
        while line := file.readline().rstrip():
            lines.append(list(map(int, list(line))))

    return lines


def check_boundaries(lines, coors):
    return True if 0 <= coors[0] < len(lines) and 0 <= coors[1] < len(lines[0]) else False


def play_steps(steps=None):
    lines = parse_input()
    uber_flash = None
    t = 0
    num_flashers = 0

    while (steps is not None and t < steps) or (steps is None and uber_flash is None):
        flashers = []
        for x in range(0, len(lines[0])):
            for y in range(0, len(lines)):
                lines[y][x] += 1
                if lines[y][x] > 9:
                    flashers.append((y, x))

        flashed = []
        while flashers:
            coors = flashers.pop()
            num_flashers += 1
            flashed.append(coors)
            adjacent = [(coors[0] + 1, coors[1]), (coors[0] - 1, coors[1]), (coors[0], coors[1] + 1),
                        (coors[0], coors[1] - 1), (coors[0] + 1, coors[1] + 1), (coors[0] + 1, coors[1] - 1),
                        (coors[0] - 1, coors[1] + 1), (coors[0] - 1, coors[1] - 1)]

            valid_adjacent = list(filter(lambda c: check_boundaries(lines, c) and c not in flashed, adjacent))

            for i in valid_adjacent:
                lines[i[0]][i[1]] += 1
                if lines[i[0]][i[1]] > 9 and (i[0], i[1]) not in flashers:
                    flashers.append((i[0], i[1]))

        for i in flashed:
            lines[i[0]][i[1]] = 0

        if sum(list(itertools.chain.from_iterable(lines))) == 0:
            uber_flash = t

        t += 1

    return t + 1, num_flashers


def solution1():
    return play_steps(100)[1]


def solution2():
    return play_steps()[0]


print(solution1())
print(solution2())
