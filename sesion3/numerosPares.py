import time

L=[20,5,3,3,657,23,7,-2,-60,5]

def numerosPares(numeros):
	res = []
	cont=0
	for i in numeros:
		if i%2==0:
			res.append(i)
			cont+=1
	return cont, res

if __name__=="__main__":
	Contador, List = numerosPares(L)
	print Contador, List
