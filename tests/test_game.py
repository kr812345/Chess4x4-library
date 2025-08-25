import pytest
from chess4x4.game import Chess4x4
from chess4x4.pieces import King, Rook


def test_available_moves_and_move():
    g = Chess4x4()
    g.setup_custom([
        (King('white'), (3, 3)),
        (Rook('white'), (3, 0)),
        (King('black'), (0, 0)),
    ])
    moves = g.available_moves('white')
    assert len(moves) > 0
    # make a legal move
    start, end = moves[0]
    g.move(start, end)


def test_illegal_move_raises():
    g = Chess4x4()
    g.setup_custom([
        (King('white'), (3, 3)),
        (King('black'), (0, 0)),
    ])
    # attempt black to move on white's turn
    with pytest.raises(ValueError):
        g.move((0, 0), (1, 0))


def test_checkmate_detection():
    g = Chess4x4()
    # Simple checkmate setup:
    # black king at (0,0)
    # white rook at (0,2) attacking row
    # white king at (1,1) cutting escape squares
    g.setup_custom([
        (King('black'), (0, 0)),
        (Rook('white'), (0, 2)),
        (King('white'), (1, 1)),
    ])
    assert g.is_checkmate('black') is True


def test_draw_only_kings():
    g = Chess4x4()
    g.setup_custom([
        (King('white'), (3, 3)),
        (King('black'), (0, 0)),
    ])
    assert g.is_draw() is True
