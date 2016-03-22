def dispersa(v):
	res=[]
	resultado= {}
	for val in range(len(v)):
		if val !=0:
			res.append(val)
	return res
	
	


if __name__=="__main__":
	v=(0,0,0,0,0,0,0,0,0,0,0,0,16,0,0,0,0,36,0,0,0)
	res=dispersa(v)
	print (res)
	
