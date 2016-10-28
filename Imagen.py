#! /usr/bin/env python3



import random

class Imagen:
    
    def __init__(self,tip="P2",nom="img1",des="imagen1",f1=200,c1=200):
        """
        Objeto imagen
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
        Devuelve el nombre
        """
        return self.nombre

    def getTipo(self):
        """
        Devuelve el tipo
        """
        return self.tipo

    def getComentario(self):
        """
        Devuelve el comentario
        """
        return self.comentario

    def getFilas(self):
        """
        Devuelve el numero de filas
        """
        return self.filas

    def getColumnas(self):
        """
        Devuelve el numero de columnas
        """
        return self.columnas

    def setNombre(self,nom):
        """
        Edita el nombre
        """
        self.nombre=nom

    def setTipo(self,tip):
        """
        Edita el tipo
        """
        self.tipo=tip

    def setComentario(self,des):
        """
        Edita el comentario
        """
        self.comentario=des

    def setPixel(self,fila,columna,valor):
        """
        Edita un pixel
        """
        self.vector1[(fila*self.columnas)+columna]=valor

    def setPixelPos(self,lugar,valor):
        """
        Edita un pixel2
        """
        self.vector1[lugar]=valor

    def getPixel(self,fila,columna):
        """
        Devuelve un pixel
        """
        return self.vector1[(fila*self.columnas)+columna]

    def getPixelPos(self,lugar):
        """
        Devuelve un pixel2
        """
        return self.vector1[lugar]

    @staticmethod
    def leerImagen(nom):
        """
        Lee de fichero una imagen
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
        Imprime en fichero la imagen
        """
        f1=open(nombre,'w')
        f1.write(self.getTipo()+'\n'+self.getComentario()+'\n'+str(self.getFilas())+' '+str(self.getColumnas())+"\n255\n")
        for ff in range(0,(self.filas*self.columnas)):
            f1.write(str(self.getPixelPos(ff))+"\n")
        f1.close()

    def imprimir(self):
        """
        Imprime la imagen
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
        Devuelve un vector con el nombre y la extension de la imagen
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
        Crea la imagen inversa
        """
        imagen=img1
        for ff in range(0,(imagen.filas*imagen.columnas)):
            imagen.setPixelPos(ff,(255-imagen.getPixelPos(ff)))
        return imagen
    
    @staticmethod
    def transponer(img1):
        """
        Crea la imagen transpuesta
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
        Crea todos los tipos de versiones de la imagen PGM
        """
        self.setComentario("# Using Python3.3: Falcon90")
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



















            



