#! /usr/bin/env python3

"""
Author: Alejandro Gomez
"""

import os, sys
from clases.Imagen import Imagen

if __name__ == '__main__':
    """
    Funcion main
    """
    if (len(sys.argv)==3):
       if (os.path.exists(sys.argv[2])):          
          img1 = Imagen.leerImagen(sys.argv[2])
          if (sys.argv[1]=="-todo"):
             img1.crearTodo()
          elif (sys.argv[1]=="-inversa"):
             nom=Imagen.dameExtensionYNombre(img1.getNombre())
             Imagen.inversa(img1).imprimirEnFichero(nom[0]+'_inversa.'+nom[1])
          elif (sys.argv[1]=="-transpuesta"):
             nom=Imagen.dameExtensionYNombre(img1.getNombre())
             Imagen.transponer(img1).imprimirEnFichero(nom[0]+'_transpuesta.'+nom[1])
          else:
              print("El parametro '"+sys.argv[1]+"' no existe.")
       else:
           print("El fichero '"+sys.argv[2]+"' no existe.")
    else:
        print(sys.argv[0]+" -[ARGUMENTO] [NOMBREFICHERO]")





