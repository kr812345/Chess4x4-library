````markdown
# Chess4x4

A **4x4 Chess Library** written in Python.  
Currently supports the classic endgame scenario **White King + Rook vs Black King** on a 4x4 chessboard.  

---

## ✨ Features
- 4x4 chessboard
- Custom starting positions
- Supports **King** and **Rook**
- Generate all possible moves
- Make legal moves
- Detect **win** (capturing opponent King)
- Detect **draw** (only two Kings left)
- Turn-based play (White starts)

---

## 📦 Installation

```bash
pip install chess4x4
````

---

## 🚀 Quick Start

```python
from chess4x4 import Chess4x4, King, Rook

# Initialize game
game = Chess4x4()

# Print the board
print(game.board)

# Generate moves for White King
moves = game.board.get_piece_moves((0, 0))
print("White King moves:", moves)

# Make a move
game.make_move((0, 0), (1, 0))

# Check status
print("Game over:", game.is_game_over())
```

---

## 📖 API Documentation

### Classes

#### `Chess4x4`

* `make_move(start: tuple[int, int], end: tuple[int, int]) -> bool`
  Make a move if legal. Returns `True` if successful.
* `is_game_over() -> bool`
  Returns `True` if the game has ended.
* `winner() -> str | None`
  Returns `"White"`, `"Black"`, or `None`.

#### `Board`

* `get_piece_moves(position: tuple[int, int]) -> list[tuple[int, int]]`
  Generate all legal moves for a piece.
* `move_piece(start, end) -> bool`
  Move a piece if valid.

#### Pieces

* `King(color: str, position: tuple[int, int])`
* `Rook(color: str, position: tuple[int, int])`

---

## 🧪 Testing

Run tests with:

```bash
pytest tests/
```

---

## 🤝 Contributing

We welcome contributions!

1. Fork the repo
2. Create a new branch

   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes

   ```bash
   git commit -m "Added feature X"
   ```
4. Push to your branch

   ```bash
   git push origin feature-name
   ```
5. Create a Pull Request 🎉

Please make sure:

* Code is well-documented
* All tests pass
* Follow the existing coding style

---

## 📜 License

This project is licensed under the MIT License.

