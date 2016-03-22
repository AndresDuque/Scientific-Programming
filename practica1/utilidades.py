import unicodedata
import string
import re, collections
import os
from collections import OrderedDict

#
# Frecuencias relativas al ingles. 
# La primera frecuencia es la A y asi sucesivamente.
#
INGLES = (0.0749, 0.0129, 0.0354, 0.0362, 0.1400, 0.0218, 0.0174, 0.0422, 0.0665, 0.0027, 0.0047, 0.0357, 
           0.0339, 0.0674, 0.0737, 0.0243, 0.0026, 0.0614, 0.0695, 0.0985, 0.0300, 0.0116, 0.0169, 0.0028, 
           0.0164, 0.0004)
ESP = (0.1253,0.0142,0.0468,0.0586,0.1368,0.0069,0.0101,0.007,0.0625,0.0044,0.0001,0.0497,0.0315,0.0671,0.0031,
		0.0868,0.0251,0.0088,0.0687,0.0798,0.0463,0.0393,0.009,0.0002,0.0022,0.009,0.0052)
		
FRECUENCIAS = (INGLES,ESP)



def QuitarPuntuacionYMayus(text):
	""" Lo he hecho en una sola funcion"""
	result=(unicode).join((c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c)!='Mn'))
	res=result.lower()
	return res


def delta(fuente,destino):
	N=0.0
	for f1,f2 in zip(fuente,destino):
		N+= abs(f1-f2)
	return N

def frecuencia(s):
	D = dict([(c,0) for c in string.lowercase])
	N=0.0
	for c in s:
		if 'a'<=c<='z':
			N+=1
			D[c]+=1
	L = D.items()
	L.sort()
	return [f/N for (l,f) in L]

def QuitaEspacios(text):
	res=[]
	for i in text:
		if i!=' ':
			res.append(i)
	texto=""
	for i in res:
		texto+=i
	return texto

def QuitaLetrasRepetidas(texto):
	dev= "".join(OrderedDict.fromkeys(texto))
	return dev

def Transformar_alfabeto(texto,clave,n):
	alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	clave1=[]
	clave=QuitaEspacios(clave)
	for i in clave:
		clave1.append(i)
	
	clave1.extend(alfabeto)
	clave_txt=""
	for i in clave1:
		clave_txt+=i
	clave2=QuitaLetrasRepetidas(clave_txt)
	alfabeto_transformado=[]
	for i in clave2:
		alfabeto_transformado.append(i)

	alfabeto2=alfabeto_transformado[-n::]
	alfabeto2.extend(alfabeto_transformado)
	alfabeto_txt=""
	for i in alfabeto2:
		alfabeto_txt+=i
	
	alfabeto_tr=QuitaLetrasRepetidas(alfabeto_txt)
	alfabeto_final=[]
	for i in alfabeto_tr:
		alfabeto_final.append(i)
	
	return alfabeto_final


if __name__=="__main__":
	palabra="Cabezon ReCorChoLis"
	f=open('big.txt', 'r')
	palabras = f.readline()
	for line in palabras:
		print (line)
	l= "vamosquenosvamos"
	r=QuitaLetrasRepetidas(l)
	print (r)
