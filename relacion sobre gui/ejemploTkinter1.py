from Tkinter import *

def botonPulsado():
	global raiz
	raiz.destroy()
	
def main():
	global raiz
	root=Tk()
	root.geometry("200x100")
	etiqueta=Label(root,text="Hola mundo")
	etiqueta.grid(row=0,column=0)
	boton=Button(root,text="Salir",command=botonPulsado)
	boton.grid(row=0,column=1)
	
	raiz=root
	
	root.mainloop()
	
main()
