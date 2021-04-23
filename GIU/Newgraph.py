from tkinter import *
from tkinter import messagebox as mb
def segundaVentana():
    root= Tk()

    root.title("Estudio de Tiempos")
    root.resizable(0,0)
    root.geometry("1200x700")
    root.config(bg="white")
    BProceso=Button(root,text="Nuevo Proceso",command=partial(newgraph,root), font=("Times", 14))
    BProceso.pack()
    mb.showinfo("Información", "Este programa fue desarrollado para el aprendizaje de Python y tkinter.")
