from models.figure_type import FigureType
from models.move import Move


def valid_coords(x: int, y: int) -> bool:
    return 0 <= x < 8 and 0 <= y < 8


def get_figure_at(board: list[list[FigureType]], x: int, y: int):
    if not valid_coords(x, y):
        return FigureType.Wall
    return board[x][y]


def is_checker(figure: FigureType) -> bool:
    return int(figure) >= 1


def is_opposite_side(first: FigureType, second: FigureType) -> bool:
    if int(first) < 1 or int(second) < 1:
        return False
    return int(first) % 2 != int(second) % 2


def get_moves_with_kills(board: list[list[FigureType]], x: int, y: int, move_before: Move = None) -> list[Move]:
    result = []
    current_figure = get_figure_at(board, x, y)
    if current_figure == FigureType.White:
        left = get_figure_at(board, x - 1, y - 1)
        if get_figure_at(board, x - 2, y - 2) == FigureType.Null and (
                left == FigureType.Black or left == FigureType.BlackQueen):

            move = Move((x, y) if move_before is None else move_before.position_from, (x - 2, y - 2),
                        [(x - 1, y - 1)] if move_before is None else [i for i in move_before.kills] + [(x - 1, y - 1)])
            new_board = [[j for j in i] for i in board]
            new_board[x][y] = FigureType.Null
            new_board[x - 1][y - 1] = FigureType.Null
            new_board[x - 2][y - 2] = FigureType.White
            for i in get_moves_with_kills(new_board, x - 2, y - 2, move):
                result.append(i)

        right = get_figure_at(board, x + 1, y - 1)
        if get_figure_at(board, x + 2, y - 2) == FigureType.Null and (
                right == FigureType.Black or right == FigureType.BlackQueen):
            move = Move((x, y) if move_before is None else move_before.position_from, (x + 2, y - 2),
                        [(x + 1, y - 1)] if move_before is None else [i for i in move_before.kills] + [(x + 1, y - 1)])
            new_board = [[j for j in i] for i in board]
            new_board[x][y] = FigureType.Null
            new_board[x + 1][y - 1] = FigureType.Null
            new_board[x + 2][y - 2] = FigureType.White
            for i in get_moves_with_kills(new_board, x + 2, y - 2, move):
                result.append(i)
    elif current_figure == FigureType.Black:
        move = Move((x, y) if move_before is None else move_before.position_from, (x - 2, y + 2),
                    [(x - 1, y + 1)] if move_before is None else [i for i in move_before.kills] + [(x - 1, y + 1)])
        left = get_figure_at(board, x - 1, y + 1)
        if get_figure_at(board, x - 2, y + 2) == FigureType.Null and (
                left == FigureType.White or left == FigureType.WhiteQueen):
            new_board = [[j for j in i] for i in board]
            new_board[x][y] = FigureType.Null
            new_board[x - 1][y + 1] = FigureType.Null
            new_board[x - 2][y + 2] = FigureType.Black
            for i in get_moves_with_kills(new_board, x - 2, y + 2, move):
                result.append(i)

        right = get_figure_at(board, x + 1, y + 1)
        if get_figure_at(board, x + 2, y + 2) == FigureType.Null and (
                right == FigureType.White or right == FigureType.WhiteQueen):
            move = Move((x, y) if move_before is None else move_before.position_from, (x + 2, y + 2),
                        [(x + 1, y + 1)] if move_before is None else [i for i in move_before.kills] + [(x + 1, y + 1)])
            new_board = [[j for j in i] for i in board]
            new_board[x][y] = FigureType.Null
            new_board[x + 1][y + 1] = FigureType.Null
            new_board[x + 2][y + 2] = FigureType.Black
            for i in get_moves_with_kills(new_board, x + 2, y + 2, move):
                result.append(i)
    elif current_figure == FigureType.BlackQueen or current_figure == FigureType.WhiteQueen:
        dx = 1
        dy = 1
        while get_figure_at(board, x + dx, y + dy) == FigureType.Null:
            dx += 1
            dy += 1
        figure = get_figure_at(board, x + dx, y + dy)
        if is_checker(figure) and is_opposite_side(current_figure, figure) and get_figure_at(board, x + dx + 1,
                                                                                             y + dy + 1) == FigureType.Null:
            if move_before is None:
                move = Move((x, y), (x + dx + 1, y + dy + 1), [(x + dx, y + dy)])
            else:
                move = Move(move_before.position_from, (x + dx + 1, y + dy + 1),
                            [i for i in move_before.kills] + [(x + dx, y + dy)])

            new_board = [[j for j in i] for i in board]
            new_board[x][y] = FigureType.Null
            new_board[x + dx][y + dy] = FigureType.Null
            new_board[x + dx + 1][y + dy + 1] = current_figure
            for i in get_moves_with_kills(new_board, x + dx + 1, y + dy + 1, move):
                result.append(i)

        dx = -1
        dy = 1
        while get_figure_at(board, x + dx, y + dy) == FigureType.Null:
            dx -= 1
            dy += 1
        figure = get_figure_at(board, x + dx, y + dy)
        if is_checker(figure) and is_opposite_side(current_figure, figure) and get_figure_at(board, x + dx - 1,
                                                                                             y + dy + 1) == FigureType.Null:
            if move_before is None:
                move = Move((x, y), (x + dx - 1, y + dy + 1), [(x + dx, y + dy)])
            else:
                move = Move(move_before.position_from, (x + dx - 1, y + dy + 1),
                            [i for i in move_before.kills] + [(x + dx, y + dy)])

            new_board = [[j for j in i] for i in board]
            new_board[x][y] = FigureType.Null
            new_board[x + dx][y + dy] = FigureType.Null
            new_board[x + dx - 1][y + dy + 1] = current_figure
            for i in get_moves_with_kills(new_board, x + dx - 1, y + dy + 1, move):
                result.append(i)

        dx = -1
        dy = -1
        while get_figure_at(board, x + dx, y + dy) == FigureType.Null:
            dx -= 1
            dy -= 1
        figure = get_figure_at(board, x + dx, y + dy)
        if is_checker(figure) and is_opposite_side(current_figure, figure) and get_figure_at(board, x + dx - 1,
                                                                                             y + dy - 1) == FigureType.Null:
            if move_before is None:
                move = Move((x, y), (x + dx - 1, y + dy - 1), [(x + dx, y + dy)])
            else:
                move = Move(move_before.position_from, (x + dx - 1, y + dy - 1),
                            [i for i in move_before.kills] + [(x + dx, y + dy)])

            new_board = [[j for j in i] for i in board]
            new_board[x][y] = FigureType.Null
            new_board[x + dx][y + dy] = FigureType.Null
            new_board[x + dx - 1][y + dy - 1] = current_figure
            for i in get_moves_with_kills(new_board, x + dx - 1, y + dy - 1, move):
                result.append(i)

        dx = 1
        dy = -1
        while get_figure_at(board, x + dx, y + dy) == FigureType.Null:
            dx += 1
            dy -= 1
        figure = get_figure_at(board, x + dx, y + dy)
        if is_checker(figure) and is_opposite_side(current_figure, figure) and get_figure_at(board, x + dx + 1,
                                                                                             y + dy - 1) == FigureType.Null:
            if move_before is None:
                move = Move((x, y), (x + dx + 1, y + dy - 1), [(x + dx, y + dy)])
            else:
                move = Move(move_before.position_from, (x + dx + 1, y + dy - 1),
                            [i for i in move_before.kills] + [(x + dx, y + dy)])

            new_board = [[j for j in i] for i in board]
            new_board[x][y] = FigureType.Null
            new_board[x + dx][y + dy] = FigureType.Null
            new_board[x + dx + 1][y + dy - 1] = current_figure
            for i in get_moves_with_kills(new_board, x + dx + 1, y + dy - 1, move):
                result.append(i)

    if move_before is not None and len(result) == 0:
        result.append(move_before)
    return result


