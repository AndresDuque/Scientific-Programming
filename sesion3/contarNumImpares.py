import time

L = [-12,8,5,6,4,1,3,7,9,8]

def contarNumImpares(numeros):
	res = []
	cont=0
	for i in numeros:
		if i%2!=0:
			res.append(i)
			cont+=1
	return cont, res

if __name__=="__main__":
	contador, List = contarNumImpares(L)
	print contador, List
