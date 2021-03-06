import sys
import os
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from functools import partial
import tkinter as tk
import config
import App.View as vw
import cronometro as cron

def imprimir():
    print("botton")

def cancelar(r):
    r.destroy()

def addPredecesores(r):
    print("botton")
    for i in range (0, len(lista)):
        pre=lista[i].get()
        vw.agregarPredecesor(tarea,pre)
    r.destroy()

def ajustarPredecesores(r):
    if len(dic_ajuste_predecesores)>0:
        for proceso in dic_ajuste_predecesores:
            vw.eliminarPredecesor(proceso, Aeliminar)
            if dic_ajuste_predecesores[proceso]!="El predecesor ya fue elegido" and dic_ajuste_predecesores[proceso]!="Sin Sucesor":
                tarea=vw.getObjectbyName(proceso)
                vw.agregarPredecesor(tarea,dic_ajuste_predecesores[proceso])
    vw.eliminarProceso(Aeliminar)
    r.destroy()

def reasignarPredecesores(r):
    vw.eliminarTodosPredecesores(Aacomodar)
    if len(lista_nuevos_predecesores)>0:
        tarea=vw.getObjectbyName(Aacomodar)
        for cada_nuevo_predecesor in lista_nuevos_predecesores:
            vw.agregarPredecesor(tarea,cada_nuevo_predecesor)        
    r.destroy()

def imprimir1():
    print("botton")

def dibujar():
    imagen=PhotoImage(file="GIU/"+vw.dibujarGrafo())
    
    #global Dibujo
    #Dibujo.pack( )
    Dibujo["image"]=imagen
    Dibujo.image=imagen

def nuevoProceso(nombre,descripcion, frecuencia,r):
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
        tareas.remove(nombre)
        if len(tareas)>1:
            r.destroy()
            ingresar_proceso2("Añadir Predecesores", "A continuación debe ingresar los predecesores del Proceso {0}".format(nombre),"Cantidad de predecesores: ",tareas)
            
def mostrarTareasSinPrecedesores(predecesorCmb,root,a):
    global Aeliminar
    Aeliminar=predecesorCmb.get()
    lista_sucesores= vw.getSucesores(Aeliminar)
    opciones=vw.getTareasNombres()
    opciones.remove(Aeliminar)
    opciones.append("Sin predecesor")
    opciones.append("El predecesor ya fue elegido")
    if len(lista_sucesores)>= 1:
        llenarScrollEliminar(predecesorCmb,lista_sucesores,opciones,root,a)
    else:
        mensajeVentana=" Para el proceso seleccionado no se encontraron sucesores.\n De click en Aceptar para eliminar correctamente el proceso. "
        llenarLabel(mensajeVentana,root)
        global dic_ajuste_predecesores
        dic_ajuste_predecesores={}

def MostrarNodosyCantidad(proceso,cantidad,tareas, root,a):
    global Aacomodar
    Aacomodar=proceso.get()
    tareas.remove(proceso.get())
    if int(cantidad.get())>0:
        LlenarScrollModificar(proceso,cantidad,tareas, root)


def openWindow(tituloVentana, mensajeVentana,tipo):
    #r.destroy()
    tareas= vw.getTareasNombres()
    Ventana_Eliminar_Proceso(tituloVentana, mensajeVentana,tipo, tareas)

def openWindowMod(tituloVentana, mensajeVentana,tipo):
    tareas= vw.getTareasNombres()
    Ventana_Modificar_Proceso(tituloVentana, mensajeVentana, tipo, tareas)

def BorrarTodo():
    vw.BorrarTodo()

