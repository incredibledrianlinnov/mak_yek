from models.board import Board, FigureType, Move


class Game:
    def __init__(self, position: str):
        self.board = Board(position)

    def get_figure_at(self, x: int, y: int) -> FigureType:
        return self.board.get_figure_at(x, y)

    def get_moves_for(self, x: int, y: int):
        return self.board.get_moves_for(x, y)

    def move(self, move: Move):
        self.board.move(move)

    def ai_move(self, new_position: str, mirror=False):
        if mirror:
            new_position = new_position[::-1].replace('p', 'r').replace('q', 't').replace('P', 'p').replace('Q', 'q').replace('r', 'P').replace('t', 'Q')
        self.board = Board(new_position)
