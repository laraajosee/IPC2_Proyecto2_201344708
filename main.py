from os import name
from tkinter import *
from tkinter.filedialog import askopenfilename
import xml.etree.ElementTree as ET
from matriz import matriz
from lista import ListaEnlazada
from ListaReporte import ListaReporte
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
from datetime import datetime
import webbrowser

now = datetime.now()
listaReporte = ListaReporte()
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

     print(comboExample.get())
     imagen = PhotoImage(file=comboExample.get()+".gv.png")
     
     #imagen_zoom=imagen.zoom(2)
     etiqueta1.config(image=imagen)
     ventana.mainloop()

def RotacionTranspuesta():
    n = matriz()
    ContadorFilas = 1
    contadorColumnas = 1
    print("rotando Imagen")
    nodo = lista.getNodo(comboExample.get())
    filas = lista.getFilas(comboExample.get())
    columnas = lista.getColumnas(comboExample.get())
    print("el numero de filas es: " +str(filas))
    print("el numero de columnas es: " +str(columnas))
    
    NuevaImagen = nodo.imagen.rotacion()
    print(NuevaImagen)
    #contadorRotacion = int(filas)
    
    
    for k in NuevaImagen:
        if(k == '*'):
            n.insertar(ContadorFilas,contadorColumnas,'*')
            ContadorFilas = ContadorFilas +1 
            #fila 1, columna 1 || fila 2, columna 1
        if(k == '-'):
            n.insertar(ContadorFilas,contadorColumnas,'-')
            ContadorFilas = ContadorFilas +1 
        if(k == '\n'):
         ContadorFilas = 1
         contadorColumnas =  contadorColumnas + 1
    #n.recorrerFilas()
    
    nombre = comboExample.get()+"RotadaTranspuesta"
    nodo = lista.insertarFinal(nombre,contadorColumnas,filas,n)
    nodo.imagen = n  
    listaCombo.append(comboExample.get()+'RotadaTranspuesta')    

    lista.crearImagen()
    listaReporte.insertar("Se roto la imagen de manera Traspuesta \n"+"Nombre de la matriz: "+comboExample.get()+"\nA la hora: "+
    str(now.date())+ " "+ str(now.time()))
    listaReporte.mostrar()

def RotacionVertical():
    n = matriz()
   
    print("rotando Imagen")
    nodo = lista.getNodo(comboExample.get())
    columnas = lista.getColumnas(comboExample.get())
    print("el numero de columnas es: " +str(columnas))
    
    NuevaImagen = nodo.imagen.rotacion()
    print(NuevaImagen)
    contadorFilas = 1
    contadorColumnas = columnas
    
    
    for k in NuevaImagen:
        if(k == '*'):
            n.insertar(contadorFilas,contadorColumnas,'*')
            contadorColumnas = contadorColumnas - 1 
        if(k == '-'):
            n.insertar(contadorFilas,contadorColumnas,'-')
            contadorColumnas = contadorColumnas - 1 
        if(k == '\n'):
         contadorFilas = contadorFilas + 1
   
         contadorColumnas = columnas
    #n.recorrerFilas()
    
    nombre = comboExample.get()+"RotadaVertical"
    nodo = lista.insertarFinal(nombre,contadorColumnas,contadorFilas,n)
    nodo.imagen = n  
    listaCombo.append(comboExample.get()+'RotadaVertical')    

    lista.crearImagen()
    listaReporte.insertar("Se roto la imagen de manera Vertical \n"+"Nombre de la matriz: "+comboExample.get()+"\nA la hora: "+
    str(now.date())+ " "+ str(now.time()))
    listaReporte.mostrar()


