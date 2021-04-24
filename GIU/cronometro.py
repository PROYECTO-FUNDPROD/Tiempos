from tkinter import Tk,Label,Button,Frame
from tkinter import *
from functools import partial
proceso=0
contador=0
def iniciar(time):
    global proceso
    global contador
    contador+=1
    time.config(state="normal")
    # mostramos la variable contandor
    time.delete(0,"end")
    time.insert(0, contador)
    time.config(state="disabled")
    
    # hacemos un llamamient a la funcion mostrarContador pasando el
    # contador mas uno
    proceso=time.after(1000, iniciar, time)
 
def parar(time):
    global proceso
    time.after_cancel(proceso)
    time.config(state="normal")

def cronometro():
    root = Tk()
    root.title('Cronometro')
    root.resizable(0,0)
    root.geometry("650x400")
    root.config(bg="white")
 
    tiempo = Entry(root, fg='black', width=20, font=("","18"))    
    tiempo.pack()
 
# si queremos que se autoejecuta al iniciar el programa hay que desomentar
# esta linea y comentar los botones
#iniciar()
 
# Generamos un frame para poner los botones de iniciar y parar
    btnIniciar=Button(root, fg='black',bg="white", text='Iniciar', command=partial(iniciar,(tiempo)))
    btnIniciar.place(x=200,y=50)
    btnParar=Button(root, fg='black',bg="white", text='Parar', command=partial(parar,tiempo))
    btnParar.place(x=250,y=50)
    btnGuardar=Button(root, fg='black',bg="white", text='Guardar', command=partial(imprimir,tiempo))
    btnGuardar.place(x=300,y=50)
    root.mainloop()

def imprimir(time):
    
    print(time.get())
cronometro()

