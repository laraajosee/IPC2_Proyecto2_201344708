from tkinter import *
from tkinter.filedialog import askopenfilename
import xml.etree.ElementTree as ET
from matriz import matriz
from lista import ListaEnlazada

lista = ListaEnlazada()

def abrir():

    filename = askopenfilename()
    tree = ET.parse(filename)
    root = tree.getroot()

    
    for elemento in root:
     
       # print(elemento.tag) #tag
     for subelemento in elemento:
            print('> ' + subelemento.text) #valores -> text
            if subelemento.tag == 'nombre':
                nombre = subelemento.text
            if subelemento.tag == 'filas':
                filas = subelemento.text
            if subelemento.tag == 'columnas':
                columnas = subelemento.text
            if subelemento.tag == 'imagen':
                imagen = subelemento.text
     analizarImagen(imagen)
     lista.insertar(nombre,filas,columnas,imagen)        
 
    
    #lista.mostrarMatriz()
    n = matriz()
    n.insertar(1,1,"carlos")
    n.insertar(1,2,"asd")
    n.insertar(1,3,"caca")
    n.insertar(2,2,"pedro")
    n.insertar(2,1,"richar")
    n.insertar(8,8,"Agustin")
    #n.recorrerFilas()
    #n.recorrerColumnas()

def analizarImagen(imagen):
         print("imprimiendo imagen "+ imagen)
         contador = 0
         for n in imagen:
            if(n == ' '):
                print('espacion en blanco encontrado')
            if(n == '*'):
             print('asterisco encontrado')
            if(n == '-'):
             print('cosooooooo encontrado')
                   
    


# Configuración de la raíz
root = Tk()

menubar = Menu(root)
root.config(menu=menubar)

ancho_ventana = 900
alto_ventana = 500

x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
root.geometry(posicion)

root.resizable(0,0)
root.title("Ventana de ejemplo")

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Cargar Archivo", command=abrir)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar")

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")

menubar.add_cascade(label="Cargar Archivo", menu=filemenu, command=abrir)
menubar.add_cascade(label="Operaciones", menu=editmenu)
menubar.add_cascade(label="Reportes", menu=helpmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)



# Finalmente bucle de la aplicación
root.mainloop()