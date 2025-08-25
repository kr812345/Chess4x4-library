# chess4x4/board.py

class Board:
    def __init__(self, size=4):
        self.size = size
        self.grid = [["--" for _ in range(size)] for _ in range(size)]
        self.pieces = []

    def add_piece(self, piece):
        r, c = piece.position
        self.pieces.append(piece)
        self.grid[r][c] = piece.get_symbol()

    def move_piece(self, piece, new_position):
        old_r, old_c = piece.position
        self.grid[old_r][old_c] = "--"

        new_r, new_c = new_position
        piece.position = (new_r, new_c)
        self.grid[new_r][new_c] = piece.get_symbol()

    def remove_piece(self, piece):
        r, c = piece.position
        self.grid[r][c] = "--"
        self.pieces.remove(piece)

    def print_board(self):
        for row in self.grid:
            print(" ".join(row))
        print()
