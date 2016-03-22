def palindromo(palabra):
	if len(palabra) < 2:
		return True
	if palabra[0] != palabra[-1]:
		return False
	return palindromo(palabra[1:-1])


if __name__=="__main__":
	prueba = "coma comida adimoc amoc"
	print palindromo(prueba)
