#!/usr/bin/env python3
"""
Tkinter-powered GUI wrapper around the Tic-Tac-Toe logic.
"""
from __future__ import annotations

import tkinter as tk
from tkinter import messagebox

from core import Board, check_winner, create_board, next_player


class TicTacToeApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Tic-Tac-Toe")
        self.resizable(False, False)

        self.board: Board = create_board()
        self.current_player: str = "X"
        self.buttons: list[tk.Button] = []
        self.status_var = tk.StringVar(value="Player X's turn")

        self._build_ui()

    def _build_ui(self) -> None:
        frame = tk.Frame(self, padx=10, pady=10)
        frame.grid(row=0, column=0)

        for idx in range(9):
            btn = tk.Button(
                frame,
                text="",
                width=6,
                height=3,
                font=("Helvetica", 20, "bold"),
                command=lambda i=idx: self.handle_click(i),
            )
            btn.grid(row=idx // 3, column=idx % 3, padx=5, pady=5)
            self.buttons.append(btn)

        status_label = tk.Label(self, textvariable=self.status_var, pady=5)
        status_label.grid(row=1, column=0, sticky="ew")

        reset_btn = tk.Button(self, text="Reset game", command=self.reset_game)
        reset_btn.grid(row=2, column=0, pady=(0, 10))

    def handle_click(self, index: int) -> None:
        if self.board[index] or check_winner(self.board):
            return

        self.board[index] = self.current_player
        self.buttons[index].config(text=self.current_player)

        winner = check_winner(self.board)
        if winner:
            self.status_var.set(f"Player {winner} wins!")
            messagebox.showinfo("Game over", f"Player {winner} wins!")
            self._disable_buttons()
            return

        if all(self.board):
            self.status_var.set("It's a draw!")
            messagebox.showinfo("Game over", "It's a draw!")
            self._disable_buttons()
            return

        self.current_player = next_player(self.current_player)
        self.status_var.set(f"Player {self.current_player}'s turn")

    def _disable_buttons(self) -> None:
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)

    def reset_game(self) -> None:
        self.board = create_board()
        self.current_player = "X"
        self.status_var.set("Player X's turn")
        for btn in self.buttons:
            btn.config(text="", state=tk.NORMAL)


def main() -> None:
    app = TicTacToeApp()
    app.mainloop()


if __name__ == "__main__":
    main()

