def esInversa(pal1,pal2):
	aux=pal2[::-1]
	for i in pal1:
		for j in aux:
			if i==j:
				return True
			else:
				return False

if __name__=="__main__":
	prueba = "abajo"
	prueba2 ="ojaba"
	print esInversa(prueba,prueba2)
