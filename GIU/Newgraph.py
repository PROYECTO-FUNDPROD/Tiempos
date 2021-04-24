from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from functools import partial

def imprimir():
    print("botton")

def segundaVentana():
    root= Tk()

    root.title("Estudio de Tiempos")
    root.resizable(0,0)
    root.geometry("1100x600")
    root.config(bg="white")

    titulo= Label(root,text="Estudio de Tiempos",foreground="black", background="white", font=("Times", 12, "italic") )
    titulo.place(x=1000,y=3)

    titulo2= Label(root,text="Dibujar Grafo",foreground="black", background="white", font=("Times", 18) )
    titulo2.pack(side=TOP, pady=10)

    Dibujo= Label(root,text="AquiDibujamos",foreground="black", background="white",font=("Times", 18), width=60, height=13,borderwidth="2", relief="solid")
    Dibujo.pack(side=TOP, pady=6)

    Bnp=Button(root,text="Añadir Proceso",command=ingresar_proceso, font=("Times", 13),height=1)
    Bnp.place(x=155,y=420)

    Bep=Button(root,text="Eliminar Proceso",command=imprimir, font=("Times", 13), height=1)
    Bep.place(x=275,y=420)

    Bbt=Button(root,text="Modificar",command=imprimir, font=("Times", 13),height=1)
    Bbt.place(x=410,y=420)

    Bbt=Button(root,text="Borrar Todo",command=imprimir, font=("Times", 13),height=1)
    Bbt.place(x=410,y=420)

    Bdib=Button(root,text="Dibujar",command=imprimir, font=("Times", 13), height=1)
    Bdib.place(x=879,y=420)

    Bcalc=Button(root,text="Siguiente",command=imprimir, font=("Times", 16), fg='red', height=2, width=16)
    Bcalc.pack(side=BOTTOM, pady=50)

    #mb.showinfo("Información", "Este programa fue desarrollado para el aprendizaje de Python y tkinter.")
def ingresar_proceso():
    listanodos=[1,2,3]
    root= Tk()

    root.title("Estudio de Tiempos: Ingresar Proceso")
    root.resizable(0,0)
    root.geometry("600x300")
    root.config(bg="white")

    titulo= Label(root,text="Estudio de Tiempos",foreground="black", background="white", font=("Times", 12, "italic") )
    titulo.place(x=10,y=3)

    titulo2= Label(root,text="Ingresar Información del Proceso",foreground="black", background="white", font=("Times", 12, "italic") )
    titulo2.place(x=10,y=3)


    nlabel=Label(root,text="Nombre:",foreground="black", background="white", font=("Times", 11))
    nlabel.pack()

    nombre=Entry(root)
    nombre.pack()

    prelabel=Label(root,text="Predecesor:",foreground="black", background="white", font=("Times", 11))
    prelabel.pack()

    predecesor= ttk.Combobox(root,values=listanodos)
    predecesor.pack()

    dlabel=Label(root,text="Descripción:",foreground="black", background="white", font=("Times", 11))
    dlabel.pack()

    descripcion= ttk.Combobox(root, text="Descripción",values=["Manual", "Automático"])
    descripcion.pack()

    freclabel=Label(root,text="Frecuencia:  Cada",foreground="black", background="white", font=("Times", 11))
    freclabel.pack()

    spin = Spinbox(root, from_= 0, to = 100)  
    spin.pack()

    unlabel=Label(root,text="unidades",foreground="black", background="white", font=("Times", 11))
    unlabel.pack()

    Bacep=Button(root,text="Aceptar",command=imprimir, font=("Times", 13), height=1)
    Bacep.place(x=879,y=420)

    Bcan=Button(root,text="Cancelar",command=imprimir, font=("Times", 13), height=1)
    Bcan.place(x=879,y=420)







