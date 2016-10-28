#! /usr/bin/env python3

import random

class Imagen:
    
    def __init__(self,tip="P2",nom="img1",des="imagen1",f1=200,c1=200):
        """
        Objet imagen
        """
        self.tipo=tip
        self.nombre=nom
        self.comentario=des
        self.filas=f1
        self.columnas=c1
        self.vector1=list()
        for ff in range(0,self.filas):
            for cc in range(0,self.columnas):
                self.vector1.append(0)#int(random.uniform(0,255)))

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

    def setNombre(self,nom):
        """
        set name
        """
        self.nombre=nom

    def setTipo(self,tip):
        """
        set tipe
        """
        self.tipo=tip

    def setComentario(self,des):
        """
        set comment
        """
        self.comentario=des

    def setPixel(self,fila,columna,valor):
        """
        set pixel
        """
        self.vector1[(fila*self.columnas)+columna]=valor

    def setPixelPos(self,lugar,valor):
        """
        set pixel2
        """
        self.vector1[lugar]=valor

    def getPixel(self,fila,columna):
        """
        return pixel
        """
        return self.vector1[(fila*self.columnas)+columna]

    def getPixelPos(self,lugar):
        """
        return pixel2
        """
        return self.vector1[lugar]

    @staticmethod
    def leerImagen(nom):
        """
        Read image file
        """
        #f1=open(nom,'r')  
        f1=open(nom,'rb')  #Leer byte
        #print(nom)
        c1 = ''
        tipo = str(f1.readline()).split('\'')[1].split('\\')[0]#Para leer el tipo de fichero
        des=str(f1.readline()).split('\'')[1].split('\\')[0]#Para leer el comentario
        cad = str(f1.readline()).split('\'')[1].split('\\')[0]
        filas = int(cad.split(' ')[0])
        columnas = int(cad.split(' ')[1])
        #print("Tipo: "+str(tipo)+" Filas:"+str(filas)+" Columnas: "+str(columnas))
        img1 = Imagen(tipo,nom,des,filas,columnas)
        str(f1.readline()) #Para leer el tamano maximo
        num = 0
        lugar = 0
        while (lugar != (filas * columnas)): #or lugar > (filas * columnas * 2)):
            cad = str(f1.read(1)).split('\'')[1].split('\\')[0]
            #print(cad)
            if (cad != ''):
                num = (num * 10) + int(cad)
            else:
                img1.setPixelPos(lugar,int(num))
                num=0
                lugar+=1
                
        f1.close()
        return img1

    def imprimirEnFichero(self,nombre):
        """
        Print image file
        """
        f1=open(nombre,'w')
        f1.write(self.getTipo()+'\n'+self.getComentario()+'\n'+str(self.getFilas())+' '+str(self.getColumnas())+"\n255\n")
        for ff in range(0,(self.filas*self.columnas)):
            f1.write(str(self.getPixelPos(ff))+"\n")
        f1.close()

    def imprimir(self):
        """
        Print image file
        """
        print(self.getTipo()+'\n'+self.getComentario()+'\n'+str(self.getFilas())+' '+str(self.getColumnas())+"\n255\n")
        for f1 in range(0,self.filas):
            for c1 in range(0,self.columnas):
                print(str(self.getPixel(f1,c1)))

    # OTRAS FUNCIONES IMPORTANTES

    # Extension de un fichero
    @staticmethod
    def dameExtensionYNombre(nombre):
        """
        Return a image string vector (name, extension)
        """
        nom=str(nombre).split('.')
        nom2=""
        exte=nom[len(nom)-1]
        for ln in nom:
            if (ln!=exte):
               nom2=nom2+'.'+ln
        list1=list()
        list1.append(nom2.split('.')[1])
        list1.append(exte)
        return list1

    # El inversa de una imagen
    @staticmethod
    def inversa(img1):
        """
        Create a inverse image
        """
        imagen=img1
        for ff in range(0,(imagen.filas*imagen.columnas)):
            imagen.setPixelPos(ff,(255-imagen.getPixelPos(ff)))
        return imagen
    
    @staticmethod
    def transponer(img1):
        """
        Create a image transponse
        """
        imagen=img1
        numPixTotal=int((imagen.filas*imagen.columnas)/2)-1
        for f1 in range(0,numPixTotal):
            pixAntiguo=imagen.getPixelPos(f1)
            pixNuevo=imagen.getPixelPos(imagen.filas-f1)
            imagen.setPixelPos(f1,pixNuevo)
            imagen.setPixelPos((imagen.filas-f1),pixAntiguo)
        return imagen
    
    def crearTodo(self):
        """
        Create a image inserse, other transponse and last inerse and transponse
        """
        self.setComentario("# Using Python3.3: PGM-Python")
        nom=Imagen.dameExtensionYNombre(self.getNombre())[0]
        exte=Imagen.dameExtensionYNombre(self.getNombre())[1]
        Imagen.transponer(self).imprimirEnFichero(nom+'_transpuesta.'+exte)
        neg=Imagen.inversa(self)
        neg.imprimirEnFichero(nom+'_inversa.'+exte)
        Imagen.transponer(neg).imprimirEnFichero(nom+'_inversa_transpuesta.'+exte)
        
if __name__ == '__main__':
    """
    Funcion main
    """
    print("Clase Imagen")



















            



