from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from functools import partial
import Msgbox as mBox
import config
import App.View as vw

def Calculos_finales():
    dic=vw.calcularTB_TE_Promedios()
    resultados(dic)

def printTB(dic,root,fila):
    for cada_tarea in dic:
        for cada_operario in dic[cada_tarea]:
            tiempo= dic[cada_tarea][cada_operario]["Basico"]
            T = Text(root, height = 0, width = 70, font=("Times", 11), relief='flat')
            mensaje="Para la Tarea {0}, el Operario {1} tuvo un tiempo básico de {2} segundos.".format(cada_tarea.nombre, cada_operario.nombre, tiempo)
            T.insert(END, mensaje)
            T.place(x=35, y=fila)
            fila=fila+10
        titulo= Label(root,text="",foreground="black", background="white", font=("Times", 3, "italic") )
        titulo.place(x=35,y=fila+5)
        fila=fila+10

        

def resultados(dic):
    root= Tk()

    root.title("Estudio de Tiempos: Presentación de resultados")
    root.resizable(0,0)
    root.geometry("650x500")
    root.config(bg="white")

    titulo= Label(root,text="Estudio de Tiempos",foreground="black", background="white", font=("Times", 12, "italic") )
    titulo.place(x=515,y=3)

    titulo2= Label(root,text="Resultados",foreground="black", background="white", font=("Times", 18, 'bold') )
    titulo2.pack(pady=35)

    T = Text(root, height = 0, width = 70, font=("Times", 11), relief='flat')
    mensaje="Los resultados de tiempos se encuentran a continuación: "
    T.insert(END, mensaje)
    T.place(x=35, y=75)

    subtitulo2= Label(root,text="Tiempo básico para cada operario:",foreground="black", background="white", font=("Times", 12, 'bold'), justify="left")
    subtitulo2.place(x=33,y=100)


    fila=115
    printTB(dic,root,fila)

    root.mainloop()


