from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from functools import partial

def informacion_operarios(operario):
    listanodos=[1,2,3]
    root= Tk()

    root.title("Estudio de Tiempos: Ingresar Información de los Operarios")
    root.resizable(0,0)
    root.geometry("500x400")
    root.config(bg="white")

    titulo= Label(root,text="Estudio de Tiempos",foreground="black", background="white", font=("Times", 12, "italic") )
    titulo.place(x=365,y=3)

    titulo2= Label(root,text="Ingresar Información de Operarios",foreground="black", background="white", font=("Times", 12, 'bold') )
    titulo2.pack(pady=35)

    T = Text(root, height = 3, width = 70, font=("Times", 9, "italic"), relief='flat')
    mensaje='Para  que  sea  posible  el  cálculo  del  estudio  de  tiempos,  es  necesario  que  ingrese la siguiente información para cada operario. El  programa  se  encargará  de  guiarlo  para el ingreso de esta.'
    T.insert(END, mensaje)
    T.place(x=38, y=70)
    
    titulo3= Label(root,text="Infomación del operario: ",foreground="black", background="white", font=("Times", 10, 'bold') )
    titulo3.place(x=38,y=125)

    titulo3a= Label(root,text=operario,foreground="black", background="white", font=("Times", 10, 'bold') )
    titulo3a.place(x=188,y=125)
    """
    genlabel=Label(root,text="Género",foreground="black", background="white", font=("Times", 11))
    genlabel.place(x=248,y=250)

    flabel=Label(root,text="¿Trabaja de pie?",foreground="black", background="white", font=("Times", 11))
    unlabel.place(x=248,y=250)

    unlabel=Label(root,text="unidades",foreground="black", background="white", font=("Times", 11))
    unlabel.place(x=248,y=250)
    """
    root.mainloop()

informacion_operarios(1)


    

