from App.Controller import cerrar_reporte
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog
from tkinter import ttk
from functools import partial
import Msgbox as mBox
import config
import App.View as vw
import pprint as p

def abrir_reporte():
    nombre="Resultados Estudio de Tiempos"
    vw.abrir_reporte(nombre)
    escribir_reporte("RESULTADOS ESTUDIO DE TIEMPOS \n \n")
    guardarlineas("RESULTADOS ESTUDIO DE TIEMPOS \n \n")

def escribir_linea():
    vw.escribir_linea()

def escribir_reporte(mensaje):
    vw.escribir_reporte(mensaje)

def Calculos_finales():
    dic=vw.calcularTB_TE_Promedios()
    resultados(dic)

def cancelar(r):
    cerrar_reporte()
    r.destroy()

def imprimir():
    print()

def guardarlineas(linea):
    vw.guardarlineas(linea)

def guardarResultados():
    guardar= filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text file", ".txt")])
    vw.guardarResultados(guardar)


def openResultados(root):
    root.destroy()
    dic=vw.traerTiempos()
    resultados(dic)

def printTB(dic,root,fila):
    for cada_tarea in dic:
        for cada_operario in dic[cada_tarea]:
            if cada_operario!= "Promedio":
                tiempo= dic[cada_tarea][cada_operario]["Basico"]
                T = Text(root, height = 0, width = 70, font=("Times", 10), relief='flat')
                mensaje="Para la Tarea {0}, el Operario {1} tuvo un tiempo básico de {2} segundos.".format(cada_tarea.nombre, cada_operario.nombre, round(tiempo,1))
                T.insert(END, mensaje)
                T.place(x=35, y=fila)
                fila=fila+15
                escribir_reporte("\n"+mensaje)
                guardarlineas("\n"+mensaje)
        titulo= Label(root,text="",foreground="black", background="white", font=("Times", 3, "italic") )
        titulo.place(x=35,y=fila+5)
        fila=fila+15
        escribir_reporte("\n \n")
        guardarlineas('\n \n')
    return fila

def printTE(dic,root, fila):
    for cada_tarea in dic:
        for cada_operario in dic[cada_tarea]:
            if cada_operario!= "Promedio":
                tiempo= dic[cada_tarea][cada_operario]["Estandar"]
                T = Text(root, height = 0, width = 70, font=("Times", 10), relief='flat')
                mensaje="Para la Tarea {0}, el Operario {1} tuvo un tiempo estándar de {2} segundos.".format(cada_tarea.nombre, cada_operario.nombre, round(tiempo,1))
                T.insert(END, mensaje)
                T.place(x=35, y=fila)
                fila=fila+15
                escribir_reporte("\n"+mensaje)
                guardarlineas("\n"+mensaje)
        titulo= Label(root,text="",foreground="black", background="white", font=("Times", 6, "italic"),height=2 )
        titulo.place(x=35,y=fila+5)
        fila=fila+15
        escribir_reporte("\n \n")
        guardarlineas("\n \n")
    return fila

def printTEP(dic,root,fila):
    for cada_tarea in dic:
        tiempo= dic[cada_tarea]["Promedio"]
        T = Text(root, height = 0, width = 70, font=("Times", 10), relief='flat')
        mensaje="El tiempo estándar promedio de la Tarea {0} es de {1} segundos.".format(cada_tarea.nombre,round(tiempo,1))
        T.insert(END, mensaje)
        T.place(x=35, y=fila)
        fila=fila+15
        escribir_reporte("\n"+mensaje)
        guardarlineas("\n"+mensaje)
        escribir_reporte("\n")
        guardarlineas("\n \n")
    


