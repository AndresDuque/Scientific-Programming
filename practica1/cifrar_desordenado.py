import utilidades

def cifrar_desordenado(texto,clave):
	alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	clave_v=[]
	for i in clave:
		clave_v.append(i)
	clave_o=[]
	for i in clave_v:
		clave_o.append(ord(i)-ord('a'))
	##print clave_o
	dic={}
	for i in range(0,len(alfabeto)):
		for j in range(0,len(alfabeto)%len(clave_o)):
			for n in range(0,len(clave_o)):
				desplazamiento=(clave_o[j+n])
				##print desplazamiento
				dic[alfabeto[i]]=alfabeto[(i+desplazamiento)%len(alfabeto)]
	
	txt_cfr=""
	for l in texto.lower():
		if l in dic:
			l=dic[l]
		txt_cfr+=l
	return txt_cfr
	
if __name__=="__main__":

	texto = "primera practica de pct"
	clave = "lapiz"
	print (cifrar_desordenado(texto,clave))
	
	
	
		
	
