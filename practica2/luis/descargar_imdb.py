# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 17:57:43 2013

@author: Luis Baca Ruiz.
"""
import utilidades as ut
import urllib.request
import re
import gzip
import os

#==============================================================================
# Descomprime uno de los ficheros.
#==============================================================================
def descomprimir(nombre):
    fichero_gz  = nombre + ".list.gz"
    fichero_txt = nombre + ".list.txt"
    f_comprimido = gzip.open(fichero_gz)
    tam = os.path.getsize(fichero_gz)
    f_descompri  = open(fichero_txt, 'wb')
    descomprimido = 0
    while True:
        buffer = f_comprimido.read(8192)
        if not buffer:
            break
        descomprimido += len(buffer)
        f_descompri.write(buffer)
        estado = "%10d {%3.2f%%}" % (descomprimido, descomprimido * 100. / int(tam))
        print(estado)
    f_comprimido.close()



#==============================================================================
# Descarga los ficheros 'actor.list.gz' y 'actresses.list.gz' si no están 
#  descargados. En el caso de que esten desactualizados tambien los descarga
#  y los actualiza. Y finalmente los descomprime.
# Si ya están actualizados entonces nos indica que lo están.
#==============================================================================
def descargarIMDB(fichero, web):
    # Probamos abrir el fichero.
    file = ut.abrirFichero(fichero)
    # Abrimos la página web.
    gestor   = urllib.request.urlopen(pagina)
    # Leemos de la página web los ficheros.
    ficheros = gestor.readlines()
    # Si el fichero se abrió (existe).
    if file != None:
        # Comprobamos la fecha.
        fecha_web = (re.findall("[A-Z][a-z][a-z] [0-9][0-9]", str(ficheros[1])) )[0]
        fecha_arch= (re.findall("[A-Z][a-z][a-z] [0-9][0-9]", str(file.readline())) )[0]
        if fecha_web == fecha_arch:
            print("El archivo \'%s\' está actualizado." % (fichero))
        else:
            print("El archivo \'%s\' no está actualizado." %(fichero))
            file.close()
            os.remove(fichero)
            print("El fichero se va a actualizar.")
            # Volvemos a llamar a la misma funcion. Para que lo descargue.
            descargarIMDB(fichero, web)
    # Si el fichero no se abrió (no existe), lo descargamos.
    else:
        # Si es para los actores.
        if fichero == 'actors.list.txt':
            url = 'ftp://ftp.fu-berlin.de/pub/misc/movies/database/actors.list.gz'
            # Abrimos el fichero donde descargarlo.   
            f = open('actors.list.gz', 'wb')
            # Abrimos la direccion del fichero.
            u = urllib.request.urlopen(url)
            # Guardamos los metadatos.
            metadatos = u.info()
            # Obtenemos el tamaño del fichero.
            tam = metadatos.get("Content-length")
            print("Descargando:",'actors.list.gz',"-> Bytes:", tam)
            
            # Lo descargamos.
            descargado = 0
            bloque     = 8192
            while True:
                buffer = u.read(bloque)
                if not buffer:
                    break
                descargado += len(buffer)
                f.write(buffer)
                estado = "%10d [%3.2f%%]" % (descargado, descargado * 100. / int(tam))
                # Mostramos el estado de la descarga.
                print(estado)
            f.close()
            
            # Descomprimiendo archivo.
            descomprimir("actors", tam)
            
            
        # Para las actrices igual.
        else:
            url = 'ftp://ftp.fu-berlin.de/pub/misc/movies/database/actresses.list.gz'
            # Abrimos el fichero donde descargarlo.   
            f = open('actresses.list.gz', 'wb')
            # Abrimos la direccion del fichero.
            u = urllib.request.urlopen(url)
            # Guardamos los metadatos.
            metadatos = u.info()
            # Obtenemos el tamaño del fichero.
            tam = metadatos.get("Content-length")
            print("Descargando:",'actresses.list.gz',"-> Bytes:", tam)
            
            # Lo descargamos.
            descargado = 0
            bloque     = 8192
            while True:
                buffer = u.read(bloque)
                if not buffer:
                    break
                descargado += len(buffer)
                f.write(buffer)
                estado = "%10d [%3.2f%%]" % (descargado, descargado * 100. / int(tam))
                # Mostramos el estado de la descarga.
                print(estado)
            f.close()
            # Descomprimimos el archivo.
            descomprimir("actresses", tam)




#==============================================================================
#==============================================================================
# # Código de pruebas.
#==============================================================================
#==============================================================================
if __name__== "__main__": 
    pagina = "ftp://ftp.fu-berlin.de/pub/misc/movies/database/"
    readme = "README"
    actors   = 'actors.list.txt'
    actrices = 'actresses.list.txt'
#    print(descargarIMDB(actors, pagina))
#    descromprimir(actors)
    descargarIMDB(actors, pagina)
    descargarIMDB(actrices, pagina)
    
