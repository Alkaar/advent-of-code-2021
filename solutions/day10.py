from statistics import median


def parse_input():
    lines = []
    with open("resources/day10.txt") as file:
        while line := file.readline().rstrip():
            lines.append(line)

    return lines


def solution1():
    score = 0
    for line in parse_input():
        stack = []
        for char in line:
            if char in ["(", "[", "{", "<"]:
                stack.append(char)
            else:
                start_chunk = stack.pop()
                score += 3 if start_chunk != "(" and char == ")" else False
                score += 57 if start_chunk != "[" and char == "]" else False
                score += 1197 if start_chunk != "{" and char == "}" else False
                score += 25137 if start_chunk != "<" and char == ">" else False

    return score


def solution2():
    scores = []
    for line in parse_input():
        stack = []
        is_incomplete = True
        for char in line:
            if char in ["(", "[", "{", "<"]:
                stack.append(char)
            else:
                if (stack[-1] == "(" and char == ")") or (stack[-1] == "[" and char == "]") or (
                        stack[-1] == "{" and char == "}") or (stack[-1] == "<" and char == ">"):
                    stack.pop()
                elif (stack[-1] != "(" and char == ")") or (stack[-1] != "[" and char == "]") or (
                        stack[-1] != "{" and char == "}") or (stack[-1] != "<" and char == ">"):
                    is_incomplete = False

        if is_incomplete:
            stack.reverse()
            score = 0
            for char in stack:
                score *= 5
                score += 1 if char == "(" else False
                score += 2 if char == "[" else False
                score += 3 if char == "{" else False
                score += 4 if char == "<" else False
            scores.append(score)

    return median(scores)


print(solution1())
print(solution2())
