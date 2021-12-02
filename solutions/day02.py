def parse_input_commands():
    commands = []
    with open("resources/day02.txt") as file:
        while line := file.readline().rstrip():
            command = line.split()
            commands.append((command[0], int(command[1])))

    return commands


def solution1():
    x, y = 0, 0
    for command in parse_input_commands():
        if command[0] == 'forward':
            x = x + command[1]
        elif command[0] == 'down':
            y = y + command[1]
        elif command[0] == 'up':
            y = y - command[1]

    return x * y


def solution2():
    x, y, aim = 0, 0, 0
    for command in parse_input_commands():
        if command[0] == 'forward':
            x = x + command[1]
            y = y + aim * command[1]
        elif command[0] == 'down':
            aim = aim + command[1]
        elif command[0] == 'up':
            aim = aim - command[1]

    return x * y


print(solution1())
print(solution2())
