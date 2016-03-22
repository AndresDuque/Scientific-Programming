
def eliminaVocales(palabra):
	vocales ="aeiouAEIOU"
	sin_vocales=""
	for i in palabra:
		if i not in vocales:
			sin_vocales+=i
	return sin_vocales

if __name__ =="__main__":
	
	listp = "Programacion tecnica y cientifica"
	l1=eliminaVocales(listp)
	print l1
