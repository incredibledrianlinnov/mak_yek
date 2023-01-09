class Move:
    def __init__(self, position_from: (int, int), position_to: (int, int), kills: list[(int, int)] = None):
        self.position_from = position_from
        self.position_to = position_to
        if not kills:
            self.kills = []
        else:
            self.kills = kills
