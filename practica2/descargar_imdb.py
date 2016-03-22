import utilidades
import urllib
import os
import gzip
import urllib2

def descargar_imdb(fichero):
	
	if(utilidades.existeFichero(fichero)==True):
		print ("El fichero ya existe")
	else:
		if fichero=='actors.list.gz':
			URL= 'ftp://ftp.fu-berlin.de/pub/misc/movies/database/actors.list.gz'
			##urllib.urlretrieve(URL,fichero)
			## fichero donde descargarlo
			f1= open('actors.list.gz', 'wb')
			req=urllib2.Request(URL)
			u=urllib2.urlopen(URL)
			datos=u.info()
			##Tamanio fichero
			t=datos.get("Content-length")
			print("Descargando:",'actors.list.gz',"-> Bytes:", t)
			des=0
			tam_bloque=8192
		
			while True:
				buffer=u.read(tam_bloque)
				if not buffer:
					break
				des+=len(buffer)
				f1.write(buffer)
				estado_descarga="%10d [%3.2f%%]" % (des, des * 100. / int(t))
				print (estado_descarga)
			f1.close()
			
			#Descomprimimos
			#utilidades.Descomprimir(fichero)
			
		else:
			URL='ftp://ftp.fu-berlin.de/pub/misc/movies/database/actresses.list.gz'
			f2=open('actresses.list.gz','wb')
			req=urllib2.Request(URL)
			u=urllib2.urlopen(URL)
			datos=u.info()
			##Tam fichero
			t=datos.get("Content-length")
			print ("Descargando:",'actresses.list.gz',"->Bytes:",t)
			des=0
			tam_bloque=8192
		
			while True:
				buffer=u.read(tam_bloque)
				if not buffer:
					break
				des+=len(buffer)
				f2.write(buffer)
				estado_descarga="%10d [%3.2f%%]" % (des,des*100/int(t))
				print (estado_descarga)
			f2.close()
			
			#Descomprimir
			#utilidades.Descomprimir(fichero)
		
		
if __name__=='__main__':
	
	print("Que archivos deseas descargar")
	print ("Pulsa 1 para: actores.list.gz ")
	print ("Pulsa 2 para: actresses.list.gz ")
	num=input("-->")
	
	if num==1:
		print("Se procede a descargar actores.list.gz")
		fichero=('actors.list.gz')
		descargar_imdb(fichero)
		utilidades.process_file('actors.list.gz',utilidades.print_info_actores)
	if num==2:
		print("Se procede a descargar actresses.list.gz")
		fichero=('actresses.list.gz')
		descargar_imdb(fichero)
		utilidades.process_file('actresses.list.gz',utilidades.print_info_actrices)
		
