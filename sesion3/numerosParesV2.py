import time

L=[20,5,3,3,657,23,7,-2,-60,5]

def numerosPares_v2(numeros):
	res = []
	Suma = 0
	pos = 0
	for i in numeros:
		if i%2==0:
			Suma+=i
			res.append(i)
	return Suma, res

if __name__=="__main__":
	Suma, List = numerosPares_v2(L)
	print Suma, List
