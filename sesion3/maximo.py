import math


L= [5,32,1,6,1,6,423,6,1322,6,1323,41]

def maximo(numeros):
	mayor = 0
	cont = 0
	pos = 1
	for i in numeros:
		mayor = i
		if mayor > cont:
			cont = i
		else:
			mayor = cont
			pos+=1
	return pos, mayor

if __name__=="__main__":
	p, n = maximo(L)

	print p, n
