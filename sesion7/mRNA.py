def mRNA(DNA):
	c1='U'
	c2='A'
	c3='G'
	c4='C'
	res=""
	result=[]
	for i in DNA:
		if i == 'A':
			result.append(c1)
		elif i=='T':
			result.append(c2)
		elif i=='C':
			result.append(c3)
		elif i=='G':
			result.append(c4)
	for i in result:
		res+=i
	return res	
	
if __name__=="__main__":
	DNA="ATCGATTG"
	resultado = mRNA(DNA)
	print (resultado)	