def LimpiarArea():
    n = matriz()
    LimparFila1= 0
    LimpiarFila2 =  0
    LimpiarColumna1 = 0
    LimpiarColumna2 = 0
    LimparFila1 = CordenadaFila1.get("1.0","end")
    LimpiarFila2 = CordenadaFila2.get("1.0","end")
    LimpiarColumna1 = CordenadaColumna1.get("1.0","end")
    LimpiarColumna2 = CordenadaColumna2.get("1.0","end")

    fila1 = int(LimparFila1) 
    fila2 = int(LimpiarFila2) 
    columna1= int(LimpiarColumna1) 
    columna2 =int(LimpiarColumna2) 

    print(str(LimparFila1))
    print(str(LimpiarFila2))
    print(str(LimpiarColumna1))
    print(str(LimpiarColumna2))

    ContadorFilas = 1
    ContadorColumnas = 1

    nodo = lista.getNodo(comboExample.get())
    NuevaImagen = nodo.imagen.rotacion()
    print(NuevaImagen)

    for k in NuevaImagen:
        if(k == '*'):
            if((ContadorFilas >= fila1 and ContadorFilas <= fila2) and(ContadorColumnas >= columna1 and ContadorColumnas <= columna2) ):
                #print("FIlas: "+ str(ContadorFilas))
                #print("Limpiar columna: "+ str(ContadorColumnas))
                n.insertar(ContadorFilas,ContadorColumnas,'-')
                ContadorColumnas = ContadorColumnas +1
            else: 
                n.insertar(ContadorFilas,ContadorColumnas,'*')
                ContadorColumnas = ContadorColumnas +1
        if(k == '-'):
            n.insertar(ContadorFilas,ContadorColumnas,'-')
            ContadorColumnas = ContadorColumnas +1 
        if(k == '\n'):
         ContadorFilas = ContadorFilas + 1
   
         ContadorColumnas = 1
    #n.recorrerFilas()
    
    nombre = comboExample.get()+"Borrada"
    nodo = lista.insertarFinal(nombre,ContadorFilas,ContadorColumnas,n)
    nodo.imagen = n  
    listaCombo.append(comboExample.get()+'Borrada')  
    

    lista.crearImagen()
    listaReporte.insertar("Se limpio el area de "+"fila 1: "+ CordenadaFila1.get("1.0","end")+ 
                                                  "columna 1: "+ CordenadaColumna1.get("1.0","end")+
                                                  "fila 2: "+ CordenadaFila2.get("1.0","end")+
                                                  "columna 2: "+ CordenadaColumna2.get("1.0","end")+
    "\n"+"Nombre de la matriz: "+comboExample.get()+"\nA la hora: "+
    str(now.date())+ " "+ str(now.time()))
    listaReporte.mostrar()


def pulsar():
    n = matriz()
    contadorColumnas = 1
    print("rotando Imagen")
    nodo = lista.getNodo(comboExample.get())
    filas = lista.getFilas(comboExample.get())
    print("el numero de filas es: " +str(filas))
    
    NuevaImagen = nodo.imagen.rotacion()
    print(NuevaImagen)
    contadorRotacion = int(filas)
    
    for k in NuevaImagen:
        if(k == '*'):
            n.insertar(contadorRotacion,contadorColumnas,'*')
            contadorColumnas = contadorColumnas +1 
        if(k == '-'):
            n.insertar(contadorRotacion,contadorColumnas,'-')
        
            contadorColumnas = contadorColumnas +1 
        if(k == '\n'):
         contadorRotacion = contadorRotacion - 1
   
         contadorColumnas = 1
    #n.recorrerFilas()
    
    nombre = comboExample.get()+"RotadaHorizontal"
    nodo = lista.insertarFinal(nombre,contadorColumnas,filas,n)
    nodo.imagen = n  
    listaCombo.append(comboExample.get()+'RotadaHorizontal')    

    lista.crearImagen()
    listaReporte.insertar("Se roto la imagen de manera Horizontal \n"+"Nombre de la matriz: "+comboExample.get()+"\nA la hora: "+
    str(now.date())+ " "+ str(now.time()))
    listaReporte.mostrar()
  
