def longs(cadenas):
	res=[]
	for i in cadenas:
		res.append(len(i))
	return res

if __name__=="__main__":
	
	lista=['hola','adios','abc']
	resultado=longs(lista)
	print (resultado)
