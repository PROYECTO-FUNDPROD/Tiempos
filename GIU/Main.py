from tkinter import *
from tkinter import filedialog
'Primera Ventana'
def mainwindow():

    root= Tk()

    root.title("Estudio de Tiempos")
    root.resizable(0,0)
    root.geometry("400x300")
    root.config(bg="white")

    titulo= Label(root,text="Estudio de Tiempos",foreground="black", background="white", font=("Times", 18) )
    titulo.pack(side=TOP, pady=20)

    BNuevo=Button(root,text="Nuevo Grafo",command=buscargrafo, font=("Times", 14))
    BNuevo.pack(pady=35)

    bold=Button(root,text="Usar grafo anterior",command=buscargrafo, font=("Times", 14))
    bold.pack()

    root.mainloop()

def buscargrafo():
    archivo= filedialog.askopenfilename(initialdir='/', title='Seleccione el archivo')

    'Segunda Ventana'

mainwindow()