def LineaHorizontal():
    n = matriz()
    LimparFila1= 0
    LimpiarFila2 =  0
    LimpiarColumna1 = 0
    LimpiarColumna2 = 0
    EElementos = 0
    LimparFila1 = CordenadaFila1.get("1.0","end")
    #LimpiarFila2 = CordenadaFila2.get("1.0","end")
    LimpiarColumna1 = CordenadaColumna1.get("1.0","end")
    #LimpiarColumna2 = CordenadaColumna2.get("1.0","end")
    EElementos = Elementos.get("1.0","end")

    ContadorColumnas = 1
    ContadorFilas  = 1

    fila1 = int(LimparFila1) 
    #fila2 = int(LimpiarFila2) 
    columna1= int(LimpiarColumna1) 
    #columna2 =int(LimpiarColumna2) 
    elementos = int(EElementos)

    nodo = lista.getNodo(comboExample.get())
    NuevaImagen = nodo.imagen.rotacion()
    print(NuevaImagen)

    for k in NuevaImagen:
        if(k == '*'):
            if(fila1 == ContadorFilas and (ContadorColumnas >= columna1 and ContadorColumnas <= elementos)):
                #print("contador FIla: "+ str(ContadorFilas) +" Contador Columnas: "+ str(ContadorColumnas))
                n.insertar(ContadorFilas,ContadorColumnas,'*')
                ContadorColumnas = ContadorColumnas + 1
               
            else:
                n.insertar(ContadorFilas,ContadorColumnas,'*')
                ContadorColumnas = ContadorColumnas +1 
            #n.insertar(contadorRotacion,contadorColumnas,'*')    
        if(k == '-'):
            if(fila1 == ContadorFilas and (ContadorColumnas >= columna1 and ContadorColumnas <= elementos)):
                #print("contador FIla: "+ str(ContadorFilas) +" Contador Columnas: "+ str(ContadorColumnas))
                n.insertar(ContadorFilas,ContadorColumnas,'*')
                ContadorColumnas = ContadorColumnas + 1
            else:
                n.insertar(ContadorFilas,ContadorColumnas,'-')
                ContadorColumnas = ContadorColumnas +1 
               
        if(k == '\n'):
         ContadorFilas = ContadorFilas + 1
   
         ContadorColumnas = 1
    nombre = comboExample.get()+"LHorizontal"
    nodo = lista.insertarFinal(nombre,ContadorFilas,ContadorColumnas,n)
    nodo.imagen = n  
    listaCombo.append(comboExample.get()+'LHorizontal')  
    

    lista.crearImagen()
    listaReporte.insertar("Se agrego una linea horizontal en:  "+"fila : "+ CordenadaFila1.get("1.0","end")+ 
                                                  "columna : "+ CordenadaColumna1.get("1.0","end")+
                                                  "Numero De elementos: "+ Elementos.get("1.0","end")+
    "\n"+" Nombre de la matriz: "+comboExample.get()+"\nA la hora: "+
    str(now.date())+ " "+ str(now.time()))
    listaReporte.mostrar()

def LineaVertical():
    n = matriz()
    LimparFila1= 0
    LimpiarFila2 =  0
    LimpiarColumna1 = 0
    LimpiarColumna2 = 0
    EElementos = 0
    LimparFila1 = CordenadaFila1.get("1.0","end")
    #LimpiarFila2 = CordenadaFila2.get("1.0","end")
    LimpiarColumna1 = CordenadaColumna1.get("1.0","end")
    #LimpiarColumna2 = CordenadaColumna2.get("1.0","end")
    EElementos = Elementos.get("1.0","end")

    ContadorColumnas = 1
    ContadorFilas  = 1

    fila1 = int(LimparFila1) 
    #fila2 = int(LimpiarFila2) 
    columna1= int(LimpiarColumna1) 
    #columna2 =int(LimpiarColumna2) 
    elementos = int(EElementos)

    nodo = lista.getNodo(comboExample.get())
    NuevaImagen = nodo.imagen.rotacion()
    print(NuevaImagen)

    for k in NuevaImagen:
        if(k == '*'):
            if((ContadorFilas >= fila1 and ContadorFilas <= elementos) and ContadorColumnas == columna1):
                print("contador FIla: "+ str(ContadorFilas) +" Contador Columnas: "+ str(ContadorColumnas))
                n.insertar(ContadorFilas,ContadorColumnas,'*')
                ContadorColumnas = ContadorColumnas + 1  
            else:
                n.insertar(ContadorFilas,ContadorColumnas,'*')
                ContadorColumnas = ContadorColumnas +1 
             
        if(k == '-'):
            if((ContadorFilas >= fila1 and ContadorFilas <= elementos) and ContadorColumnas == columna1):
                print("contador FIla: "+ str(ContadorFilas) +" Contador Columnas: "+ str(ContadorColumnas))
                n.insertar(ContadorFilas,ContadorColumnas,'*')
                ContadorColumnas = ContadorColumnas + 1
            else:
                n.insertar(ContadorFilas,ContadorColumnas,'-')
                ContadorColumnas = ContadorColumnas +1 
               
        if(k == '\n'):
         ContadorFilas = ContadorFilas + 1
   
         ContadorColumnas = 1
    nombre = comboExample.get()+"LVertical"
    nodo = lista.insertarFinal(nombre,ContadorFilas,ContadorColumnas,n)
    nodo.imagen = n  
    listaCombo.append(comboExample.get()+'Lvertical')  
    

    lista.crearImagen()
    listaReporte.insertar("Se agrego una linea Vertical en:  "+"fila : "+ CordenadaFila1.get("1.0","end")+ 
                                                  "columna : "+ CordenadaColumna1.get("1.0","end")+
                                                  "Numero De elementos: "+ Elementos.get("1.0","end")+
    "\n"+" Nombre de la matriz: "+comboExample.get()+"\n A la hora: "+
    str(now.date())+ " "+ str(now.time()))
    listaReporte.mostrar()
    


