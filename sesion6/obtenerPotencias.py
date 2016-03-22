def obtenerPotencias(numero):
	##if type(numero)!= type(int)
	lista=[]
	auxl=[]
	r=numero-1
	while numero>=0:
		aux=numero
		aux2=aux*aux
		numero=numero-1
		lista.append(aux2)
		
	lista.extend(lista[r::-1])
	return lista
	
if __name__=="__main__":
	numero = 7
	res=obtenerPotencias(numero)
	print (res)
