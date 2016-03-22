## 1. sumNumlista(numeros)
## a- range b- sin range
## medir tiempos
## 2.contarNumerosImpares(numeros), que se cuente el numero de impares que hay
## 3. NumerosPares(numeros), devuelve una lista
import time

num = (7,)*10000000

def sumNumLista(numeros):
	suma = 0
	for i in numeros:
		suma +=i
	return suma


def sumNumLista2(numeros):
	suma = 0
	for i in range(len(numeros)):
		suma+=numeros[i]
	return suma
	
if __name__=="__main__":

	Ti = time.time()
	sumNumLista(num)
	Tf = time.time()
	print("Suma lista sin range ")
	print("%.3f" % (Tf-Ti))

	T= time.time()
	sumNumLista2(num)
	F=time.time()
	print ("Suma lista con range")
	print("%.3f" %(Tf-Ti))