def CargarReporte():
    webbrowser.open_new_tab('Reporte.html') 


def callbackFunc1(event):
    print("callbackFunc1")
ventana=Tk()
#ventana.geometry('800x500')
ancho_ventana = 1200
alto_ventana = 650
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
boton.place(x=50,y=475)

botonRotacion=Button(ventana,text='Rotacion Vertical',command=RotacionVertical)
botonRotacion.place(x=200,y=475)

botonTranspuesta=Button(ventana,text='Rotacion Traspuesta',command=RotacionTranspuesta)
botonTranspuesta.place(x=350,y=475)

botonLimpiar=Button(ventana,text='Limpiar Area',command=LimpiarArea)
botonLimpiar.place(x=500,y=475)

botonHorizontal=Button(ventana,text='Linea Horizontal',command=LineaHorizontal)
botonHorizontal.place(x=500,y=500)

botonLimpiar=Button(ventana,text='Linea Vertical',command=LineaVertical)
botonLimpiar.place(x=500,y=525)

botonLimpiar=Button(ventana,text='Agregar Triangulo',command=RotacionTranspuesta)
botonLimpiar.place(x=500,y=550)



CordenadaFila1=tk.Text(ventana, height=1.4,widt=7)
CordenadaFila1.place(x=730, y=475)
CordenadaFila1.insert("insert", "Fila")

CordenadaColumna1=tk.Text(ventana, height=1.4,widt=7)
CordenadaColumna1.place(x=780, y=475)
CordenadaColumna1.insert("insert", "Columna")

CordenadaFila2=tk.Text(ventana, height=1.4,widt=7)
CordenadaFila2.place(x=730, y=500)
CordenadaFila2.insert("insert", "Fila")

CordenadaColumna2=tk.Text(ventana, height=1.4,widt=7)
CordenadaColumna2.place(x=780, y=500)
CordenadaColumna2.insert("insert", "Columna")

Elementos=tk.Text(ventana, height=1.4,widt=9)
Elementos.place(x=845, y=500)
Elementos.insert("insert", "Elementos")

lblCordenada1=Label(ventana,text='Primera Cordenada')
lblCordenada1.place(x=600,y=475)
lblCordenada1.config(padx=10,pady=4)

lblCordenada2=Label(ventana,text='Segunda Cordenada')
lblCordenada2.place(x=600,y=500)
lblCordenada2.config(padx=10,pady=4)

menubar = Menu(ventana)
ventana.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
filemenu1 = Menu(menubar, tearoff=0)
filemenu2 = Menu(menubar, tearoff=0)

filemenu.add_command(label="Cargar Archivo", command=abrir)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=ventana.quit)

filemenu1.add_command(label="Cargar Reporte", command=CargarReporte)
filemenu2.add_command(label="Datos del Estudiante", command=CargarReporte)
filemenu2.add_command(label="Documentacion", command=CargarReporte)


menubar.add_cascade(label="Cargar Archivo", menu=filemenu, command=abrir)
menubar.add_cascade(label="Reporte", menu=filemenu1, command=abrir)
menubar.add_cascade(label="Ayuda", menu=filemenu2, command=abrir)

comboExample = ttk.Combobox(ventana, 
                            values=["hola"],postcommand=changeMonth)
comboExample.place(x=50,y=100)
comboExample.current()
comboExample.bind("<<ComboboxSelected>>", callbackFunc)




ventana.mainloop()