# Cursor Tic-Tac-Toe

Tic-Tac-Toe for two players with both terminal and desktop (Tkinter) launchers.

## Requirements

- Python 3.10 or newer (Tkinter ships with the standard macOS build)

## Launch options

### Text mode

```bash
python3 tic_tac_toe.py
```

You will be prompted for board positions `1-9` until someone wins or the board fills.

### Windowed mode

```bash
python3 gui_app.py
```

This opens a small window where you click squares, much like Minesweeper/Saper.
On macOS you can also double-click `gui_app.py` in Finder if `.py` files are
associated with Python Launcher.

## Project Structure

- `core.py` – shared helper functions (board state, winner detection)
- `tic_tac_toe.py` – classic CLI loop
- `gui_app.py` – Tkinter-based desktop window

## Contributing

Feel free to fork the repo and submit pull requests.

