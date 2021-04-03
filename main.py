from os import name
from tkinter import *
from tkinter.filedialog import askopenfilename
import xml.etree.ElementTree as ET
from matriz import matriz
from lista import ListaEnlazada
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo



lista = ListaEnlazada()

listaCombo = []

   

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
                n = matriz()
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
                   
                    
     
     lista.insertarFinal(nombre,filas,columnas,n)
     listaCombo.append(nombre)
     #nodo.imagen = n
     print("es la matriz que se esta guardando:")
     print(n.recorrerFilas())
        
     
     
          
    
   
    #lista.mostrarMatriz()
    #lista.crearImagen()

def changeMonth():
    comboExample["values"] = listaCombo
                                   

def callbackFunc(event):
     print("New Element Selected")
     print(comboExample.get())
     imagen = PhotoImage(file="M4.gv.png")
     #imagen_zoom=imagen.zoom(4)
     etiqueta1.config(image=imagen)
     ventana.mainloop()

def pulsar():
    #print('Hola',nombre.get())
    imagen = PhotoImage(file="M4.gv.png")
    etiqueta1.config(image=imagen)
    ventana.mainloop()

ventana=Tk()
#ventana.geometry('800x500')
ancho_ventana = 1500
alto_ventana = 800
x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)
ventana.resizable(0,0)

etiqueta=Label(ventana,text='Nombre:')
etiqueta.place(x=650,y=20)

etiqueta1=Label(ventana,text='imagen1',bg="green")
etiqueta1.place(x=50,y=130)
etiqueta1.config(padx=200,pady=200)
#imagen = PhotoImage(file="prueva.png")
#etiqueta1.config(image=imagen)

boton=Button(ventana,text='Actualizar',command=pulsar)
boton.place(x=20,y=700)

nombre=StringVar()
cajatexto=Entry(ventana,textvariable=nombre)
cajatexto.place(x=500,y=20)

menubar = Menu(ventana)
ventana.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Cargar Archivo", command=abrir)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=ventana.quit)

menubar.add_cascade(label="Cargar Archivo", menu=filemenu, command=abrir)

comboExample = ttk.Combobox(ventana, 
                            values=["hola"],postcommand=changeMonth)
comboExample.place(x=50,y=100)
comboExample.current()

comboExample.bind("<<ComboboxSelected>>", callbackFunc)


ventana.mainloop()