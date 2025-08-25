from typing import Optional, List, Tuple
from .utils import validate_pos
from .pieces import Piece

Position = Tuple[int, int]


class Board:
    def __init__(self):
        # 4x4 board: rows 0..3, cols 0..3
        self.grid: List[List[Optional[Piece]]] = [[None for _ in range(4)] for _ in range(4)]

    def place_piece(self, piece: Piece, position: Position) -> None:
        validate_pos(position)
        r, c = position
        if self.grid[r][c] is not None:
            raise ValueError(f"Square {position} is already occupied")
        self.grid[r][c] = piece

    def move_piece(self, start: Position, end: Position) -> None:
        validate_pos(start)
        validate_pos(end)
        sr, sc = start
        er, ec = end
        piece = self.grid[sr][sc]
        if piece is None:
            raise ValueError(f"No piece at start position {start}")
        # allow capture
        if start == end:
            raise ValueError("Start and end positions are the same")
        self.grid[er][ec] = piece
        self.grid[sr][sc] = None

    def is_empty(self, position: Position) -> bool:
        validate_pos(position)
        r, c = position
        return self.grid[r][c] is None

    def get_piece(self, position: Position):
        validate_pos(position)
        r, c = position
        return self.grid[r][c]

    def find_king(self, color: str):
        for r in range(4):
            for c in range(4):
                p = self.grid[r][c]
                if p is not None and getattr(p, "symbol", None) == "K" and p.color == color:
                    return (r, c)
        return None

    def print_board(self) -> None:
        # ASCII print: top row is row 0
        print("+----+----+----+----+")
        for r in range(4):
            row_repr = ""
            for c in range(4):
                p = self.grid[r][c]
                if p is None:
                    cell = "    "
                else:
                    cell = f" {p.symbol}{p.color[0].upper()} "
                row_repr += f"|{cell}"
            row_repr += "|"
            print(row_repr)
            print("+----+----+----+----+")