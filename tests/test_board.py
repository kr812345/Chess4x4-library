import pytest
from chess4x4.board import Board
from chess4x4.pieces import King, Rook


def test_place_and_move_piece():
    b = Board()
    k = King('white')
    b.place_piece(k, (1, 1))
    assert not b.is_empty((1, 1))
    b.move_piece((1, 1), (2, 2))
    assert b.get_piece((2, 2)) is k
    assert b.is_empty((1, 1))


def test_place_on_occupied_raises():
    b = Board()
    b.place_piece(King('white'), (0, 0))
    with pytest.raises(ValueError):
        b.place_piece(Rook('black'), (0, 0))


def test_move_from_empty_raises():
    b = Board()
    with pytest.raises(ValueError):
        b.move_piece((0, 0), (0, 1))
