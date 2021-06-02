import sys
import os
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from functools import partial
import config
sys.path.insert(0, "App\View.py")
import App.View as vw

def imprimir():
    print("botton")


def addPredecesores():
    print("botton")
    for i in range (0, len(lista)):
        pre=lista[i].get()
        vw.agregarPredecesor(tarea,pre)

def dibujar():
    vw.dibujarGrafo()


def nuevoProceso(nombre,descripcion, frecuencia):
    if nombre=="" or descripcion=='' or frecuencia=='':
        titulo="Información Incompleta"
        mensaje= "Por favor complete todas las casillas de información para continuar"
        icono="error"
        mb.okMessageBox(titulo,mensaje,icono)
    else:
        global tarea
        tarea= vw.nueva_tarea(nombre,descripcion,frecuencia)
        tareas= vw.getTareasNombres()
        print(tareas)
        if len(tareas)>1:
            ingresar_proceso2("Añadir Predecesores", "A continuación debe ingresar los predecesores del Proceso {0}".format(nombre),"Cantidad de predecesores: ",tareas)
            

def cancelar(r):
    r.destroy()


def openWindow(tituloVentana, mensajeVentana,tipo):
    #r.destroy()
    tareas= vw.getTareasNombres()
    varios(tituloVentana, mensajeVentana,tipo, tareas)

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

    Bep=Button(root,text="Eliminar Proceso",command= lambda: openWindow("Eliminar Proceso", "A continuación deberá modificar los procesos que\nquedarán sin antecesor","Proceso: "), font=("Times", 13), height=1)
    Bep.place(x=275,y=420)

    Bbt=Button(root,text="Modificar Proceso",command=lambda: openWindow("Modificar Proceso", "A continuación podrá modificar los predecesores del proceso deseado","Proceso: "), font=("Times", 13),height=1)
    Bbt.place(x=410,y=420)

    Bbt=Button(root,text="Borrar Todo",command=imprimir, font=("Times", 13),height=1)
    Bbt.place(x=780,y=420)

    Bdib=Button(root,text="Dibujar",command=dibujar, font=("Times", 13), height=1)
    Bdib.place(x=879,y=420)

    Bcalc=Button(root,text="Siguiente",command=imprimir, font=("Times", 16), fg='red', height=2, width=16)
    Bcalc.pack(side=BOTTOM, pady=50)

    #mb.showinfo("Información", "Este programa fue desarrollado para el aprendizaje de Python y tkinter.")
def ingresar_proceso():
    listanodos=[1,2,3]
    nombre='A'
    root= Tk()

    root.title("Estudio de Tiempos: Ingresar Proceso")
    root.resizable(0,0)
    root.geometry("380x300")
    root.config(bg="white")

    titulo= Label(root,text="Estudio de Tiempos",foreground="black", background="white", font=("Times", 12, "italic") )
    titulo.place(x=245,y=3)

    titulo2= Label(root,text="Ingresar Información del Proceso",foreground="black", background="white", font=("Times", 12, 'bold') )
    titulo2.place(x=70,y=45)

    nlabel=Label(root,text="Nombre:",foreground="black", background="white", font=("Times", 11))
    nlabel.place(x=70,y=100)

    nombre=Entry(root,width= 21)
    nombre.place(x=170,y=100)

    dlabel=Label(root,text="Descripción:",foreground="black", background="white", font=("Times", 11))
    dlabel.place(x=70,y=150)

    descripcion= ttk.Combobox(root, text="Descripción",values=["Manual", "Automático"],width= 18)
    descripcion.place(x=170,y=150)

    freclabel=Label(root,text="Frecuencia:",foreground="black", background="white", font=("Times", 11))
    freclabel.place(x=70,y=200)

    calabel=Label(root,text="Cada",foreground="black", background="white", font=("Times", 11))
    calabel.place(x=170,y=200)

    spin = Spinbox(root, from_= 0, to = 100, width=3)  
    spin.place(x=211,y=200)

    unlabel=Label(root,text="unidades",foreground="black", background="white", font=("Times", 11))
    unlabel.place(x=248,y=200)

    Bacep=Button(root,text="Aceptar",command= lambda: nuevoProceso(nombre.get(), descripcion.get(),spin.get()), font=("Times", 13), height=1)
    Bacep.place(x=222,y=250)

    Bcan=Button(root,text="Cancelar",command= lambda: cancelar(root), font=("Times", 13), height=1)
    Bcan.place(x=290,y=250)

