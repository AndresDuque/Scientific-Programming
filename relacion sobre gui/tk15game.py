#! /usr/bin/env python
"""
Fifteenth game
"""
# tested only on windows xp, py vesion 2.6.2

__author__ = "Constantine Klevtsov aka dlx <dlx1989@gmail.com>"
__version__ = '0.1'

from Tkinter import *
import random
import functools
import sys

def get_grid(num):
    info = pieces[num].grid_info()
    return (int(info['row']), int(info['column']))
    
def get_num(row, column):
    if row > 3 or column > 3:
        return 0
    widget = frame.grid_slaves(row=row, column=column)
    return pieces.index(widget[0])


def move(event=None, num=None):    
    row_empty, col_empty = get_grid(0)
    keymap = {'Left': (row_empty, col_empty-1),
              'Right': (row_empty, col_empty+1),
              'Up': (row_empty-1, col_empty),
              'Down': (row_empty+1, col_empty)}
    if event:
        try: num = get_num(*keymap[event.keysym])
        except TclError: return
    
    row, col = get_grid(num)
    
    if abs(row-row_empty) + abs(col-col_empty) == 1:  
            pieces[num].grid(row=row_empty, column=col_empty)
            empty.grid(row=row, column=col)

def create_grid(n):
    for i in range(n):
        for q in range(n):
            yield (i, q)
            
def new(event=None):
    grid = [i for i in create_grid(4)]
    random.shuffle(grid)
    for (row, column), piece in zip(grid, pieces):
        piece.grid(row=row, column=column, padx=4, pady=4)
    return grid
    
root = Tk()
root.title("15")
root.bind("<KeyPress>", move)
root.bind("q", sys.exit)
root.bind("n", new)

frame = Frame(root, bg='black')
frame.pack()

def PieceButton(i):
    return Button(
        frame, 
        text=str(i), 
        width=3,
        borderwidth=5,
        relief=RIDGE,
        font='Arial 20 bold',
        command=functools.partial(move, num=i)
        )

pieces = map(PieceButton, range(16))
empty = pieces[0] = Label(frame, bg='black')
grid = new()

root.mainloop()