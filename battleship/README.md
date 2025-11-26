# Battleship CLI

Play a classic player-vs-computer Battleship match in the terminal.

## Requirements

- Python 3.10+

## Run

```bash
python3 battleship.py
```

Enter coordinates such as `A4` to fire. Hits are marked `X`, misses `O`. Your
own board shows incoming fire from the AI. First to sink all ships wins.

## Game setup

- Board: 6x6 grid (`A-F`, `1-6`)
- Fleet: `3`, `3`, and `2`-length ships
- Ships are placed randomly without overlap.
- Computer fires randomly but never repeats the same spot.

Feel free to tweak `BOARD_SIZE` or `SHIP_LENGTHS` to experiment with difficulty.

