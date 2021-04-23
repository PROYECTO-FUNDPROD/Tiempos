from tkinter import *


'Primera Ventana'
root= Tk()

root.title("Estudio de Tiempos")
root.resizable(0,0)
root.geometry("400x300")
root.config(bg="white")

titulo= Label(root,text="Estudio de Tiempos",foreground="white", background="black",width=44,height=1, font=("Times", 12) )
titulo.place(x=0,y=60)

titulo2= Label(root,text="Estudio de Tiempos",foreground="yellow", background="gray",width=0,height=0, font=("Times", 12) )
titulo2.pack()


def imprimir():
    print("Se presionó el botón")

BNuevo=Button(root,text="Nuevo Grafo",command=imprimir, width=12)
BNuevo.place(y=105)


bold=Button(root,text="Usar grafo anterior",command=imprimir)
bold.place(y=250)


root.mainloop()

