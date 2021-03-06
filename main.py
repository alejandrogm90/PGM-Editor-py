#! /usr/bin/env python3

import os, sys
from clases.Imagen import Imagen

if __name__ == '__main__':
    """
    Funtcion main
    """
    if (len(sys.argv)==3):
       if (os.path.exists(sys.argv[2])):          
          img1 = Imagen.leerImagen(sys.argv[2])
          if (sys.argv[1]=="-all"):
             img1.crearTodo()
          elif (sys.argv[1]=="-inverse"):
             nom=Imagen.dameExtensionYNombre(img1.getNombre())
             Imagen.inversa(img1).imprimirEnFichero(nom[0]+'_inverse.'+nom[1])
          elif (sys.argv[1]=="-transposed"):
             nom=Imagen.dameExtensionYNombre(img1.getNombre())
             Imagen.transponer(img1).imprimirEnFichero(nom[0]+'_transposed.'+nom[1])
          else:
              print("The parameter '"+sys.argv[1]+"' do not exist.")
       else:
           print("The file '"+sys.argv[2]+"' do not exist.")
    else:
        print(sys.argv[0]+" -[ARGUMENT] [FILE-NAME]")





