from nodo import Nodo

class ListaEnlazada:
    def __init__(self):
        self.inicio = None

    def insertar(self,nombre,filas,columnas,imagen):
        nuevo = Nodo(nombre, filas,columnas,imagen)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

    def mostrarMatriz(self):
        tmp = self.inicio
        while tmp is not None:
            print('Nombre Matriz: '+ str(tmp.nombre)+' filas: '+ str(tmp.filas)+ ' columnas: '+ str(tmp.columnas+'\n imagen: '+ str(tmp.imagen)))
            tmp = tmp.siguiente