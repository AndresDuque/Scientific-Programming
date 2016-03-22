# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 17:57:43 2013

@author: Luis Baca Ruiz.
"""
import os

def existeFichero(nombre):
    # Comprobamos si existe el fichero.
    return os.path.isfile(nombre)

def abrirFichero(nombre):
    # Comprobamos si existe el fichero.
    existe = existeFichero(nombre)
    # Si existe.
    if existe == True:
        return open(nombre)
    # Sino.
    else:
        return None


#==============================================================================
#==============================================================================
# # Código de pruebas.
#==============================================================================
#==============================================================================
if __name__== "__main__": 
    nom_fich = "README"
    print(abrirFichero(nom_fich))
