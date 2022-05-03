#! /usr/bin/env python3


from email.charset import Charset

PIXEL_SPLIT = 16

class Imagen:
    def __init__(self, tip="P2", nom="img1", des="imagen1", f1=200, c1=200):
        """
        Objet imagen
        """
        self.tipo = tip
        self.nombre = nom
        self.comentario = des
        self.filas = f1
        self.columnas = c1
        self.vector1 = list()
        for ff in range(0, self.filas):
            for cc in range(0, self.columnas):
                self.vector1.append(0)

    def getNombre(self):
        """
        return name
        """
        return self.nombre

    def getTipo(self):
        """
        return tipe
        """
        return self.tipo

    def getComentario(self):
        """
        return comment
        """
        return self.comentario

    def getFilas(self):
        """
        return number of files
        """
        return self.filas

    def getColumnas(self):
        """
        return number of columns
        """
        return self.columnas

    def setNombre(self, nom):
        """
        set name
        """
        self.nombre = nom

    def setTipo(self, tip):
        """
        set tipe
        """
        self.tipo = tip

    def setComentario(self, des):
        """
        set comment
        """
        self.comentario = des

    def setPixel(self, fila, columna, valor):
        """
        set pixel
        """
        self.vector1[(fila * self.columnas) + columna] = valor

    def setPixelPos(self, lugar, valor):
        """
        set pixel2
        """
        self.vector1[lugar] = valor

    def getPixel(self, fila, columna):
        """
        return pixel
        """
        return self.vector1[(fila * self.columnas) + columna]

    def getPixelPos(self, lugar):
        """
        return pixel2
        """
        return self.vector1[lugar]

    @staticmethod
    def leerImagen(nom):
        """
        Read image file
        """
        f1 = open(nom, "rb")
        c1 = ""
        # Para leer el tipo de fichero
        tipo = str(f1.readline()).split("'")[1].split("\\")[0]
        # Para leer el comentario
        des = str(f1.readline()).split("'")[1].split("\\")[0]
        cad = str(f1.readline()).split("'")[1].split("\\")[0]
        filas = int(cad.split(" ")[0])
        columnas = int(cad.split(" ")[1])
        img1 = Imagen(tipo, nom, des, filas, columnas)
        str(f1.readline())  # Para leer el tamano maximo
        num = 0
        lugar = 0
        while lugar != (filas * columnas):
            cad = str(f1.read(1)).split("'")[1].split("\\")[0]
            if cad != "":
                num = (num * 10) + int(cad)
            else:
                img1.setPixelPos(lugar, int(num))
                num = 0
                lugar += 1

        f1.close()
        return img1

    def imprimirPgmEnFichero(self, nombre):
        """
        Print image file
        """
        f1 = open(nombre, "w")
        f1.write(
            self.getTipo()
            + "\n"
            + self.getComentario()
            + "\n"
            + str(self.getFilas())
            + " "
            + str(self.getColumnas())
            + "\n255\n"
        )
        for ff in range(0, (self.filas * self.columnas)):
            f1.write(str(self.getPixelPos(ff)) + "\n")
        f1.close()

    def imprimir(self):
        """
        Print image file
        """
        print(
            self.getTipo()
            + "\n"
            + self.getComentario()
            + "\n"
            + str(self.getFilas())
            + " "
            + str(self.getColumnas())
            + "\n255\n"
        )
        for f1 in range(0, self.filas):
            for c1 in range(0, self.columnas):
                print(str(self.getPixel(f1, c1)))

    # Extension de un fichero
    @staticmethod
    def dameExtensionYNombre(nombre):
        """
        Return a image string vector (name, extension)
        """
        nom = str(nombre).split(".")
        nom2 = ""
        exte = nom[len(nom) - 1]
        for ln in nom:
            if ln != exte:
                nom2 = nom2 + "." + ln
        list1 = list()
        list1.append(nom2.split(".")[1])
        list1.append(exte)
        return list1

    @staticmethod
    def inversa(img1):
        """
        Create a inverse image
        """
        imagen = img1
        for ff in range(0, (imagen.filas * imagen.columnas)):
            imagen.setPixelPos(ff, (255 - imagen.getPixelPos(ff)))
        return imagen

    @staticmethod
    def transponer(img1):
        """
        Create a image transponse
        """
        imagen = img1
        numPixTotal = int((imagen.filas * imagen.columnas) / 2) - 1
        for f1 in range(0, numPixTotal):
            pixAntiguo = imagen.getPixelPos(f1)
            pixNuevo = imagen.getPixelPos(imagen.filas - f1)
            imagen.setPixelPos(f1, pixNuevo)
            imagen.setPixelPos((imagen.filas - f1), pixAntiguo)
        return imagen

    def crearTodo(self):
        """
        Create a image inserse, other transponse and last inerse and transponse
        """
        self.setComentario("# Using Python3.3: PGM-Python")
        nom = Imagen.dameExtensionYNombre(self.getNombre())[0]
        exte = Imagen.dameExtensionYNombre(self.getNombre())[1]
        Imagen.transponer(self).imprimirPgmEnFichero(nom + "_transpuesta." + exte)
        neg = Imagen.inversa(self)
        neg.imprimirPgmEnFichero(nom + "_inversa." + exte)
        Imagen.transponer(neg).imprimirPgmEnFichero(nom + "_inversa_transpuesta." + exte)

    @staticmethod
    def codificar(img1,texto1):
        """
        Create codificate text in a image
        """
        imagen = img1
        numPixTotal = int((imagen.filas * imagen.columnas) / 2) - 1
        numLetrasTotal = len(texto1)
        posEnTexto=0
        posEnImagen=0
        while (posEnImagen + PIXEL_SPLIT) < numPixTotal and posEnTexto <= numLetrasTotal:
            if posEnTexto != numLetrasTotal:
                imagen.setPixelPos(posEnImagen, ord(texto1[posEnTexto]))
            else:
                imagen.setPixelPos(posEnImagen, 254)
            posEnTexto = posEnTexto + 1
            posEnImagen = posEnImagen + PIXEL_SPLIT
        return imagen

    @staticmethod
    def descodificar(img1):
        """
        Create decodify text in a image
        """
        imagen = img1
        numPixTotal = int((imagen.filas * imagen.columnas) / 2) - 1
        textoFinal = ""
        letra = 0
        posEnImagen = 0
        while letra != 254 and posEnImagen < numPixTotal:
            letra = imagen.getPixelPos(posEnImagen)
            textoFinal = textoFinal + chr(letra)
            posEnImagen = posEnImagen + PIXEL_SPLIT
        return textoFinal

    @staticmethod
    def imprimirTextoEnFichero(nombre,textoFinal):
        """
        Print text in file
        """
        f1 = open(nombre, "w")
        for line in textoFinal.split("', '"):
            line2 = line
            # Strat chars in file
            if line2[0:2] == "['":
                line2 = line2[2:len(line2)]
            # Last chars in file
            if line2[len(line2)-2:len(line2)] == "]þ" :
                line2 = line2[0:len(line2)-3]
            else:
                line2 = line2[0:len(line2)-2]
            f1.write(line2+"\n")
        f1.close()

if __name__ == "__main__":
    """
    Funcion main
    """
    print("Clase Imagen")
