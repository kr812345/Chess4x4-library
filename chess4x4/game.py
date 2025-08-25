from typing import List, Tuple
from .board import Board
from .pieces import Piece, King, Rook
from .utils import validate_pos

Position = Tuple[int, int]


class Chess4x4:
    def __init__(self):
        self.board = Board()
        self.turn = "white"
        self.move_history: List[Tuple[Position, Position]] = []

    def setup_custom(self, pieces_positions: List[Tuple[Piece, Position]]) -> None:
        # clear board
        self.board = Board()
        for piece, pos in pieces_positions:
            validate_pos(pos)
            self.board.place_piece(piece, pos)

    def available_moves(self, color: str) -> List[Tuple[Position, Position]]:
        moves = []
        for r in range(4):
            for c in range(4):
                p = self.board.get_piece((r, c))
                if p is not None and p.color == color:
                    for end in p.get_moves(self.board, (r, c)):
                        moves.append(((r, c), end))
        return moves

    def move(self, start: Position, end: Position) -> None:
        validate_pos(start)
        validate_pos(end)
        piece = self.board.get_piece(start)
        if piece is None:
            raise ValueError("No piece at start position")
        if piece.color != self.turn:
            raise ValueError("It's not this piece's turn")
        legal = piece.get_moves(self.board, start)
        if end not in legal:
            raise ValueError("Illegal move for this piece")
        # perform move
        self.board.move_piece(start, end)
        self.move_history.append((start, end))
        # switch turn
        self.turn = "black" if self.turn == "white" else "white"

    def is_under_attack(self, position: Position, attacker_color: str) -> bool:
        # any opponent move that targets position
        for r in range(4):
            for c in range(4):
                p = self.board.get_piece((r, c))
                if p is not None and p.color == attacker_color:
                    if position in p.get_moves(self.board, (r, c)):
                        return True
        return False

    def is_checkmate(self, color: str) -> bool:
        # simplified: check if king is in check and the side has no legal moves
        king_pos = self.board.find_king(color)
        if king_pos is None:
            # no king -> consider checkmate
            return True
        in_check = self.is_under_attack(king_pos, "white" if color == "black" else "black")
        if not in_check:
            return False
        # if any legal move exists for color, not checkmate
        if self.available_moves(color):
            # but we must ensure none of the moves resolves check; simplified: assume any move suffices
            # to be more correct, check resulting positions
            for start, end in self.available_moves(color):
                # simulate
                saved_from = self.board.get_piece(start)
                saved_to = self.board.get_piece(end)
                self.board.move_piece(start, end)
                new_king = self.board.find_king(color)
                still_in_check = self.is_under_attack(new_king, "white" if color == "black" else "black") if new_king else True
                # undo
                self.board.move_piece(end, start)
                self.board.grid[end[0]][end[1]] = saved_to
                if not still_in_check:
                    return False
            return True
        return True

    def is_draw(self) -> bool:
        # basic draw conditions:
        # 1) only kings remain
        pieces = []
        for r in range(4):
            for c in range(4):
                p = self.board.get_piece((r, c))
                if p is not None:
                    pieces.append(p)
        if all(isinstance(p, King) for p in pieces) and len(pieces) >= 2:
            return True
        # 2) stalemate: side to move has no moves and is not in check
        avail = self.available_moves(self.turn)
        king_pos = self.board.find_king(self.turn)
        in_check = False
        if king_pos:
            in_check = self.is_under_attack(king_pos, "white" if self.turn == "black" else "black")
        if not avail and not in_check:
            return True
        return False