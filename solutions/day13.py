from enum import Enum


def parse_input():
    paper = set()
    folds = []

    with open("resources/day13.txt") as file:
        while line := file.readline():
            if "," in line:
                paper.add(tuple(map(int, line.rstrip().split(","))))

            if "fold along" in line:
                folds.append(list(map(lambda f: [f[0], int(f[1])], [line.rstrip().strip("fold along").split("=")]))[0])

    return paper, folds


class FoldType(Enum):
    HORIZONTAL = 0
    VERTICAL = 1


def folding(paper, fold_line, fold_type):
    x_or_y = None
    if fold_type == FoldType.VERTICAL:
        x_or_y = 0
    elif fold_type == FoldType.HORIZONTAL:
        x_or_y = 1

    paper = set(filter(lambda d: d[x_or_y] != fold_line, paper))
    new_paper = set()
    for d in paper:
        if d[x_or_y] > fold_line:
            if fold_type == FoldType.HORIZONTAL:
                new_paper.add((d[0], d[1] - ((d[1] - fold_line) * 2)))
            if fold_type == FoldType.VERTICAL:
                new_paper.add((d[0] - ((d[0] - fold_line) * 2), d[1]))
        else:
            new_paper.add(d)

    return new_paper


def fold_paper(paper, fold):
    if fold[0] == "y":
        paper = folding(paper, fold[1], FoldType.HORIZONTAL)
    if fold[0] == "x":
        paper = folding(paper, fold[1], FoldType.VERTICAL)

    return paper


def solution1():
    paper, folds = parse_input()

    return len(fold_paper(paper, folds[0]))


def print_paper(paper):
    max_x = max(list(map(lambda d: d[0], paper)))
    max_y = max(list(map(lambda d: d[1], paper)))

    for y in range(0, max_y+1):
        line = ""
        for x in range(0, max_x+1):
            line += "#" if (x, y) in paper else "."
        print(line)


def solution2():
    paper, folds = parse_input()

    for fold in folds:
        paper = fold_paper(paper, fold)

    print_paper(paper)


print(solution1())
solution2()
