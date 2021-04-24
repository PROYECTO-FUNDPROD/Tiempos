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
    root.geometry("650x400")
    root.config(bg="white")
    labelP=Label(root,text="Procesos",foreground="black", background="white", font=("Times", 11))
    labelP.place(x=15,y=105)
    predecesor= ttk.Combobox(root,values=listanodos,width= 15)
    predecesor.place(x=140,y=105)
    titulo= Label(root,text="Estudio de Tiempos",foreground="black", background="white", font=("Times", 12, "italic") )
    titulo.place(x=490,y=3)
    tituloV= Label(root,text=tituloVentana,foreground="black", background="white", font=("Times", 15, "bold") )
    tituloV.place(x=255,y=30)
    mensajeV= Label(root,text=mensajeVentana,foreground="black", background="white", font=("Times", 12) )
    mensajeV.place(x=15,y=140)
    frameTwo = Frame(bg="white")
    
    canvas=Canvas(frameTwo,bg="white",width=600,height=200)
    canvas.pack(side="left")
    

    scrollb=ttk.Scrollbar( frameTwo, orient="vertical",command=canvas.yview)
    scrollb.pack(side="right",fill="y")
    canvas.configure(yscrollcommand=scrollb.set) 
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion = canvas.bbox("all")))




    listFrame=Frame(canvas,background="white")
    canvas.create_window((0,0),window=listFrame, anchor="nw")
    
    
    #scrollb.grid_forget()    
    frameTwo.pack(side="bottom",pady=30)
    num_piezas = 5
    optionmenus_piezas = list()
    numpiezas = []
    numerolotes = []
    optionmenus_prioridad = list()
    lotes = list()
    mispiezas = ['One', 'Two', 'Three', 'Four', 'Five']
    n = 1
    textotamano = Label(listFrame, text = "", justify="left",bg="white")
    textotamano.pack(ipadx=322)
    while n <= num_piezas:
        
        textopieza = Label(listFrame, text = "Pieza: "+str(n), justify="left",bg="white")
        textopieza.pack(side="top",padx=20)
        var = StringVar()
        if(tipo=="personas"):
            llenar=Spinbox(listFrame, from_= 0, to = 150)  
        else:
            llenar = OptionMenu(listFrame, var, *mispiezas)
        
        llenar.config(width=10,bg="white")
        llenar.pack(side="top",padx=5)
        var.set("One"+str(n))


        n += 1
    

    
    root.mainloop()
    
ventana("Eliminar proceso", "A continuación debera modificar los procesos que quedaran sin antecesor","procesos")