#!/usr/bin/env python3
"""
Simple two-player Tic-Tac-Toe game for the terminal.
"""

from __future__ import annotations

import itertools

from core import Board, check_winner, create_board, is_draw


def print_board(board: Board) -> None:
    """Render the board with positions for empty slots."""
    cells = [cell if cell else str(idx + 1) for idx, cell in enumerate(board)]
    rows = [cells[i : i + 3] for i in range(0, 9, 3)]
    print("\nCurrent board:")
    for row in rows:
        print(" | ".join(row))
        if row is not rows[-1]:
            print("--+---+--")
    print()


def read_move(player: str, board: Board) -> int:
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
    board = create_board()
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

        if is_draw(board):
            print_board(board)
            print("It's a draw! Well played both.")
            break


if __name__ == "__main__":
    play_game()

