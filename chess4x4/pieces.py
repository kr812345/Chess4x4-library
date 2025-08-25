from __future__ import annotations
from typing import List, Tuple
from abc import ABC, abstractmethod
from .utils import pos_in_bounds
from .board import Board

Position = Tuple[int, int]


class Piece(ABC):
    def __init__(self, color: str, symbol: str):
        if color not in ("white", "black"):
            raise ValueError("color must be 'white' or 'black'")
        self.color = color
        self.symbol = symbol

    @abstractmethod
    def get_moves(self, board: Board, position: Position) -> List[Position]:
        """Return a list of valid end positions for this piece from `position` on `board`."""
        pass


class King(Piece):
    def __init__(self, color: str):
        super().__init__(color, "K")

    def get_moves(self, board: Board, position: Position) -> List[Position]:
        moves: List[Position] = []
        r, c = position
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if not pos_in_bounds((nr, nc)):
                    continue
                target = board.get_piece((nr, nc))
                # can move to empty or capture opponent
                if target is None or target.color != self.color:
                    moves.append((nr, nc))
        return moves


class Rook(Piece):
    def __init__(self, color: str):
        super().__init__(color, "R")

    def get_moves(self, board: Board, position: Position) -> List[Position]:
        moves: List[Position] = []
        r, c = position
        # four directions
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            while pos_in_bounds((nr, nc)):
                target = board.get_piece((nr, nc))
                if target is None:
                    moves.append((nr, nc))
                else:
                    if target.color != self.color:
                        moves.append((nr, nc))
                    break
                nr += dr
                nc += dc
        return moves