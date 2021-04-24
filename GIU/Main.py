from tkinter import *
from tkinter import filedialog
import Newgraph as N
import Msgbox as msgs
from tkinter import messagebox as mb
from functools import partial
'Primera Ventana'
def mainwindow():

    root= Tk()

    root.title("Estudio de Tiempos")
    root.resizable(0,0)
    root.geometry("400x300")
    root.config(bg="white")

    titulo= Label(root,text="Estudio de Tiempos",foreground="black", background="white", font=("Times", 18) )
    titulo.pack(side=TOP, pady=20)

    BNuevo=Button(root,text="Nuevo Grafo",command=partial(newgraph,root), font=("Times", 14))
    BNuevo.pack(pady=35)

    bold=Button(root,text="Usar grafo anterior",command=buscargrafo, font=("Times", 14))
    bold.pack()

    root.mainloop()

def buscargrafo():
    msgs.doMessageBox("Titulo Prueba","Mensaje Prueba","info",noAccion,noAccion)
    archivo= filedialog.askopenfilename(initialdir='/', title='Seleccione el archivo')

    'Segunda Ventana'
def newgraph(r):
    r.destroy()
    N.segundaVentana()
def noAccion():
    null


    

    
mainwindow()