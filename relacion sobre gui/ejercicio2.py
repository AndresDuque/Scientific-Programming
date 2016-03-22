"""Construye un visualizador de imagenes."""


from Tkinter import *
import tkFileDialog
from PIL import ImageTk, Image

root = Tk(className="Image viewer")

canvas_width = 800
canvas_height = 600
root.config(bg="black")

img=None

## Imagenes JPEG tambien

def openimage():
    picfile = tkFileDialog.askopenfilename()
    if picfile:
        canvas.img = ImageTk.PhotoImage(file=picfile)
        canvas.create_image(0,0, anchor=NW, image=canvas.img) 
        canvas.configure(canvas, scrollregion=(0,0,canvas.img.width(),canvas.img.height()))

yscrollbar = Scrollbar(root)
yscrollbar.pack(side=RIGHT, fill=Y)

xscrollbar = Scrollbar(root, orient=HORIZONTAL)
xscrollbar.pack(side=BOTTOM, fill=X)

canvas = Canvas(root, width=canvas_width, height=canvas_height, yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)
button = Button(root,text="Abrir imagen",command=openimage)
button.pack(side=BOTTOM)
canvas.pack(side=TOP)
yscrollbar.config(command=canvas.yview)
xscrollbar.config(command=canvas.xview)

mainloop()
