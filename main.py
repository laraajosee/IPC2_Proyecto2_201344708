from tkinter import *
from tkinter.filedialog import askopenfilename
import xml.etree.ElementTree as ET

def abrir():

    filename = askopenfilename()
    tree = ET.parse(filename)
    root = tree.getroot()

    
  
    for elemento in root: 
        for subelemento in elemento:
            if(subelemento.tag == 'nombre'):
                print(subelemento.tag)
         
         
         
                   
    


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