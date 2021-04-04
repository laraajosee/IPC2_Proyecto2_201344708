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
     n = matriz()
       # print(elemento.tag) #tag
     for subelemento in elemento:
            #print('> ' + subelemento.text) #valores -> text
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
                   
                    
     
     nodo = lista.insertarFinal(nombre,filas,columnas,n)
     nodo.imagen = n  
     listaCombo.append(nombre)
        
     
     
   
    #lista.mostrarMatriz()
    lista.crearImagen()

def changeMonth():
    comboExample["values"] = listaCombo
                                   

def callbackFunc(event):
     nodo = lista.getNodo(comboExample.get())
     print("imprimiento pulsar")
     nodo.imagen.recorrerFilas()
     print(comboExample.get())
     imagen = PhotoImage(file=comboExample.get()+".gv.png")
     
     #imagen_zoom=imagen.zoom(2)
     etiqueta1.config(image=imagen)
     ventana.mainloop()

def pulsar():
    print("rotando Imagen")
    imagen = PhotoImage(file="M4.gv.png")
    etiqueta1.config(image=imagen)
    ventana.mainloop()

ventana=Tk()
#ventana.geometry('800x500')
ancho_ventana = 1200
alto_ventana = 800
x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)
ventana.resizable(0,0)


etiqueta1=Label(ventana,text='imagen1',bg="green")
etiqueta1.place(x=50,y=130)
etiqueta1.config(padx=125,pady=125)

etiqueta2=Label(ventana,text='imagen2',bg="green")
etiqueta2.place(x=450,y=130)
etiqueta2.config(padx=125,pady=125)


boton=Button(ventana,text='Rotacion Horizontal',command=pulsar)
boton.place(x=50,y=525)

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