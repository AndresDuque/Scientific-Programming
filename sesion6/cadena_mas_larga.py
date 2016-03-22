def cadena_mas_larga(cadenas,n):
	res=[]
	for i in cadenas:
		if len(i)>n:
			res.append(i)
	return res


if __name__=="__main__":
	
	prueba=["hola","caballo","aguacate"]
	numero=5
	res = cadena_mas_larga(prueba,numero)
	print(res)
