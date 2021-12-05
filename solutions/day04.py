import itertools


class Spot(object):
    def __init__(self, number, marked=False):
        self.number = number
        self.marked = marked

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Spot({self.number}, {self.marked})"


def parse_input():
    with open("resources/day04.txt") as file:
        moves = file.readline().rstrip().split(",")

        bingo_boards, bingo_board = [], []
        while line := file.readline():
            bingo_board.append([Spot(num) for num in line.rstrip().split()])
            if len(bingo_board) == 6:
                bingo_boards.append(bingo_board[1:])
                bingo_board = []

    return moves, bingo_boards


def update_bingo_boards(bingo_boards, move):
    for bingo_board in bingo_boards:
        for y in range(0, len(bingo_board[0])):
            for x in range(0, len(bingo_board)):
                if bingo_board[y][x].number == move:
                    bingo_board[y][x].marked = True


def score_bingo_board(bingo_board, move):
    flattened_board = list(itertools.chain.from_iterable(bingo_board))
    return sum(int(s.number) for s in list(filter(lambda s: s.marked is False, flattened_board))) * int(move)


def find_winning_board(bingo_boards):
    winner_found, winning_board_num, board_num = False, None, 0

    while not winner_found and board_num < len(bingo_boards):
        board = bingo_boards[board_num]

        i = 0
        while winner_found is False and i < len(board):
            if ((len(list(filter(lambda s: s.marked is True, board[i]))) == 5) or
                    (len(list(filter(lambda s: s.marked is True, [col[i] for col in board]))) == 5)):
                winner_found = True
                winning_board_num = board_num
            i = i + 1

        board_num = board_num + 1

    return winning_board_num


def solution1():
    moves, bingo_boards = parse_input()

    move, winning_board_num = None, None
    while winning_board_num is None:
        move = moves[0]
        moves.pop(0)

        update_bingo_boards(bingo_boards, move)

        winning_board_num = find_winning_board(bingo_boards)

    return score_bingo_board(bingo_boards[winning_board_num], move)


def find_winning_boards(bingo_boards):
    winning_boards, board_num = [], 0

    for board_num in range(0, len(bingo_boards)):
        board = bingo_boards[board_num]

        winner_found, i = False, 0
        while winner_found is False and i < len(board):
            if ((len(list(filter(lambda s: s.marked is True, board[i]))) == 5) or
                    (len(list(filter(lambda s: s.marked is True, [col[i] for col in board]))) == 5)):
                winner_found = True
                winning_boards.append(board_num)
            i = i + 1

    return winning_boards


def solution2():
    moves, bingo_boards = parse_input()

    move, losing_board = None, None
    while len(bingo_boards) > 0:
        move = moves[0]
        moves.pop(0)

        update_bingo_boards(bingo_boards, move)

        winning_boards = find_winning_boards(bingo_boards)

        if winning_boards is not None:
            if len(bingo_boards) == 1:
                losing_board = bingo_boards[0]
            winning_boards.reverse()
            for i in winning_boards:
                del bingo_boards[i]

    return score_bingo_board(losing_board, move)


print(solution1())
print(solution2())
