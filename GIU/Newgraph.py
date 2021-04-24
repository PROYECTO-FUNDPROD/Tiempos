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
    titulo.place(x=960,y=3)

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
    root.geometry("500x300")
    root.config(bg="white")

    titulo= Label(root,text="Estudio de Tiempos",foreground="black", background="white", font=("Times", 12, "italic") )
    titulo.place(x=360,y=3)

    titulo2= Label(root,text="Ingresar Información del Proceso",foreground="black", background="white", font=("Times", 12) )
    titulo2.place(x=40,y=30)


    nlabel=Label(root,text="Nombre:",foreground="black", background="white", font=("Times", 11))
    nlabel.place(x=40,y=70)

    nombre=Entry(root,width= 15)
    nombre.place(x=140,y=70)

    prelabel=Label(root,text="Predecesor:",foreground="black", background="white", font=("Times", 11),)
    prelabel.place(x=40,y=120)

    predecesor= ttk.Combobox(root,values=listanodos,width= 15)
    predecesor.place(x=140,y=120)

    dlabel=Label(root,text="Descripción:",foreground="black", background="white", font=("Times", 11))
    dlabel.place(x=40,y=170)

    descripcion= ttk.Combobox(root, text="Descripción",values=["Manual", "Automático"],width= 15)
    descripcion.place(x=140,y=170)

    freclabel=Label(root,text="Frecuencia:  Cada",foreground="black", background="white", font=("Times", 11))
    freclabel.place(x=40,y=220)

    spin = Spinbox(root, from_= 0, to = 100, width=3)  
    spin.place(x=160,y=220)

    unlabel=Label(root,text="unidades",foreground="black", background="white", font=("Times", 11))
    unlabel.place(x=200,y=220)

    Bacep=Button(root,text="Aceptar",command=imprimir, font=("Times", 13), height=1)
    Bacep.place(x=260,y=260)

    Bcan=Button(root,text="Cancelar",command=imprimir, font=("Times", 13), height=1)
    Bcan.place(x=360,y=260)







