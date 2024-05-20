import numpy as np
import tkinter as tk
from tkinter import messagebox

class ConnectFour:
    ROW_COUNT = 6
    COLUMN_COUNT = 7
    PLAYER_ONE = 1
    PLAYER_TWO = 2
    EMPTY = 0

    def __init__(self):
        self.board = self.create_board()
        self.game_over = False
        self.turn = ConnectFour.PLAYER_ONE

    def create_board(self):
        return np.zeros((ConnectFour.ROW_COUNT, ConnectFour.COLUMN_COUNT))

    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece

    def is_valid_location(self, col):
        return self.board[ConnectFour.ROW_COUNT - 1][col] == ConnectFour.EMPTY

    def get_next_open_row(self, col):
        for r in range(ConnectFour.ROW_COUNT):
            if self.board[r][col] == ConnectFour.EMPTY:
                return r
        return None

    def winning_move(self, piece):
        # Check horizontal locations
        for c in range(ConnectFour.COLUMN_COUNT - 3):
            for r in range(ConnectFour.ROW_COUNT):
                if self.board[r][c] == piece and self.board[r][c + 1] == piece and self.board[r][c + 2] == piece and self.board[r][c + 3] == piece:
                    return True

        # Check vertical locations
        for c in range(ConnectFour.COLUMN_COUNT):
            for r in range(ConnectFour.ROW_COUNT - 3):
                if self.board[r][c] == piece and self.board[r + 1][c] == piece and self.board[r + 2][c] == piece and self.board[r + 3][c] == piece:
                    return True

        # Check positively sloped diagonals
        for c in range(ConnectFour.COLUMN_COUNT - 3):
            for r in range(ConnectFour.ROW_COUNT - 3):
                if self.board[r][c] == piece and self.board[r + 1][c + 1] == piece and self.board[r + 2][c + 2] == piece and self.board[r + 3][c + 3] == piece:
                    return True

        # Check negatively sloped diagonals
        for c in range(ConnectFour.COLUMN_COUNT - 3):
            for r in range(3, ConnectFour.ROW_COUNT):
                if self.board[r][c] == piece and self.board[r - 1][c + 1] == piece and self.board[r - 2][c + 2] == piece and self.board[r - 3][c + 3] == piece:
                    return True
        return False

class ConnectFourGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four")
        self.player_one_points = 0
        self.player_two_points = 0
        self.create_menu()
        self.init_game()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Game", command=self.init_game)
        file_menu.add_command(label="Restart Game", command=self.restart_game)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        self.points_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Points", menu=self.points_menu)
        self.points_menu.add_command(label="Show Points", command=self.show_points)

    def init_game(self):
        self.game = ConnectFour()
        if hasattr(self, 'canvas'):
            self.canvas.delete("all")
        else:
            self.canvas = tk.Canvas(self.root, width=700, height=600, bg='blue')
            self.canvas.pack()

        self.canvas.bind("<Button-1>", self.handle_click)
        self.draw_board()

    def restart_game(self):
        self.init_game()
        self.player_one_points = 0
        self.player_two_points = 0

    def draw_board(self):
        for r in range(ConnectFour.ROW_COUNT):
            for c in range(ConnectFour.COLUMN_COUNT):
                x_start = c * 100
                y_start = r * 100 + 100
                self.canvas.create_oval(x_start + 5, y_start + 5, x_start + 95, y_start + 95, fill='white')

    def handle_click(self, event):
        if self.game.game_over:
            return

        col = event.x // 100
        if self.game.is_valid_location(col):
            row = self.game.get_next_open_row(col)
            self.animate_drop(row, col, self.game.turn)

    def animate_drop(self, row, col, piece):
        x_start = col * 100
        y_start = 0
        y_end = (ConnectFour.ROW_COUNT - row - 1) * 100
        color = 'red' if piece == ConnectFour.PLAYER_ONE else 'yellow'

        disk = self.canvas.create_oval(x_start + 5, y_start + 5, x_start + 95, y_start + 95, fill=color)

        def drop():
            nonlocal y_start
            if y_start < y_end:
                y_start += 20
                self.canvas.move(disk, 0, 20)
                self.root.after(10, drop)
            else:
                self.game.drop_piece(row, col, piece)
                if self.game.winning_move(piece):
                    self.game.game_over = True
                    messagebox.showinfo("Connect Four", f"Player {piece} wins!")
                    if piece == ConnectFour.PLAYER_ONE:
                        self.player_one_points += 1
                    else:
                        self.player_two_points += 1
                    self.show_points()
                else:
                    self.game.turn = ConnectFour.PLAYER_TWO if self.game.turn == ConnectFour.PLAYER_ONE else ConnectFour.PLAYER_ONE

        drop()

    def show_points(self):
        messagebox.showinfo("Points", f"Player One: {self.player_one_points}\nPlayer Two: {self.player_two_points}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = ConnectFourGUI(root)
    root.mainloop()
