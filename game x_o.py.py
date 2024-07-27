import random
import tkinter as tk
from tkinter import messagebox

def check_win(board, player, computer):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    if [player, player, player] in win_conditions:
        messagebox.showinfo("player win ", " congrtulation player")
        return True
    elif [computer, computer, computer] in win_conditions:
        messagebox.showinfo("computer  win ", " congrtulation computer")
        return True
    elif all(cell != ' ' for row in board for cell in row):
        messagebox.showinfo("tie", "tie")
    return False

def move_player(row, col):
    global current_player, board, buttons
    if board[row][col] == ' ':
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, )
        if check_win(board, player, computer):
            disable_all_buttons()
        else:
            switch_player()
            if current_player == computer:
                move_computer()

def move_computer():
    global board, buttons
    while True:
        row_compu = random.randint(0, 2)
        col_compu = random.randint(0, 2)
        if board[row_compu][col_compu] == ' ':
            board[row_compu][col_compu] = computer
            buttons[row_compu][col_compu].config(text=computer )
            break
    if check_win(board, player, computer):
        disable_all_buttons()
    else:
        switch_player()

def switch_player():
    global current_player, player, computer
    current_player = player if current_player == computer else computer

def disable_all_buttons():
    global buttons
    for row in buttons:
        for button in row:
            button.config(state=tk.DISABLED)

def restart_game():
    global board, buttons, current_player
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = player
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=' ', state=tk.NORMAL)

window = tk.Tk()
window.title("لعبة X & O")
window.geometry("400x450")

player = "X"
computer = "O"
current_player = player

board = [[' ' for _ in range(3)] for _ in range(3)]



buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        button = tk.Button(window, text=' ', font=("Arial", 40), width=5, height=2,
                           command=lambda row=row, col=col: move_player(row, col))
        button.grid(row=row+2, column=col, padx=5, pady=5)
        buttons[row][col] = button
        
        
label_player = tk.Label(window, text="You: 0", font=("Arial", 20))
label_player.grid(pady=10 , row=0, column=0)

label_computer = tk.Label(window, text="Computer: 0", font=("Arial", 20))
label_computer.grid(pady=10 ,row=0, column=2)        

restart_button = tk.Button(window, text="RESTART", font=("Arial", 20), bg="green", command=restart_game)
restart_button.grid(row=1, column=1, pady=10)

window.mainloop()
