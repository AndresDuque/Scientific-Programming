def contarLetras(palabra):
	aux={}
	res=[]
	contador=1
	for i in palabra:
		a=i
		if i==a:
			aux={i:contador}
			res.append(aux)
		else:
			contador=contador+1
			aux={i:contador}
			res.append(aux)
	return res

if __name__=="__main__":
	
	pal='patata'
	resultado=contarLetras(pal)
	print (resultado)
