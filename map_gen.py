import tkinter as tk
import random as r


CELL = 20
COLS = 40
ROWS = 40
whitespace = 2
percentage = 50

MAP_size = int(((ROWS - whitespace) * (COLS - whitespace)) * (percentage / 100))

possible_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # left, right, up, down

Cell_checker = {}

def placeWalker():
    random_row = r.randint(whitespace, ROWS - whitespace - 1)
    random_col = r.randint(whitespace, COLS - whitespace - 1)
    
    return(random_col, random_row)

def create_grid(random_cell): 
    lable1 = tk.Label(win, text=f"({random_cell[0]+1},{random_cell[1]+1})", font=("Arial", 16))
    lable1.pack()

    lable2 = tk.Label(win, text=f"MAP Size: {MAP_size}", font=("Arial", 16))
    lable2.pack()

    lable3 = tk.Label(win, text=f"Grid Size: {COLS * ROWS}", font=("Arial", 16))
    lable3.pack()

    canvas = tk.Canvas(win, width=COLS*CELL, height=ROWS*CELL)
    canvas.pack(expand=True)

    for row in range(ROWS):
        canvas.create_line(0, row*CELL, COLS*CELL, row*CELL)

        for col in range(COLS + 1):
            canvas.create_line(col*CELL, 0 ,col*CELL, ROWS*CELL)
            if (col, row) == random_cell:
                canvas.create_rectangle(col*CELL, row*CELL, (col+1)*CELL, (row+1)*CELL, fill="red")
                Cell_checker[(col, row)] = "floor"
                walker_move(random_cell, canvas)


def walker_move(random_cell, canvas):
    current_cell = random_cell

    while len(Cell_checker) < MAP_size:
        direction = r.choice(possible_directions)
        new_cell = current_cell[0] + direction[0], current_cell[1] + direction[1]
        if (whitespace <= new_cell[0] < COLS - whitespace) and (whitespace <= new_cell[1] < ROWS - whitespace):
            if new_cell not in Cell_checker:
                canvas.create_rectangle(new_cell[0]*CELL, new_cell[1]*CELL, (new_cell[0]+1)*CELL, (new_cell[1]+1)*CELL, fill="green")
                Cell_checker[new_cell] = "floor"
            current_cell = new_cell
    else:
         return Create_walls(canvas)

def Create_walls(canvas):
    for row in range(ROWS):
        for col in range(COLS):
            if (col, row) not in Cell_checker:
                adjacent_floors = 0
                for direction in possible_directions:
                    adjacent_cell = (col + direction[0], row + direction[1])
                    if adjacent_cell in Cell_checker:
                        adjacent_floors += 1
                if adjacent_floors > 0:
                    canvas.create_rectangle(col*CELL, row*CELL, (col+1)*CELL, (row+1)*CELL, fill="black")
                  

win = tk.Tk()

random_cell = placeWalker()

create_grid(random_cell)

win.mainloop()