class Board:
    def __init__(self, position: str):
        self.board = [[FigureType.Null for __ in range(8)] for _ in range(8)]
        self.turn = 0

        for i in range(32):
            pos = i * 2 + (i // 4 + 1) % 2
            y = pos // 8
            x = pos % 8
            if position[i] == 'p':
                self.board[x][y] = FigureType.Black
            elif position[i] == 'q':
                self.board[x][y] = FigureType.BlackQueen
            elif position[i] == 'P':
                self.board[x][y] = FigureType.White
            elif position[i] == 'Q':
                self.board[x][y] = FigureType.WhiteQueen

    def get_figure_at(self, x: int, y: int) -> FigureType:
        return get_figure_at(self.board, x, y)

    def get_moves_for(self, x: int, y: int) -> list[Move]:
        if int(self.get_figure_at(x, y)) < 1:
            return []

        if int(self.get_figure_at(x, y) % 2 == self.turn):
            return []

        result = get_moves_with_kills(self.board, x, y)

        if self.get_figure_at(x, y) == FigureType.White:
            if self.get_figure_at(x - 1, y - 1) == FigureType.Null:
                result.append(Move((x, y), (x - 1, y - 1)))
            if self.get_figure_at(x + 1, y - 1) == FigureType.Null:
                result.append(Move((x, y), (x + 1, y - 1)))

        if self.get_figure_at(x, y) == FigureType.Black:
            if self.get_figure_at(x - 1, y + 1) == FigureType.Null:
                result.append(Move((x, y), (x - 1, y + 1)))
            if self.get_figure_at(x + 1, y + 1) == FigureType.Null:
                result.append(Move((x, y), (x + 1, y + 1)))

        if self.get_figure_at(x, y) == FigureType.WhiteQueen or self.get_figure_at(x, y) == FigureType.BlackQueen:
            dx = 0
            dy = 0
            while True:
                dx += 1
                dy += 1
                if self.get_figure_at(x + dx, y + dy) == FigureType.Null:
                    result.append(Move((x, y), (x + dx, y + dy)))
                else:
                    break

            dx = 0
            dy = 0
            while True:
                dx -= 1
                dy += 1
                if self.get_figure_at(x + dx, y + dy) == FigureType.Null:
                    result.append(Move((x, y), (x + dx, y + dy)))
                else:
                    break

            dx = 0
            dy = 0
            while True:
                dx += 1
                dy -= 1
                if self.get_figure_at(x + dx, y + dy) == FigureType.Null:
                    result.append(Move((x, y), (x + dx, y + dy)))
                else:
                    break

            dx = 0
            dy = 0
            while True:
                dx -= 1
                dy -= 1
                if self.get_figure_at(x + dx, y + dy) == FigureType.Null:
                    result.append(Move((x, y), (x + dx, y + dy)))
                else:
                    break

        return result

    def move(self, move: Move):
        self.board[move.position_from[0]][move.position_from[1]], self.board[move.position_to[0]][move.position_to[1]] = \
            self.board[move.position_to[0]][move.position_to[1]], self.board[move.position_from[0]][
                move.position_from[1]]

        for i in move.kills:
            self.board[i[0]][i[1]] = FigureType.Null

        if move.position_to[1] == 7 and self.get_figure_at(move.position_to[0],
                                                           move.position_to[1]) == FigureType.Black:
            self.board[move.position_to[0]][move.position_to[1]] = FigureType.BlackQueen
        elif move.position_to[1] == 0 and self.get_figure_at(move.position_to[0],
                                                             move.position_to[1]) == FigureType.White:
            self.board[move.position_to[0]][move.position_to[1]] = FigureType.WhiteQueen

        self.turn = int(not self.turn)

    def to_string(self, mirror=False) -> str:
        result = ''
        for i in range(32):
            pos = i * 2 + (i // 4 + 1) % 2
            y = pos // 8
            x = pos % 8
            if self.board[x][y] == FigureType.Black:
                result += 'p'
            elif self.board[x][y] == FigureType.BlackQueen:
                result += 'q'
            elif self.board[x][y] == FigureType.White:
                result += 'P'
            elif self.board[x][y] == FigureType.WhiteQueen:
                result += 'Q'
            else:
                result += '*'

        if mirror:
            return result[::-1].replace('p', 'r').replace('q', 't').replace('P', 'p').replace('Q', 'q').replace('r', 'P').replace('t', 'Q')
        return result