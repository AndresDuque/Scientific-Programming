
mat= [[0,3],[6,4]]

def dimensiones(matriz):
	col=0
	fil=0
	for i in matriz:
		fil +=1
		for j in matriz:
			col+=1
	return i, j

if __name__=="__main__":
	f, c = dimensiones(mat)
	print f, c

