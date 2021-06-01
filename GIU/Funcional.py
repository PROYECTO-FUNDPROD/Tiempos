from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from functools import partial

def imprimir():
    print("botton")



def ventana(tituloVentana, mensajeVentana,tipo):
    listanodos=[1,2,3]
    root= Tk()
    root.title("Estudio de Tiempos")
    root.resizable(0,0)
    root.geometry("400x400")
    root.config(bg="white")
    labelP=Label(root,text=tipo,foreground="black", background="white", font=("Times", 11))
    labelP.place(x=15,y=85)
    predecesor= ttk.Combobox(root,values=listanodos,width= 15)
    predecesor.place(x=140,y=85)
    titulo= Label(root,text="Estudio de Tiempos",foreground="black", background="white", font=("Times", 12, "italic") )
    titulo.place(x=265,y=3)
    tituloV= Label(root,text=tituloVentana,foreground="black", background="white", font=("Times", 15, "bold") )
    tituloV.pack(pady=30)
    mensajeV= Label(root,text=mensajeVentana,foreground="black", background="white", font=("Times", 12), justify="left" )
    mensajeV.place(x=15,y=120)
    Bacep=Button(root,text="Aceptar",command= imprimir, font=("Times", 13), height=1, )
    Bacep.place(x=320,y=340)

    frameTwo = Frame(bg="white")
    canvas=Canvas(frameTwo,bg="white",width=350,height=200)
    canvas.pack(side="left")

    scrollb=ttk.Scrollbar( frameTwo, orient="vertical",command=canvas.yview)
    scrollb.pack(side="right",fill="y")
    canvas.configure(yscrollcommand=scrollb.set) 
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion = canvas.bbox("all")))


    listFrame=Frame(canvas,background="white")
    canvas.create_window((0,0),window=listFrame, width= 350, height= 150, anchor="center")

    
    #scrollb.grid_forget()    
    frameTwo.pack(side="top",pady=85)
    num_piezas = len(listanodos)
    
    n = 1
    
    while n <= num_piezas:        
        textopieza = Label(listFrame, text = "Proceso: "+str(n), justify="left",bg="white")
        textopieza.pack(ipady=0, ipadx=10)
        var = StringVar()
        if(tipo=="personas"):
            llenar=Spinbox(listFrame, from_= 0, to = 150)  
        else:
            llenar =ttk.Combobox(listFrame, values=listanodos, width=15)

        llenar.pack(side= "top", padx=100)
        n += 1

    

    ventana("Eliminar proceso", "A continuación debera modificar los procesos que\nquedarán sin antecesor","procesos")