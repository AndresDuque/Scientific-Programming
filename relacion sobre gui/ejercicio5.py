"""
Construye un interfaz de usuario que permita dibujar lineas rectas en una ventana.
"""

from Tkinter import Tk, Canvas

start = None

def onclick_handler(event):
    global start
    start = (event.x, event.y)

def onrelease_handler(event):
    global start
    if start is not None:
        x = start[0]
        y = start[1]
        event.widget.create_line(x, y, event.x, event.y)
        start = None

master = Tk()
canvas = Canvas(master, width=200, height=200)
canvas.bind("<Button-1>", onclick_handler)
canvas.bind("<ButtonRelease-1>", onrelease_handler)
canvas.pack()
master.mainloop()

