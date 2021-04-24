from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from functools import partial

def condiciones_laborales():
    listanodos=[1,2,3]
    root= Tk()

    root.title("Estudio de Tiempos: Ingresar Información de los Operarios")
    root.resizable(0,0)
    root.geometry("500x400")
    root.config(bg="white")

    titulo= Label(root,text="Estudio de Tiempos",foreground="black", background="white", font=("Times", 12, "italic") )
    titulo.place(x=365,y=3)

    titulo2= Label(root,text="Ingresar Condiciones Laborales",foreground="black", background="white", font=("Times", 12, 'bold') )
    titulo2.pack(pady=35)

    T = Text(root, height = 0, width = 70, font=("Times", 10), relief='flat')
    mensaje="Por favor complete la siguiente información: "
    T.insert(END, mensaje)
    T.place(x=35, y=75)

    Alabel=Label(root,text="Trabajo de pie",foreground="black", background="white", font=("Times", 11),)
    Alabel.place(x=70,y=150)

    A= ttk.Combobox(root,values=listanodos,width= 18)
    A.place(x=170,y=150)

    Blabel=Label(root,text="Postura",foreground="black", background="white", font=("Times", 11))
    Blabel.place(x=70,y=200)

    B= ttk.Combobox(root,values=listanodos,width= 18)
    B.place(x=170,y=150)

    Clabel=Label(root,text="Uso de fuerza",foreground="black", background="white", font=("Times", 11))
    Clabel.place(x=70,y=200)

    C= ttk.Combobox(root,values=["Manual", "Automático"],width= 18)
    C.place(x=170,y=200)

    Dlabel=Label(root,text="Iluminación:",foreground="black", background="white", font=("Times", 11),)
    Dlabel.place(x=70,y=150)

    D= ttk.Combobox(root,values=listanodos,width= 18)
    D.place(x=170,y=150)

    Elabel=Label(root,text="Condiciones Atmosféricas:",foreground="black", background="white", font=("Times", 11))
    Elabel.place(x=70,y=200)

    E= ttk.Combobox(root,values=["Manual", "Automático"],width= 18)
    E.place(x=170,y=200)

    Flabel=Label(root,text="Concentración necesaria: ",foreground="black", background="white", font=("Times", 11),)
    Flabel.place(x=70,y=150)

    F= ttk.Combobox(root,values=listanodos,width= 18)
    F.place(x=170,y=150)

    Glabel=Label(root,text="Ruido: ",foreground="black", background="white", font=("Times", 11))
    Glabel.place(x=70,y=200)

    G= ttk.Combobox(root,values=["Manual", "Automático"],width= 18)
    G.place(x=170,y=200)

    Hlabel=Label(root,text="Tensión mental:",foreground="black", background="white", font=("Times", 11),)
    Hlabel.place(x=70,y=150)

    H= ttk.Combobox(root,values=listanodos,width= 18)
    H.place(x=170,y=150)

    Ilabel=Label(root,text="Monotonía: ",foreground="black", background="white", font=("Times", 11))
    Ilabel.place(x=70,y=200)

    I= ttk.Combobox(root,values=["Manual", "Automático"],width= 18)
    I.place(x=170,y=200)

    Jlabel=Label(root,text="Tedio:",foreground="black", background="white", font=("Times", 11),)
    Jlabel.place(x=70,y=150)

    J=ttk.Combobox(root,values=listanodos,width= 18)
    J.place(x=170,y=150)


    
    root.mainloop()
condiciones_laborales()

    