def continuar(r):
    r.destroy()
    tareas= vw.getTareasNombres()
    cron.cronometro(tareas)

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
    global Dibujo
    
    imagen=PhotoImage(file="GIU/Inicio.png")
    Dibujo= Label(root,image=imagen,width=800,height=340,bg="white")
    Dibujo.pack( )
    Dibujo.image=imagen

    Bnp=Button(root,text="Añadir Proceso",command=ingresar_proceso, font=("Times", 13),height=1)
    Bnp.place(x=155,y=420)

    Bep=Button(root,text="Eliminar Proceso",command= lambda: openWindow("Eliminar Proceso", "A continuación deberá modificar los procesos que\nquedarán sin antecesor","Proceso: "), font=("Times", 13), height=1)
    Bep.place(x=275,y=420)

    Bbt=Button(root,text="Modificar Proceso",command=lambda: openWindowMod("Modificar Proceso", "A continuación podrá modificar los predecesores del\nproceso deseado. Debe reingresar todos los predecesores\nde dicho proceso.","Proceso: "), font=("Times", 13),height=1)
    Bbt.place(x=410,y=420)

    Bbt=Button(root,text="Borrar Todo",command=BorrarTodo, font=("Times", 13),height=1)
    Bbt.place(x=780,y=420)

    Bdib=Button(root,text="Dibujar",command=dibujar, font=("Times", 13), height=1)
    Bdib.place(x=879,y=420)

    Bcalc=Button(root,text="Siguiente",command= lambda: continuar(root), font=("Times", 16), fg='red', height=2, width=16)
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

    descripcion= ttk.Combobox(root, text="Descripción",values=["Manual", "Automático"],width= 18, state="readonly")
    descripcion.place(x=170,y=150)

    freclabel=Label(root,text="Frecuencia:",foreground="black", background="white", font=("Times", 11))
    freclabel.place(x=70,y=200)

    calabel=Label(root,text="Cada",foreground="black", background="white", font=("Times", 11))
    calabel.place(x=170,y=200)

    spin = Spinbox(root, from_= 0, to = 100, width=3)  
    spin.place(x=211,y=200)

    unlabel=Label(root,text="unidades",foreground="black", background="white", font=("Times", 11))
    unlabel.place(x=248,y=200)

    Bacep=Button(root,text="Aceptar",command= lambda: nuevoProceso(nombre.get(), descripcion.get(),spin.get(),root), font=("Times", 13), height=1)
    Bacep.place(x=222,y=250)

    Bcan=Button(root,text="Cancelar",command= lambda: cancelar(root), font=("Times", 13), height=1)
    Bcan.place(x=290,y=250)

def ingresar_proceso2(tituloVentana, mensajeVentana, tipo, listanodos):
    lista_cantidad= list(range(0, len(listanodos)+1))
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
    Bacep=Button(root,text="Aceptar",command= lambda: addPredecesores(root), font=("Times", 13), height=1, )
    Bacep.place(x=320,y=340)

    
    predecesor= ttk.Combobox(root,values=lista_cantidad,width= 15,state="readonly")
    predecesor.bind("<<ComboboxSelected>>",partial(llenarScroll,predecesor,listanodos,root))
    predecesor.place(x=180,y=85)
contador=0
def llenarScroll(predecesorCmb,listanodos, root, a):
    predecesor=predecesorCmb.get()
    print(listanodos)
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
            llenar =ttk.Combobox(listFrame, values=listanodos, width=15,state="readonly")
            lista.append(llenar)
            llenar.config(width=10)
            llenar.pack(side= "top")
            n += 1    
        
def deletef(frame):
    frame.pack_forget()
    frame.destroy()

def Ventana_Eliminar_Proceso(tituloVentana, mensajeVentana, tipo, listanodos):
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
    Bacep=Button(root,text="Aceptar",command= lambda:ajustarPredecesores(root), font=("Times", 13), height=1, )
    Bacep.place(x=242,y=340)
    Bacep=Button(root,text="Cancelar",command= lambda: cancelar(root), font=("Times", 13), height=1, )
    Bacep.place(x=310,y=340)

    predecesor= ttk.Combobox(root,values=listanodos,width= 15,state="readonly")
    predecesor.bind("<<ComboboxSelected>>",partial(mostrarTareasSinPrecedesores,predecesor,root))
    predecesor.place(x=140,y=85)
