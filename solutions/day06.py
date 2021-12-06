def parse_input():
    file = open("resources/day06.txt", "r")
    fishes = file.readline().rstrip().split(",")

    fishes_dict = {}
    for fish in list(map(int, fishes)):
        fishes_dict[fish] = fishes_dict[fish] + 1 if fish in fishes_dict else 1

    return fishes_dict


def game_of_life(days):
    fishes = parse_input()
    for t in range(0, days):
        new_fishes = {}
        for i in fishes.keys():
            if i == 0:
                new_fishes[6] = fishes[i] + new_fishes[6] if 6 in new_fishes else fishes[i]
                new_fishes[8] = fishes[i] + new_fishes[8] if 8 in new_fishes else fishes[i]
            elif i == 7:
                new_fishes[6] = fishes[i] + new_fishes[6] if 6 in new_fishes else fishes[i]
            else:
                new_fishes[i-1] = fishes[i]

        fishes = new_fishes

    return sum(fishes.values())


def solution1():
    return game_of_life(80)


def solution2():
    return game_of_life(256)


print(solution1())
print(solution2())
