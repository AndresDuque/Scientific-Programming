def cadenas_mas_larga(cadenas):
	res=" "
	for i in cadenas:
		for a in cadenas:
			if len(i)<len(a):
				res=a
	return res
			
			
if __name__=="__main__":
	prueba=["hola","caballo","aguacate"]
	res=cadenas_mas_larga(prueba)
	print (res)
