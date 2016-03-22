"""
Construye un interfaz de usuario con una entrada de una cadena, un recuadro de texto y un
boton. Debe permitir escribir un texto en el recuadro de texto, introducir el nombre de un
fichero de forma que cuando se pulse el boton se guarde el texto en el fichero indicado.
"""

from Tkinter import *
import tkSimpleDialog
import tkFileDialog

entryBox=None
entryBox2=None

def BotonPulsado():
	global entryBox
	txt=entryBox.get()
	print ("Texto introducido: ",txt)
	nombre_fichero=entryBox2.get()
	fname=tkFileDialog.SaveAs(filetypes=[('File text','*.txt')],initialfile=nombre_fichero,
	title='Save a file').show()
	if fname:
		f=open(fname,'w')
		f.write(txt)
		f.close()
#boton cerrar
def botonCerrar():
	global raiz
	raiz.destroy()
	
#Caja para introducir el texto a guardar en el fichero
def crearCajaTexto(parent):
	global entryBox
	etiqueta=Label(parent,text="Introduce texto")
	entryBox=Entry(parent)
	etiqueta.grid()
	entryBox.grid()

#Caja para introducir el nombre del archivo a guardar
def creaCajaNombre(parent):
	global entryBox2
	etiqueta=Label(parent,text="Nombre del fichero")
	entryBox2=Entry(parent)
	etiqueta.grid()
	entryBox2.grid()

def main():
	global raiz
	root=Tk()
	root.title("Guardar archivo")
	
	root.geometry("300x300")
	
	miBoton=Button(root,text="Guarda texto", command=BotonPulsado)
	miBoton.grid()
	
	crearCajaTexto(root)
	creaCajaNombre(root)
	
	Cerrar=Button(root,text="Cerrar",command=botonCerrar)
	Cerrar.grid(row=15,column=1)
	
	raiz=root
	
	root.mainloop()
	
main()

