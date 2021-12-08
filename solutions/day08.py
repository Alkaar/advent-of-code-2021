import itertools


def parse_input():
    segments = []
    with open("resources/day08.txt") as file:
        while line := file.readline().rstrip():
            line = (line.split(" | "))
            segments.append([line[0].split(" "), map(set, line[1].split(" "))])

    return segments


def solution1():
    outputs = [i[1] for i in parse_input()]
    flattened_board = list(itertools.chain.from_iterable(outputs))

    return len(list(filter(lambda d: len(d) in (2, 3, 4, 7), flattened_board)))


def calc_segments(segments):
    one = set("".join(filter(lambda num: len(num) == 2, segments[0])))
    four = set("".join(filter(lambda num: len(num) == 4, segments[0])))
    seven = set("".join(filter(lambda num: len(num) == 3, segments[0])))
    eight = set("".join(filter(lambda num: len(num) == 7, segments[0])))
    two_three_five = list((filter(lambda num: len(num) == 5, segments[0])))
    zero_six_nine = list((filter(lambda num: len(num) == 6, segments[0])))

    a = (seven - one).pop()
    g = (list(filter(lambda s: len(s) == 1, (list(map(lambda s: set(s) - four.union(set(a)), two_three_five)))))[0]).pop()
    e = (eight - four.union({a, g})).pop()
    b = (list(filter(lambda s: len(s) == 1, (list(map(lambda s: set(s) - one.union({a, g, e}), zero_six_nine)))))[0]).pop()
    d = (eight - one.union({a, b, e, g})).pop()
    c = (list(filter(lambda s: len(s) == 1, (list(map(lambda s: set(s) - {a, d, e, g}, two_three_five)))))[0]).pop()
    f = (one - {c}).pop()

    output = ""
    for digit in segments[1]:
        if digit == {a, b, c, e, f, g}:
            output += "0"
        elif digit == {c, f}:
            output += "1"
        elif digit == {a, c, d, e, g}:
            output += "2"
        elif digit == {a, c, d, f, g}:
            output += "3"
        elif digit == {b, c, d, f}:
            output += "4"
        elif digit == {a, b, d, f, g}:
            output += "5"
        elif digit == {a, b, d, e, f, g}:
            output += "6"
        elif digit == {a, c, f}:
            output += "7"
        elif digit == {a, b, c, d, e, f, g}:
            output += "8"
        elif digit == {a, b, c, d, f, g}:
            output += "9"

    return int(output)


def solution2():
    total = 0
    for segments in parse_input():
        total += calc_segments(segments)

    return total


print(solution1())
print(solution2())
