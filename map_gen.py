import tkinter as tk
import random as r


CELL = 20
COLS = 40
ROWS = 40
whitespace = 2


def placeWalker():
    random_row = r.randint(0, ROWS - whitespace)
    random_col = r.randint(0, COLS -whitespace)
    
    return(random_col, random_row)

def create_grid(random_cell): 
    lable = tk.Label(win, text=f"{random_cell}", font=("Arial", 16))
    lable.pack()
    canvas = tk.Canvas(win, width=COLS*CELL, height=ROWS*CELL)
    canvas.pack(expand=True)

    for row in range(ROWS + 1):
        canvas.create_line(0, row*CELL, COLS*CELL, row*CELL)

    for col in range(COLS + 1):
        canvas.create_line(col*CELL, 0 ,col*CELL, ROWS*CELL)


win = tk.Tk()

random_cell = placeWalker()

create_grid(random_cell)
win.mainloop()