def ingresar_proceso2(tituloVentana, mensajeVentana, tipo, listanodos):
    lista= list(range(0, len(listanodos)))
    root= Tk()
    root.title("Estudio de Tiempos")
    root.resizable(0,0)
    root.geometry("400x400")
    root.config(bg="white")

    labelP=Label(root,text=tipo,foreground="black", background="white", font=("Times", 11))
    labelP.place(x=15,y=85)
   
    titulo= Label(root,text="Estudio de Tiempos",foreground="black", background="white", font=("Times", 12, "italic") )
    titulo.place(x=265,y=3)
    tituloV= Label(root,text=tituloVentana,foreground="black", background="white", font=("Times", 15, "bold") )
    tituloV.pack(pady=30)
    mensajeV= Label(root,text=mensajeVentana,foreground="black", background="white", font=("Times", 12), justify="left" )
    mensajeV.place(x=15,y=120)
    Bacep=Button(root,text="Aceptar",command= addPredecesores, font=("Times", 13), height=1, )
    Bacep.place(x=320,y=340)

    
    predecesor= ttk.Combobox(root,values=lista,width= 15)
    predecesor.bind("<<ComboboxSelected>>",partial(llenarScroll,predecesor,listanodos,root))
    predecesor.place(x=140,y=85)

contador=0
def llenarScroll(predecesorCmb,listanodos, root, a):
    predecesor=predecesorCmb.get()
    global lista
    lista=[]
    if predecesor!="":
        
        frameTwo = Frame(root,bg="white")
        
        canvas=Canvas(frameTwo,bg="white",width=350,height=200)
        canvas.pack(side="left")

        scrollb=ttk.Scrollbar( frameTwo, orient="vertical",command=canvas.yview)
        scrollb.pack(side="right",fill="y")
        canvas.configure(yscrollcommand=scrollb.set) 
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion = canvas.bbox("all")))

        listFrame=Frame(canvas,background="white")
        canvas.create_window((0,0),window=listFrame, anchor="center")
    
    #scrollb.grid_forget()
        frameTwo.tkraise()    
        frameTwo.pack(side="top",pady=85)
        n = 1
        num_piezas=0
        print("aquio"+ predecesor +"...")
        num_piezas = int(predecesor)
        while n <= num_piezas:        
            textopieza = Label(listFrame, text = "Predecesor "+str(n), justify="left",bg="white")
            textopieza.pack(side="top")
            var = StringVar()
            llenar =ttk.Combobox(listFrame, values=listanodos, width=15)
            lista.append(llenar)
            llenar.config(width=10)
            llenar.pack(side= "top")
            n += 1
          
        
def deletef(frame):
    frame.pack_forget()
    frame.destroy()


def varios(tituloVentana, mensajeVentana, tipo, listanodos):
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

    frameTwo = Frame(root,bg="white")
    canvas=Canvas(frameTwo,bg="white",width=350,height=200)
    canvas.pack(side="left")

    scrollb=ttk.Scrollbar( frameTwo, orient="vertical",command=canvas.yview)
    scrollb.pack(side="right",fill="y")
    canvas.configure(yscrollcommand=scrollb.set) 
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion = canvas.bbox("all")))


    listFrame=Frame(canvas,background="white")
    canvas.create_window((0,0),window=listFrame, anchor="center")

    
    #scrollb.grid_forget()    
    frameTwo.pack(side="top",pady=85)
    num_piezas = len(listanodos)
    
    n = 1
    
    while n <= num_piezas:        
        textopieza = Label(listFrame, text = "Proceso: "+str(n), justify="left",bg="white")
        textopieza.pack(side="top", padx=150)
        var = StringVar()
        if(tipo=="personas"):
            llenar=Spinbox(listFrame, from_= 0, to = 150)  
        else:
            llenar =ttk.Combobox(listFrame, values=listanodos, width=15)
        llenar.config(width=10)
        llenar.pack(side= "top", padx=150)
        n += 1



#varios("Eliminar proceso", "A continuación debera modificar los procesos que\nquedarán sin antecesor","Procesos:")


