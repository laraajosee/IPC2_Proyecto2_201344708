from nodos import Nodo, nodoEncabezado
from encabezado import listaEncabezado
from graphviz import Graph

class matriz:
    def __init__(self) :
        self.eFilas = listaEncabezado()
        self.eColumnas = listaEncabezado()



    def insertar(self, fila, columna, valor):
        nuevo = Nodo(fila, columna, valor)
          #inrestar por filas
        eFila = self.eFilas.getEncabezado(fila)
        if eFila == None:
            eFila = nodoEncabezado(fila)
            eFila.accesoNodo = nuevo
            self.eFilas.setEncabezado(eFila)
        else:
            if nuevo.columna < eFila.accesoNodo.columna:
                nuevo.derecha = eFila.accesoNodo
                eFila.accesoNodo.izquierda = nuevo
                eFila.accesoNodo = nuevo
            else:
                actual = eFila.accesoNodo
                while actual.derecha != None:
                    if nuevo.columna < actual.derecha.columna:
                        nuevo.derecha = actual.derecha
                        actual.derecha.izquierda = nuevo
                        nuevo.izquierda = actual
                        actual.derecha = nuevo
                        break
                    actual = actual.derecha

                if actual.derecha == None: 
                    actual.derecha = nuevo
                    nuevo.izquierda = actual
                     

    def recorrerFilas(self):
        eFila = self.eFilas.primero   
        print("\n**************recorrido por filas*************************")

        while eFila != None:

            actual = eFila.accesoNodo
            print("\nfila"+str(actual.fila))
            print("columna   valor  ")
            while actual != None:
                print(str(actual.columna)+"      "+ actual.valor)
                actual = actual.derecha

            eFila = eFila.siguiente

        print("\n**************FIn recorrido por filas*************************")

    def llenarCeldas(self, var):
      
        eFila = self.eFilas.primero  
        concatenar = ''
        concatenar = "<<TABLE>" 
        #print("\n**************empezando tabla*************************")

        while eFila != None:
            
            concatenar = concatenar + "\n<TR>"
            #print("creando Fila")
            actual = eFila.accesoNodo
            #print("\nfila"+str(actual.fila))
            #print("columna   valor  ")
            while actual != None:
                #print(str(actual.columna)+"            "+ actual.valor)
                if(actual.valor== '*'):
                 concatenar = concatenar + "\n<TD bgcolor='black'>*</TD>" 
                if(actual.valor== '-'):
                 concatenar = concatenar + "\n<TD> </TD>" 
                actual = actual.derecha
            concatenar = concatenar + "\n</TR>"
            print("finalizando filas")
            eFila = eFila.siguiente
        
        concatenar = concatenar + "\n</TABLE>>"
        #print("\n**************Finalizando Tabla *************************")
        h = Graph(var, format='png')
        h.node('tab', label=concatenar)
        h.view()

    def recorrerColumnas(self):
        eColumna = self.eColumnas.primero
        print("\n**************recorrido por columnas*************************")

        while eColumna != None:

            actual = eColumna.accesoNodo
            print("\nColumna"+str(actual.columna))
            print("fila     valor   ")
            while actual != None:
                print(str(actual.fila)+"     "+actual.valor)
                actual = actual.abajo

            eColumna = eColumna.siguiente  
       
        print("\n**************fin  recorrido por columnas*************************")
