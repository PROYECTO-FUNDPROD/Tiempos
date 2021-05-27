from tkinter import Tk,Label,Button,Frame
from tkinter import *
from functools import partial
from tkinter import ttk
import Msgbox as msgs
proceso=0
contador=0
user=1
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

def cronometro():
    global user
    root = Tk()
    root.title('Cronometro')
    root.resizable(0,0)
    root.geometry("400x200")
    root.config(bg="white")
    global tiempo
    tiempo = Entry(root, fg='black', width=25, font=("","18"))    
    tiempo.pack()
    tiempo.insert(0, 0)
    
# si queremos que se autoejecuta al iniciar el programa hay que desomentar
# esta linea y comentar los botones
#iniciar()
 
# Generamos un frame para poner los botones de iniciar y parar
    btnIniciar=Button(root, fg='black',bg="white", text='Iniciar', command=partial(iniciar,(tiempo)))
    btnIniciar.place(x=35,y=50)
    btnParar=Button(root, fg='black',bg="white", text='Parar', command=partial(parar,tiempo))
    btnParar.place(x=85,y=50)
    btnGuardar=Button(root, fg='black',bg="white", text='Guardar', command=partial(imprimir,tiempo))
    btnGuardar.place(x=135,y=50)
    Sexolabel=Label(root,text="Sexo:",foreground="black", background="white", font=("Times", 11),)
    Sexolabel.place(x=35,y=100)

    Sexo= ttk.Combobox(root,values=['Hombre','Mujer'],width= 18)
    Sexo.place(x=215,y=100)
    Fnivelacionlabel=Label(root,text="Factor de Nivelacion:",foreground="black", background="white", font=("Times", 11),)
    Fnivelacionlabel.place(x=35,y=130)

    Fnivelacion= Spinbox(root, from_= 0, to = 150, width=19) 
    Fnivelacion.place(x=215,y=130)
    root.mainloop()

def imprimir(time):
    global user
    msgs.doMessageBox("Guardar tiempo","Desea guardar el tiempo registrado?. Usuario "+str(user),"info",siAccion,noAccion)
    print(time.get())

def noAccion():
    global user
    reiniciarCronometro()
    user+=1
    print ("Usuario es "+ str(user))
    print("No Funciona")

def siAccion():
    global user
    msgs.doMessageBox("Guardar tiempo","Desea registrar otro tiempo?. Usuario "+str(user),"info",reiniciarCronometro,noAccion)
    print("Funciona")
def reiniciarCronometro():
    global proceso
    global contador
    proceso=0
    contador=0
    tiempo.config(state="normal")
    tiempo.delete(0,"end")
    tiempo.insert(0, contador)

cronometro()

