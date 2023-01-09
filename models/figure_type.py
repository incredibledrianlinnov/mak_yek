import enum


class FigureType(enum.IntEnum):
    Wall = -1
    Null = 0
    White = 1
    WhiteQueen = 3
    Black = 2
    BlackQueen = 4