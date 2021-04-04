from matriz import matriz
from nodo import Nodo
from graphviz import Graph

class ListaEnlazada:
    def __init__(self):
        self.inicio = None

    def insertar(self,nombre,filas,columnas,imagen):
        nuevo = Nodo(nombre, filas,columnas,imagen)
        if self.inicio is None:
            self.inicio = nuevo
            return nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
        return nuevo

    def insertarFinal(self,nombre, filas,columnas,imagen):
        nuevo = Nodo(nombre, filas,columnas,imagen)
        if self.inicio is None:
            self.inicio = nuevo
            return nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
            nuevo.anterior = tmp
            return nuevo
        return None

    def getNodo(self, valor):
        tmp = self.inicio
        while tmp is not None:
            if str.lower(tmp.nombre) == str.lower(valor):
                return tmp
            tmp = tmp.siguiente
        return None
    
    def getFilas(self, valor):
        tmp = self.inicio
        while tmp is not None:
            if str.lower(tmp.nombre) == str.lower(valor):
                return tmp.filas
            tmp = tmp.siguiente
        return None

    def getColumnas(self, valor):
        tmp = self.inicio
        while tmp is not None:
            if str.lower(tmp.nombre) == str.lower(valor):
                return int(tmp.columnas)
            tmp = tmp.siguiente
        return None

        
    def mostrarMatriz(self):
        tmp = self.inicio
        while tmp is not None:
            print('Nombre Matriz: '+ str(tmp.nombre)+' filas: '+ str(tmp.filas)+ ' columnas: '+ str(tmp.columnas)+'\n imagen: ')
            tmp.imagen.recorrerFilas()
            tmp = tmp.siguiente

    def listaCombobox(self):
         tmp = self.inicio
         lista = []
         while tmp is not None:          
            #cadena = cadena+'"'+str(tmp.nombre)+'"'+',\n'
            lista.append(tmp.nombre)
            tmp = tmp.siguiente
         
        
         return lista
    
    def getSize(self):
        tmp = self.inicio
        cont = 0
        while tmp is not None:
            cont += 1
            tmp = tmp.siguiente
            print(cont)
        return cont

    def crearImagen(self):
        tmp = self.inicio
        while tmp is not None:
            #print('Nombre Matriz: '+ str(tmp.nombre))
            var = str(tmp.nombre)
            #tmp.imagen.recorrerFilas()
            tmp.imagen.llenarCeldas(var)
            #print("esto es hola : " + hola)
            tmp = tmp.siguiente

          
