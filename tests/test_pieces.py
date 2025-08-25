from chess4x4.board import Board
from chess4x4.pieces import King, Rook


def test_king_center_moves():
    b = Board()
    k = King('white')
    b.place_piece(k, (1, 1))
    moves = k.get_moves(b, (1, 1))
    assert (0, 0) in moves
    assert (0, 1) in moves
    assert (2, 2) in moves


def test_king_edge_moves():
    b = Board()
    k = King('white')
    b.place_piece(k, (0, 0))
    moves = k.get_moves(b, (0, 0))
    assert (0, 1) in moves
    assert (1, 0) in moves
    assert (1, 1) in moves


def test_rook_row_moves():
    b = Board()
    r = Rook('white')
    b.place_piece(r, (2, 0))
    moves = r.get_moves(b, (2, 0))
    assert (2, 1) in moves
    assert (2, 2) in moves
    assert (2, 3) in moves


def test_rook_blocked_by_piece():
    b = Board()
    r = Rook('white')
    blocker = King('white')
    b.place_piece(r, (1, 1))
    b.place_piece(blocker, (1, 2))
    moves = r.get_moves(b, (1, 1))
    assert (1, 2) not in moves
    assert (1, 0) in moves
