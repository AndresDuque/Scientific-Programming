def inversa(l):
	final=""
	lista_result=l.split()
	lista_result.reverse()
	return " ".join(lista_result)
	
if __name__=='__main__':
	l="four score and seven years"
	final=inversa(l)
	print (final)
	
