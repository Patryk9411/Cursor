"""
Shared Tic-Tac-Toe helpers for both CLI and GUI frontends.
"""
from __future__ import annotations

from typing import List, Optional

Board = List[Optional[str]]

WINNING_LINES: tuple[tuple[int, int, int], ...] = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def create_board() -> Board:
    return [None] * 9


def check_winner(board: Board) -> Optional[str]:
    for a, b, c in WINNING_LINES:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_draw(board: Board) -> bool:
    return all(board) and check_winner(board) is None


def next_player(current: str) -> str:
    return "O" if current == "X" else "X"

