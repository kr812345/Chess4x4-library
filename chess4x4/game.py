# chess4x4/game.py

from .pieces import King, Rook
from .board import Board

class Chess4x4:
    def __init__(self):
        self.board = Board(4)
        self.turn = "W"  # White starts

    def setup(self, wk_pos, wr_pos, bk_pos):
        """Custom setup: give positions as (row, col)."""
        self.wk = King("W", wk_pos)
        self.wr = Rook("W", wr_pos)
        self.bk = King("B", bk_pos)

        self.board.add_piece(self.wk)
        self.board.add_piece(self.wr)
        self.board.add_piece(self.bk)

    def make_move(self, piece, new_position):
        # If move captures opponent king -> WIN
        target = [p for p in self.board.pieces if p.position == new_position]
        if target:
            captured = target[0]
            if captured.name == "K" and captured.color != piece.color:
                self.board.remove_piece(captured)
                self.board.move_piece(piece, new_position)
                return f"{piece.color} wins by capturing King!"

        self.board.move_piece(piece, new_position)
        self.turn = "B" if self.turn == "W" else "W"
        return "Move made."

    def is_draw(self):
        # Draw if only 2 kings remain
        kings = [p for p in self.board.pieces if p.name == "K"]
        return len(kings) == 2

    def is_in_check(self, king):
        """Check if a king is attacked by rook."""
        enemy_pieces = [p for p in self.board.pieces if p.color != king.color]
        for p in enemy_pieces:
            if king.position in p.possible_moves():
                return True
        return False

    def print_board(self):
        self.board.print_board()
