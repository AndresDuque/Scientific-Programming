def invertirDiccionario(d):
	idict = {}
	for val in d.values():
		idict[val] = []
		for clave in d.keys():
			if d[clave] == val:
				if clave not in idict[val]: idict[val].append(clave)
	return idict

if __name__=="__main__":
	d = {'a':1,'b':2,'c':3, 'd':2}
	result = invertirDiccionario(d)
	print (result)
