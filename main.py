import os
import tkinter as tk

GRID_SIZE = 4 
CELL_SIZE = 100 
PLAYER_START_X = 0
PLAYER_START_Y = 0


def draw_grid(canvas, rows, cols):
    for i in range(rows + 1):
        canvas.create_line(0, i * CELL_SIZE, cols * CELL_SIZE, i * CELL_SIZE)
    for j in range(cols + 1):
        canvas.create_line(j * CELL_SIZE, 0, j * CELL_SIZE, rows * CELL_SIZE)

def update_message(new_message):
    message_box.config(state=tk.NORMAL)  
    message_box.delete("1.0", tk.END) 
    message_box.insert(tk.END, new_message) 
    message_box.config(state=tk.DISABLED) 

def move_player(event):
    global player_x, player_y

    if event.keysym == "Up" and player_y > 0:
        canvas.move(player, 0, -CELL_SIZE)
        player_y -= 1
    elif event.keysym == "Down" and player_y < GRID_SIZE - 1:
        canvas.move(player, 0, CELL_SIZE)
        player_y += 1
    elif event.keysym == "Left" and player_x > 0:
        canvas.move(player, -CELL_SIZE, 0)
        player_x -= 1
    elif event.keysym == "Right" and player_x < GRID_SIZE - 1:
        canvas.move(player, CELL_SIZE, 0)
        player_x += 1

    update_message(f"You moved to position ({player_x}, {player_y}).")


root = tk.Tk()
root.title("Spongebob: Grid Explorer")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

canvas = tk.Canvas(frame, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE, bg="white")
canvas.grid(row=0, column=0, padx=5, pady=5)


player_img = tk.PhotoImage(file="spongebob.png")
player_x = PLAYER_START_X
player_y = PLAYER_START_Y


player = canvas.create_image(player_x * CELL_SIZE + CELL_SIZE // 2, 
                             player_y * CELL_SIZE + CELL_SIZE // 2, 
                             image=player_img)

message_box = tk.Text(frame, width=30, height=10, wrap=tk.WORD, state=tk.DISABLED)
message_box.grid(row=0, column=1, padx=5, pady=5)

draw_grid(canvas, GRID_SIZE, GRID_SIZE)

update_message("Welcome! Move around and explore.")

root.bind("<Up>", move_player)
root.bind("<Down>", move_player)
root.bind("<Left>", move_player)
root.bind("<Right>", move_player)


root.mainloop()
