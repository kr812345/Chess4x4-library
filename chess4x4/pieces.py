# chess4x4/pieces.py

class Piece:
    def __init__(self, color, name, position):
        self.color = color  # "W" or "B"
        self.name = name    # "K" for King, "R" for Rook
        self.position = position  # (row, col)

    def get_symbol(self):
        return f"{self.color}{self.name}"


class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, "K", position)

    def possible_moves(self, board_size=4):
        r, c = self.position
        moves = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < board_size and 0 <= nc < board_size:
                    moves.append((nr, nc))
        return moves


class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, "R", position)

    def possible_moves(self, board_size=4):
        r, c = self.position
        moves = []
        for i in range(board_size):
            if i != r:
                moves.append((i, c))
            if i != c:
                moves.append((r, i))
        return moves
