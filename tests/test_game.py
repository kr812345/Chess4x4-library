# tests/test_game.py
from chess4x4 import Chess4x4

def test_draw_condition():
    game = Chess4x4()
    game.setup((3, 0), (2, 0), (0, 3))
    # Remove rook to force 2 kings only
    game.board.remove_piece(game.wr)
    assert game.is_draw() == True