def resultados(dic):
    tar=len(dic)
    op=len(list(dic.values()))
    dim=((62*op)+(65*tar))+200

    abrir_reporte()
    root= Tk()

    root.title("Estudio de Tiempos: Presentación de resultados")
    root.resizable(0,0)
    root.geometry("500x{}".format(str(dim)))
    root.config(bg="white")

    titulo= Label(root,text="Estudio de Tiempos",foreground="black", background="white", font=("Times", 12, "italic") )
    titulo.place(x=365,y=3)

    titulo2= Label(root,text="Resultados",foreground="black", background="white", font=("Times", 18, 'bold') )
    titulo2.pack(pady=35)

    T = Text(root, height = 0, width = 70, font=("Times", 11), relief='flat')
    mensaje="Los resultados de tiempos para cada operario se encuentran a continuación: "
    T.insert(END, mensaje)
    T.place(x=35, y=75)

    escribir_reporte(mensaje+"\n")
    guardarlineas(mensaje+"\n")
    
    subtitulo2= Label(root,text="Tiempo básico para cada operario:",foreground="black", background="white", font=("Times", 12, 'bold'), justify="left")
    subtitulo2.place(x=33,y=100)

    escribir_reporte("\nTiempo básico para cada operario:")
    guardarlineas("\nTiempo básico para cada operario:")

    fila=130
    p.pprint(dic)
    fila= printTB(dic,root,fila)
    
    escribir_linea()
    guardarlineas("----------------------------------------------------\n")
    escribir_reporte("\nTiempo estándar para cada operario:")
    guardarlineas("\nTiempo estándar para cada operario:")
    subtitulo3= Label(root,text="Tiempo estándar para cada operario:",foreground="black", background="white", font=("Times", 12, 'bold'), justify="left")
    subtitulo3.place(x=33,y=fila)
    fila= fila+30
    fila=printTE(dic,root,fila)

    escribir_linea()
    guardarlineas("----------------------------------------------------\n")
    escribir_linea()
    guardarlineas("----------------------------------------------------\n")
    
    Bacep=Button(root,text="Ir a resultados generales",command= lambda: resultados2(dic,root), font=("Times", 13), height=1, )
    Bacep.place(x=300,y=dim-50)
    root.mainloop()



def resultados2(dic,r):
    r.destroy()
    tar=len(dic)
    dim= 30*tar+350
    root= Tk()

    root.title("Estudio de Tiempos: Presentación de resultados")
    root.resizable(0,0)
    root.geometry("500x{}".format(str(dim)))
    root.config(bg="white")

    titulo= Label(root,text="Estudio de Tiempos",foreground="black", background="white", font=("Times", 12, "italic") )
    titulo.place(x=365,y=3)

    titulo2= Label(root,text="Resultados",foreground="black", background="white", font=("Times", 18, 'bold') )
    titulo2.pack(pady=35)

    T = Text(root, height = 0, width = 70, font=("Times", 11), relief='flat')
    mensaje="Los resultados de tiempos promedio por Tarea se encuentran a continuación: "
    T.insert(END, mensaje)
    T.place(x=35, y=75)

    subtitulo2= Label(root,text="Tiempo estándar promedio para cada Tarea:",foreground="black", background="white", font=("Times", 12, 'bold'), justify="left")
    subtitulo2.place(x=33,y=100)
    escribir_reporte("\nLos resultados de tiempos promedio por Tarea se encuentran a continuación:\n")
    guardarlineas("\nLos resultados de tiempos promedio por Tarea se encuentran a continuación:\n")
    escribir_reporte("\nTiempo estándar promedio para cada Tarea:")
    guardarlineas("\nTiempo estándar promedio para cada Tarea:\n")


    fila= 135
    printTEP(dic,root,fila)
    escribir_reporte("\n")
    guardarlineas("\n")
    escribir_linea()
    guardarlineas("----------------------------------------------------\n")

    #subtitulo4= Label(root,text="Tiempo estándar de la empresa:",foreground="black", background="white", font=("Times", 12, 'bold'), justify="left")
    #subtitulo4.place(x=33,y=100)

    Bvol=Button(root,text="Volver a resultados por operario",command= lambda: openResultados(root), font=("Times", 13), height=1, )
    Bvol.place(x=10,y=dim-50)
    Bgud=Button(root,text="Guardar Resultados",command= lambda: guardarResultados(), font=("Times", 13), height=1, )
    Bgud.place(x=338,y=dim-85)
    Bce=Button(root,text="Terminar",command= lambda: cancelar(root), font=("Times", 13), height=1, )
    Bce.place(x=410,y=dim-50)



#Calculos_finales()
