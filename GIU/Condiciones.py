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

    T = Text(root, height = 0, width = 70, font=("Times", 11), relief='flat')
    mensaje="Por favor complete la siguiente información: "
    T.insert(END, mensaje)
    T.place(x=35, y=75)

    Alabel=Label(root,text="Trabajo de pie:",foreground="black", background="white", font=("Times", 11),)
    Alabel.place(x=35,y=115)

    A= ttk.Combobox(root,values=['Sí','No'],width= 15)
    A.place(x=140,y=115)

    Blabel=Label(root,text="Postura:",foreground="black", background="white", font=("Times", 11))
    Blabel.place(x=35,y=150)

    B= ttk.Combobox(root,values=['Cómoda', 'Ligeramente incómoda','Incómoda','Muy incómoda'],width= 18)
    B.place(x=140,y=150)
    
    Clabel=Label(root,text="Uso de fuerza",foreground="black", background="white", font=("Times", 11))
    Clabel.place(x=35,y=185)

    T1 = Text(root, height = 2, width = 70, font=("Times", 10,'italic'), relief='flat')
    mensaje1="? Peso (Kg) levantado, tirado o \n empujado por kilogramo "
    T1.insert(END, mensaje1)
    T1.place(x=305, y=178)

    cspin = Spinbox(root, from_= 0, to = 50)  
    cspin.place(x=140,y=185)
    '''
    Dlabel=Label(root,text="Iluminación:",foreground="black", background="white", font=("Times", 11),)
    Dlabel.place(x=70,y=150)

    D= ttk.Combobox(root,values=["Suficiente', 'Ligeramente baja",'Bastante baja','Absolutamente insuficiente'],width= 18)
    D.place(x=170,y=150)

    Elabel=Label(root,text="Condiciones Atmosféricas:",foreground="black", background="white", font=("Times", 11))
    Elabel.place(x=70,y=200)

    T2 = Text(root, height = 0, width = 70, font=("Times", 10), relief='flat')
    mensaje2="Calor humedad medido en Kata (milicalorías/cm^2/segundos)"
    T2.insert(END, mensaje2)
    T2.place(x=35, y=75)

    espin = Spinbox(root, from_= 0, to = 20)  
    espin.place(x=211,y=250)

    Flabel=Label(root,text="Concentración necesaria: ",foreground="black", background="white", font=("Times", 11),)
    Flabel.place(x=70,y=150)

    F= ttk.Combobox(root,values=['Cierta precisión','Precisión o fatigoso','Gran precisión o muy fatigoso'],width= 18)
    F.place(x=170,y=150)

    Glabel=Label(root,text="Ruido: ",foreground="black", background="white", font=("Times", 11))
    Glabel.place(x=70,y=200)

    G= ttk.Combobox(root,values=["Contínuo", "Intermitente y fuerte","Intermitente y muy fuerte", "Estridente y fuerte"],width= 18)
    G.place(x=170,y=200)

    Hlabel=Label(root,text="Tensión mental:",foreground="black", background="white", font=("Times", 11),)
    Hlabel.place(x=70,y=150)

    H= ttk.Combobox(root,values=['No complejo','Complejo','Bastante complejo','Muy complejo'],width= 18)
    H.place(x=170,y=150)

    Ilabel=Label(root,text="Monotonía: ",foreground="black", background="white", font=("Times", 11))
    Ilabel.place(x=70,y=200)

    I= ttk.Combobox(root,values=["No monótono', 'Algo monótono",'Bastante monótono', 'Muy monótono'],width= 18)
    I.place(x=170,y=200)

    Jlabel=Label(root,text="Tedio:",foreground="black", background="white", font=("Times", 11),)
    Jlabel.place(x=70,y=150)

    J=ttk.Combobox(root,values=['No aburrido','Aburrido','Bastante aburrido','Muy aburrido'],width= 18)
    J.place(x=170,y=150)
    '''

    
    root.mainloop()
condiciones_laborales()

    