import tkinter as tk


CELL = 20
COLS = 20
ROWS = 20


# Creating Window
win = tk.Tk()



canvas = tk.Canvas(win, width=COLS*CELL, height=ROWS*CELL)
canvas.pack(expand=True)


for r in range(ROWS + 1):
    canvas.create_line(0, r*CELL, COLS*CELL, r*CELL)

for c in range(COLS + 1):
    canvas.create_line(c*CELL, 0 ,c*CELL, ROWS*CELL)

win.mainloop()


