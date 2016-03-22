
def inicioFinVocal(palabra):
	vocales = "aeiouAEIOU"
	principio=palabra[0]
	final =palabra[-1]
	if principio and final in vocales:
		return True
	else:
		return False


if __name__=="__main__":
	
	prueba = "abajo"
	pr = "coma"
	pru= "sobreescribir"
	
	print inicioFinVocal(prueba)
	print inicioFinVocal(pr)
	print inicioFinVocal(pru)
