import utilidades
import string

def cifrar_cesar(texto,desplazamiento):
	alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	
	dic={}
	for i in range(0,len(alfabeto)):
		dic[alfabeto[i]]=alfabeto[(i+desplazamiento)%len(alfabeto)]
		
	txt_cfr=""
	for l in texto.lower():
		if l in dic:
			l=dic[l]
		txt_cfr+=l
	return txt_cfr
	
	
if __name__=="__main__":

	print ('Introduce texto para pasarlo a codigo cesar: ')
	text = raw_input().lower()
	print (text)
	des = int(input('Introduce el desplazamiento: '))
	res = cifrar_cesar(text,des)
	print (res)
