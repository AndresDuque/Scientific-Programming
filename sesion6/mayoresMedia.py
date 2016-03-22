def mayoresMedia(numeros):
	media=(sum(numeros)/len(numeros))
	print (media)
	res=[]
	for i in numeros:
		if i>media:
			res.append(i)
	return res

if __name__=="__main__":
	numeros=[1,2,3,5,15,13,5,7,3,8,3,1,5,20]
	resultado=mayoresMedia(numeros)
	print (resultado)
	
	
