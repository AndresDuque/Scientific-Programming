import os
import re
import sys
import shelve
import gzip
import urllib2

## Lectura sin descomprimir (mas rapido)
def open_gunzip(filename):
    cmd = 'gunzip -c ' + filename
    fp = os.popen(cmd)
    return fp

def process_file(filename, f, num=float('Inf')):
    fp = open_gunzip(filename)
    i = 0

    # Saltar la cabecera
    for line in fp:
        if line.strip() == '----			------':
            break

    # regexp para reconocer actor, tab, movie
    split1 = re.compile('([^\t]*)\t*(.*)', re.UNICODE)

    # regexp para reconocer titulo pelicula, fecha, funcion
    split2 = re.compile('([^\(]*)\s*(\([^\)]*\))[^\[]*(\[[^\]]*\])?', 
                        re.UNICODE)

    # regexp para reconocer television (TV), video (V), video game (VG)
    video = re.compile('\(T?V|VG\)', re.U)

    actor = ''
    for line in fp:
        line = line.rstrip()
        if line == '': continue
        if line[0] == '-----': break
		
		# Divide la linea en info actor y movie info
        ro = split1.match(line)
        if ro:
            new_actor, info = ro.groups()
            if new_actor:
                actor = new_actor
        else:
            print 'BAD1', line
            continue

        # salta television shows (titulos entre comillas)
        if info[0] == '"':
            continue

        # salta video y tv
        if video.search(info):
            continue

        # dividir la informacion en el titulo, la fecha y el papel
        ro = split2.match(info)
        if ro:
            title, date, role = ro.groups()
            if date == None:
                print 'BAD2', line
                continue

            f(actor, date, title, role)
            i += 1
            if i > num: break
        else:
            print 'BAD3', line
            continue

    stat = fp.close()
    return stat
"""
def creartxt():
	archivo_actores=open('actores.txt','w')
	archivo_actores.close()
	archivo_actrices=open('actrices.txt','w')
	archivo_actrices.close()

def print_info_actores(actor, date, title, role):
	actores=open('actores.txt','a')
	sys.stdout=actores
	print actor, date, title, role

def print_info_actrices(actor, date, title, role):
	actrices=open('actrices.txt','a')
	sys.stdout=actrices
	print actor, date, title, role 
"""

def existeFichero(fichero):
	# Comprobamos si existe el fichero.
	existe=os.path.isfile(fichero)
	if existe==True:
		return True
	else:
		return False
		


def comprobar_actualizacion(fichero):
	URL='ftp://ftp.fu-berlin.de/pub/misc/movies/database/'
	file=existeFichero(fichero)
	g=urllib2.Request
	u=urllib2.urlopen(URL)
	ficheros=u.readlines()
	f=existeFichero(fichero)
	if(f!=False):
		webdate=(re.findall("[A-Z][a-z][a-z] [0-9][0-9]", str(ficheros[1])) )[0]
		filedate=(re.findall("[A-Z][a-z][a-z] [0-9][0-9]", str(file.readline())) )[0]
		if webdate==filedate:
			print ("El archivo esta actualizado")
		else:
			print("El archivo esta desactualizado, se procede a actualizar")
			f.close()
			os.remove(f)
			descargar_imdb(fichero)
	
def Descomprimir(archivo):
	if archivo=='actors.list.gz':
		if(existeFichero('actores.txt')==True):
			print("Ya existe actores.txt, descomprimido")
		else:
			f=gzip.open('actors.list.gz','rb')
			uncompress=open('actores.txt','wb')
			file_content=f.read()
			uncompress.write(file_content)
			f.close()
			uncompress.close()
	else:
		if(existeFichero('actrices.txt')==True):
			print("Ya existe archivo descomprimido actrices.txt")
		else:
			f=gzip.open('actresses.list.gz','rb')
			uncompress=open('actrices.txt','wb')
			file_content=f.read()
			uncompress.write(file_content)
			f.close()
			uncompress.close()


if __name__ == '__main__':
    process_file('actresses.list.gz',print_info_actrices)
    ##creartxt()
