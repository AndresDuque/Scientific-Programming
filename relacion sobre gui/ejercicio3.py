"""Construye un visualizador de matrices."""

from Tkinter import *
import random

def RGBs(num):
 # Colores RGB aleatoriso
 return [[random.randint(0,255) for i in range(0,3)] for j in range(0,num)]

def rgb2Hex(rgb_tuple):
    return '#%02x%02x%02x' % tuple(rgb_tuple)

def drawGrid(w,colors):
 col = 0; row = 0
 colors = [rgb2Hex(color) for color in colors]
 for color in colors:
  w.create_rectangle(col, row, col+1, row+1, fill=color, outline=color)
  col+=1
  if col == 100:
   row += 1; col = 0

root = Tk()
w = Canvas(root)
w.grid()
colors = RGBs(5000)
drawGrid(w,colors)
root.mainloop()
