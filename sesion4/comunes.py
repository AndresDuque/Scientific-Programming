def comunes(pal1,pal2):
	res = ""
	for i in pal1:
		for j in pal2:
			if j==i:
				res+=j
	return res;
				
	
if __name__=="__main__":
	prueba = "coma"
	prueba2="comer"
	print comunes(prueba,prueba2)
