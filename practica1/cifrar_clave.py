import utilidades

def cifrar_clave(texto,clave,n):
	alfabeto_final = utilidades.Transformar_alfabeto(texto,clave,n)
	
	dic={}
	for i in range(0,len(alfabeto_final)):
		dic[alfabeto_final[i]]=alfabeto_final[(i+n)%len(alfabeto_final)]
	
	txt_cfr=""
	for l in texto.lower():
		if l in dic:
			l=dic[l]
			txt_cfr+=l
	return txt_cfr

if __name__=="__main__":

	texto="plaza nueva"
	clave=3
	text="Primera practica de programacion tecnica y cientifica"
	res = cifrar_clave(text,texto,clave)
	print (res)
