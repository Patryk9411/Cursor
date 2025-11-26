# Battleship (Ships) CLI

Simple text-based Battleship game where you face an AI opponent.

## Requirements

- Python 3.10+ (standard library only)

## How to play

```bash
python3 battleship.py
```

- Enter coordinates like `B4` to fire at the computer's grid.
- `X` marks hits, `O` marks misses. Your own board always shows where the
  computer has fired.
- Sink all enemy ships before yours are destroyed to win.

## Rules implemented

- Board size: 6x6.
- Fleet: two ships of length 3, one ship of length 2.
- Ships are placed randomly without touching constraints.
- Computer picks random shots but never repeats a coordinate.

Feel free to modify `SHIP_LENGTHS` or `BOARD_SIZE` in `battleship.py` to create
custom difficulties.

