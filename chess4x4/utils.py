from typing import Tuple

Position = Tuple[int, int]


def pos_in_bounds(position: Position) -> bool:
    """Return True if position is within 4x4 board (0..3, 0..3)."""
    if not (isinstance(position, tuple) and len(position) == 2):
        return False
    r, c = position
    return isinstance(r, int) and isinstance(c, int) and 0 <= r < 4 and 0 <= c < 4


def validate_pos(position: Position) -> None:
    """Raise ValueError if position is invalid."""
    if not pos_in_bounds(position):
        raise ValueError(f"Invalid board position: {position}. Must be tuple (row,col) with 0..3.)")