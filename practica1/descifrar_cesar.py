import utilidades
import string
import random


def cifrar_cesar(texto,desplazamiento):
	
	alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	
	dic={}
	for i in range(0,len(alfabeto)):
		dic[alfabeto[i]]=alfabeto[(i+desplazamiento)%len(alfabeto)]
		
	txt_cfr=""
	for l in texto.lower():
		if l in dic:
			l=dic[l]
		txt_cfr+=l
	return txt_cfr
	

def descifrar_cesar(s):
	deltamin=1000
	bestrot=0
	freq=utilidades.frecuencia(s)
	for clave in range(26):
		d = min([utilidades.delta(freq[clave:]+freq[:clave],x) for x in utilidades.FRECUENCIAS])
		if d<deltamin:
			deltamin=d
			bestrot=clave
	return cifrar_cesar(s,-bestrot)


""" Texto cifrado en cifrar_cesar.py"""

texto1=""" vsfivxs """
texto2 = """ nkrru cuxrj se tgsk oy gtjxky """

if __name__=="__main__":
	
	""" Se compila con python descifrar_cesar.py 
	Con python3, me da error en string.lowercase() en utilidades.py"""
	
	for text in (texto1,texto2):
		print ("Texto cifrado")
		print (texto1)
		print (texto2)
		
		print ("A continuacion texto descifrado")
		X =descifrar_cesar(text)
		print (X)
