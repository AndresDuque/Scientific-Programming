"""
Construye un interfaz de usuario que represente una imagen y permita jugar al n-puzzle con
esa imagen.
"""

from Tkinter import *
import sys

root = Tk()
root.title("15-PUZZLE")

frame = Frame(root)
frame["height"]=100
frame["width"]=100
frame["borderwidth"]=4
frame["relief"]=RAISED
frame.grid(row=0,column=0,sticky=E+W+N+S)

frame2 = Frame(root)
frame2["height"]=10
frame2["width"]=80
frame2["borderwidth"]=4
frame2["relief"]=RAISED
frame2.grid(row=1,column=0,sticky=E+W+N+S)



names=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]

n=0
for i in range (4):
    for j in range(4):
        if n!=15:
         item=Button(frame,text=names[n])
         item.grid(row=i,column=j,sticky=E+W+N+S)
         n=n+1

quit = Button(root,text="HECHO")
quit.grid(row=2,column=0,sticky=E+W+N+S)
scramble = Button(root,text="MEZCLAR")
scramble.grid(row=3,column=0,sticky=E+W+N+S)


root.mainloop()