def llenarScrollEliminar(predecesorCmb,lista_sucesores, listanodos, root, a):
    predecesor=predecesorCmb.get()
    global dic_ajuste_predecesores
    dic_ajuste_predecesores={}
    
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
        n = 0
        num_piezas=0
        print("aquio"+ predecesor +"...")
        num_piezas = len(lista_sucesores)
        while n < num_piezas:        
            textopieza = Label(listFrame, text = "Nuevo Predecesor Tarea "+str(lista_sucesores[n]), justify="left",bg="white")
            textopieza.pack(side="top")
            var = StringVar()
            listan=listanodos.copy()
            listan.remove(lista_sucesores[n])
            llenar =ttk.Combobox(listFrame, values=listan, width=20, state="readonly")
            dic_ajuste_predecesores[lista_sucesores[n]]=llenar
            llenar.config(width=25)
            llenar.pack(side= "top")
            n += 1
def llenarLabel(mensajeVentana,root):
    mensajeV= Label(root,text=mensajeVentana,foreground="black", background="white", font=("Times", 12), justify="left",borderwidth="1", relief="solid", width=42, height=6 )
    mensajeV.place(x=10, y=185)         

def Ventana_Modificar_Proceso(tituloVentana, mensajeVentana, tipo, listanodos):
    lista_cantidad= list(range(0, len(listanodos)))
    root= Tk()
    root.title("Estudio de Tiempos")
    root.resizable(0,0)
    root.geometry("400x400")
    root.config(bg="white")

    labelP=Label(root,text=tipo,foreground="black", background="white", font=("Times", 11))
    labelP.place(x=15,y=65)
    labelC=Label(root,text="Cantidad: ",foreground="black", background="white", font=("Times", 11))
    labelC.place(x=15,y=95)
    titulo= Label(root,text="Estudio de Tiempos",foreground="black", background="white", font=("Times", 12, "italic") )
    titulo.place(x=265,y=3)
    tituloV= Label(root,text=tituloVentana,foreground="black", background="white", font=("Times", 15, "bold") )
    tituloV.pack(pady=30)
    mensajeV= Label(root,text=mensajeVentana,foreground="black", background="white", font=("Times", 12), justify="left" )
    mensajeV.place(x=15,y=120)
    Bacep=Button(root,text="Aceptar",command= lambda:reasignarPredecesores(root), font=("Times", 13), height=1, )
    Bacep.place(x=242,y=335)
    Bacep=Button(root,text="Cancelar",command= lambda: cancelar(root), font=("Times", 13), height=1, )
    Bacep.place(x=310,y=335)

    proceso= ttk.Combobox(root,values=listanodos,width= 15,state="readonly")
    proceso.place(x=140,y=65)
    cantidad= ttk.Combobox(root,values=lista_cantidad,width= 15,state="readonly")
    cantidad.bind("<<ComboboxSelected>>",partial(MostrarNodosyCantidad,proceso,cantidad,listanodos,root))
    cantidad.place(x=140,y=95)

def LlenarScrollModificar(procesoCmb, cantidadCmb, listanodos, root):
    cantidad=cantidadCmb.get()
    global lista_nuevos_predecesores
    lista_nuevos_predecesores=[]
    if cantidad!="":
        
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
        frameTwo.pack(side="top",pady=110)
        n = 1
        num_piezas=0
        num_piezas = int(cantidad)
        while n <= num_piezas:        
            textopieza = Label(listFrame, text = "Predecesor "+str(n), justify="left",bg="white")
            textopieza.pack(side="top")
            var = StringVar()
            llenar =ttk.Combobox(listFrame, values=listanodos, width=15,state="readonly")
            lista_nuevos_predecesores.append(llenar)
            llenar.config(width=10)
            llenar.pack(side= "top")
            n += 1    
#varios("Eliminar proceso", "A continuación debera modificar los procesos que\nquedarán sin antecesor","Procesos:")


