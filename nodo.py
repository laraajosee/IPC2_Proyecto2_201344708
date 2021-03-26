from matriz import matriz
class Nodo:
    def __init__(self, nombre,filas, columnas, imagen):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.imagen = matriz()
        self.siguiente = None