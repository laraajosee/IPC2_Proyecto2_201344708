from tkinter import *
from tkinter.filedialog import askopenfilename
import xml.etree.ElementTree as ET
from matriz import matriz
from lista import ListaEnlazada

lista = ListaEnlazada()
n = matriz()

  


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
                contadorColumnas = 0
                contadorFilas = 0
                for k in imagen:
                    if(k == '-'):
                        n.insertar(contadorFilas,contadorColumnas,'-')
                        contadorColumnas = contadorColumnas +1
                        
                    if(k == '*'):
                        n.insertar(contadorFilas,contadorColumnas,'*')
                        contadorColumnas = contadorColumnas +1
                        
                    if(k == '\n'):
                        contadorFilas = contadorFilas +1
                        contadorColumnas = 1
                       
                    
     
     nodo = lista.insertarFinal(nombre,filas,columnas,"")
     nodo.imagen = n        
 
    lista.mostrarMatriz() 
               
              


# Configuración de la raíz
raiz = Tk()
imagen = PhotoImage(file="prueva.png")
mi_Frame = Frame(raiz, width=1000, height=1000)
mi_Frame.pack()
#mi_Label = Label(mi_Frame, text="Metodo place")
#mi_Label.place(x=70, y=10)
label1 = Label(mi_Frame, text="hola",bg= "green")
label1.place(x=5, y=50)
label1.config(padx=125,pady=125)

label2 = Label(mi_Frame, text="hola",bg= "green")
label2.place(x=350, y=50)
label2.config(padx=100,pady=100)



mi_Entry = Entry(mi_Frame) #Creación de Entry
mi_Entry.place(x=150, y=10)



menubar = Menu(raiz)
raiz.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Cargar Archivo", command=abrir)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=raiz.quit)

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
ancho_ventana = 1500
alto_ventana = 800

x_ventana = raiz.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = raiz.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
raiz.geometry(posicion)

raiz.resizable(0,0)
raiz.title("Calculos Ortagonales")



raiz.mainloop()