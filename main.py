#! /usr/bin/env python3

from cmath import pi
import os, sys
from clases.Imagen import Imagen

if __name__ == "__main__":
    """
    Funtcion main
    """
    if len(sys.argv) == 3 or len(sys.argv) == 4:
        if os.path.exists(sys.argv[2]) or os.path.exists(sys.argv[3]):
            img1 = Imagen.leerImagen(sys.argv[2])
            if (sys.argv[1] == "--all") or (sys.argv[1] == "-a"):
                img1.crearTodo()
            elif (sys.argv[1] == "--inverse") or (sys.argv[1] == "-i"):
                nom = Imagen.dameExtensionYNombre(img1.getNombre())
                Imagen.inversa(img1).imprimirPgmEnFichero(nom[0] + "_inverse." + nom[1])
            elif (sys.argv[1] == "--transposed") or (sys.argv[1] == "-t"):
                nom = Imagen.dameExtensionYNombre(img1.getNombre())
                Imagen.transponer(img1).imprimirPgmEnFichero(
                    nom[0] + "_transposed." + nom[1]
                )
            elif (sys.argv[1] == "--encode") or (sys.argv[1] == "-e"):
                if len(sys.argv) == 4:
                    nom = Imagen.dameExtensionYNombre(img1.getNombre())
                    texto1 = str(open(sys.argv[3]).readlines())
                    Imagen.codificar(img1, texto1).imprimirPgmEnFichero(
                        nom[0] + "_codificated." + nom[1]
                    )
                else:
                    print("A text file to insert in PGM image is required.")
            elif (sys.argv[1] == "--decodificar") or (sys.argv[1] == "-d"):
                nom = Imagen.dameExtensionYNombre(img1.getNombre())
                Imagen.imprimirTextoEnFichero(
                    nom[0] + "_decoded." + nom[1], 
                    Imagen.descodificar(img1)
                )
            else:
                print("The parameter '" + sys.argv[1] + "' do not exist.")
        else:
            print("The file '" + sys.argv[2] + "' do not exist.")
    else:
        print(sys.argv[0] + " [ARGUMENT] [FILE-NAME] [FILE-TO-CODIFICATE]")
        print("ARGUMENTS: ")
        print(" --inverse, -i : Return the inverse of given file")
        print(" --transposed, -t : Return the transposed of given file")
        print(" --all, -a : Return both options (inverse and transposed) ")
        print(" --encode, -e : Encode text inside a PGM file")
        print(" --decode, -d : Return the text from a PGM file encoded")
