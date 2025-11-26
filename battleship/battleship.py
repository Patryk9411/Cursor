#!/usr/bin/env python3
"""
Command-line Battleship (Ships) game versus the computer.
"""
from __future__ import annotations

import random
import string

BOARD_SIZE = 6
SHIP_LENGTHS = [3, 3, 2]
ROW_LABELS = string.ascii_uppercase[:BOARD_SIZE]


def create_board(fill: str = ".") -> list[list[str]]:
    return [[fill for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def place_ship(board: list[list[str]], length: int) -> None:
    """Place a ship of given length randomly on board without overlap."""
    while True:
        orientation = random.choice(("H", "V"))
        if orientation == "H":
            row = random.randrange(BOARD_SIZE)
            col = random.randrange(BOARD_SIZE - length + 1)
            slots = [(row, col + offset) for offset in range(length)]
        else:
            row = random.randrange(BOARD_SIZE - length + 1)
            col = random.randrange(BOARD_SIZE)
            slots = [(row + offset, col) for offset in range(length)]

        if all(board[r][c] == "." for r, c in slots):
            for r, c in slots:
                board[r][c] = "S"
            return


def place_fleet() -> list[list[str]]:
    board = create_board()
    for length in SHIP_LENGTHS:
        place_ship(board, length)
    return board


def render_board(board: list[list[str]], hide_ships: bool = False) -> str:
    header = "  " + " ".join(str(idx + 1) for idx in range(BOARD_SIZE))
    rows = []
    for idx, row in enumerate(board):
        display_row = []
        for cell in row:
            if hide_ships and cell == "S":
                display_row.append(".")
            else:
                display_row.append(cell)
        rows.append(f"{ROW_LABELS[idx]} " + " ".join(display_row))
    return "\n".join([header, *rows])


def parse_move(raw: str) -> tuple[int, int] | None:
    raw = raw.strip().upper()
    if len(raw) < 2:
        return None
    row_char, col_part = raw[0], raw[1:]
    if row_char not in ROW_LABELS:
        return None
    if not col_part.isdigit():
        return None
    col_num = int(col_part)
    if not (1 <= col_num <= BOARD_SIZE):
        return None
    return ROW_LABELS.index(row_char), col_num - 1


def shoot(board: list[list[str]], row: int, col: int) -> str:
    """Return result string and update board with hit/miss markers."""
    target = board[row][col]
    if target in ("X", "O"):
        return "repeat"
    if target == "S":
        board[row][col] = "X"
        return "hit"
    board[row][col] = "O"
    return "miss"


def all_ships_sunk(board: list[list[str]]) -> bool:
    return not any(cell == "S" for row in board for cell in row)


def computer_move(previous_moves: set[tuple[int, int]]) -> tuple[int, int]:
    while True:
        move = (random.randrange(BOARD_SIZE), random.randrange(BOARD_SIZE))
        if move not in previous_moves:
            previous_moves.add(move)
            return move


def main() -> None:
    print("Welcome to Battleship! Sink the computer's fleet first to win.\n")
    player_board = place_fleet()
    computer_board = place_fleet()
    computer_history: set[tuple[int, int]] = set()

    while True:
        print("Your board:")
        print(render_board(player_board))
        print("\nTarget board:")
        print(render_board(computer_board, hide_ships=True))

        move = None
        while move is None:
            raw = input("\nEnter a target (e.g., A3): ")
            move = parse_move(raw)
            if move is None:
                print("Invalid coordinate. Try again.")
        result = shoot(computer_board, *move)
        if result == "repeat":
            print("You already fired there. Choose again.")
            continue
        print("Hit!" if result == "hit" else "Miss.")

        if all_ships_sunk(computer_board):
            print("\nAll enemy ships sunk. You win!")
            break

        comp_row, comp_col = computer_move(computer_history)
        comp_result = shoot(player_board, comp_row, comp_col)
        coord = f"{ROW_LABELS[comp_row]}{comp_col + 1}"
        if comp_result == "hit":
            print(f"Computer fires at {coord} — hit!")
        else:
            print(f"Computer fires at {coord} — miss.")

        if all_ships_sunk(player_board):
            print("\nYour fleet has been destroyed. Computer wins.")
            break


if __name__ == "__main__":
    main()

