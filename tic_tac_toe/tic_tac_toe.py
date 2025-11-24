#!/usr/bin/env python3
"""
Simple two-player Tic-Tac-Toe game for the terminal.
"""

from __future__ import annotations

import itertools


def print_board(board: list[str | None]) -> None:
    """Render the board with positions for empty slots."""
    cells = [cell if cell else str(idx + 1) for idx, cell in enumerate(board)]
    rows = [cells[i : i + 3] for i in range(0, 9, 3)]
    print("\nCurrent board:")
    for row in rows:
        print(" | ".join(row))
        if row is not rows[-1]:
            print("--+---+--")
    print()


def check_winner(board: list[str | None]) -> str | None:
    """Return the winning symbol if someone won; otherwise None."""
    winning_lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    for a, b, c in winning_lines:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None


def read_move(player: str, board: list[str | None]) -> int:
    """Prompt the player until a valid move is provided."""
    while True:
        raw = input(f"Player {player}, choose a square (1-9): ").strip()
        if not raw.isdigit():
            print("Please enter a number between 1 and 9.")
            continue
        position = int(raw) - 1
        if position not in range(9):
            print("That square is outside the board. Try again.")
            continue
        if board[position]:
            print("That square is already taken. Choose another one.")
            continue
        return position


def play_game() -> None:
    """Run a single Tic-Tac-Toe match between two human players."""
    board: list[str | None] = [None] * 9
    print("Welcome to Tic-Tac-Toe! Player X goes first.\n")

    for player in itertools.cycle(("X", "O")):
        print_board(board)
        move = read_move(player, board)
        board[move] = player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins! Thanks for playing.")
            break

        if all(board):
            print_board(board)
            print("It's a draw! Well played both.")
            break


if __name__ == "__main__":
    play_game()

