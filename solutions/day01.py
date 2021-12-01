from itertools import islice


def solution1():
    num_increases = 0

    with open("resources/day01.txt") as file:
        prev = file.readline().rstrip()
        while curr := file.readline().rstrip():
            if int(curr) > int(prev):
                num_increases = num_increases + 1
            prev = curr
    return num_increases


def solution2():
    num_increases = 0

    with open("resources/day01.txt") as file:
        window = [int(x.rstrip()) for x in list(islice(file, 3))]
        while curr_depth := file.readline().rstrip():
            window.append(int(curr_depth))
            if sum(window[1:]) > sum(window[:3]):
                num_increases = num_increases + 1
            window.pop(0)
    return num_increases


print(solution1())
print(solution2())
