
def mayuscula(palabra):
	list1= ""
	for i in palabra:
		list1+=i.upper()
	return list1
	
if __name__=="__main__":
	
	listp = "Hola mundo"
	print mayuscula(listp)
