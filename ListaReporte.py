from NodoReporte import Nodo
import webbrowser
class ListaReporte:
    def __init__(self):
        self.inicio = None

    def insertar(self,StringReporte):
        nuevo = Nodo(StringReporte)
        if self.inicio is None:
            self.inicio = nuevo
            return nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
        return nuevo

    def insertarFinal(self,StringReporte):
        nuevo = Nodo(StringReporte)
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


   
    def mostrar(self):
        concatenar = ""
        tmp = self.inicio
        while tmp is not None:
            print('Mensaje: '+ str(tmp.StringReporte))
            concatenar =  concatenar + "<tr>"+"<td>"+str(tmp.StringReporte)+"</td>"+"</tr>"
            tmp = tmp.siguiente
        
        hola = concatenar = """<html>
        <head>
        <title>Reporte Proyecto 2</title> <meta charset="utf-8">
        <link rel="stylesheet" type="text/css" href="estilosCU01052D.css">
        </head>
        <body>
		<table border="1">
		<caption>Reporte Proyecto 2</caption> """ + concatenar + """</table>
	    </body>
        </html>"""

        f = open('Reporte.html','w')

        mensaje = hola

        f.write(mensaje)
        f.close()  
         



          
