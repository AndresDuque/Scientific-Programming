def ordenAlfabetico(palabra):
	aux=palabra[1]
	for i in palabra:
		for j in aux:
			if chr(ord(i))< chr(ord(j)):
				return True
			else:
				return False

if __name__=="__main__":
	prueba = "abejo"
	prueba2 ="abcde"
	print ordenAlfabetico(prueba)
	print ordenAlfabetico(prueba2)
