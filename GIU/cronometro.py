from tkinter import Tk,Label,Button,Frame
from tkinter import *
from functools import partial
from tkinter import ttk
import Msgbox as msgs
proceso=0
contador=0
user=1
tarea=1

def iniciar():
    global proceso
    global contador
    
    contador+=1
    tiempo.config(state="normal")
    # mostramos la variable contandor
    tiempo.delete(0,"end")
    tiempo.insert(0, contador)
    tiempo.config(state="disabled")
    
    # hacemos un llamamient a la funcion mostrarContador pasando el
    # contador mas uno
    proceso=tiempo.after(1000, iniciar)
 
def parar():

    tiempo.after_cancel(proceso)

def cronometro(tasks):
    global tareas
    global tiempo
    global titulo3
    global btnIniciar
    global btnGuardar
    tareas=tasks
    root = Tk()
    root.title('Ingresar Tiempos de Ejecución')
    root.resizable(0,0)
    root.geometry("400x350")
    root.config(bg="white")
    titulo= Label(root,text="Estudio de Tiempos",foreground="black", background="white", font=("Times", 12, "italic") )
    titulo.place(x=265,y=3)
    titulo2= Label(root,text="Ingresar Tiempo de Ejecución por Operario",foreground="black", background="white", font=("Times", 12, 'bold') )
    titulo2.pack(pady=35)
    titulo3= Label(root,text="Tarea {1} Operario {0}:".format(user,tarea),foreground="black", background="white", font=("Times", 12) )
    titulo3.place(x=35,y=70)
    
    tiempo = Entry(root, fg='black', width=20, font=("","18"))    
    tiempo.pack(pady=4)
    tiempo.insert(0, 0)
    
# si queremos que se autoejecuta al iniciar el programa hay que desomentar
# esta linea y comentar los botones
#iniciar()
 
# Generamos un frame para poner los botones de iniciar y parar

    btnIniciar=Button(root, fg='black',bg="white", text='Iniciar', command=iniciar)
    btnIniciar.place(x=35,y=145)

    btnGuardar=Button(root, fg='black',bg="white", text='Guardar',command= imprimir)
    btnGuardar.place(x=135,y=145)
    Sexolabel=Label(root,text="Sexo:",foreground="black", background="white", font=("Times", 11),)
    Sexolabel.place(x=35,y=190)

    Sexo= ttk.Combobox(root,values=['Hombre','Mujer'],width= 18)
    Sexo.place(x=215,y=190)
    Fnivelacionlabel=Label(root,text="Factor de Nivelacion:",foreground="black", background="white", font=("Times", 11),)
    Fnivelacionlabel.place(x=35,y=230)

    Fnivelacion= Spinbox(root, from_= 0, to = 150, width=19) 
    Fnivelacion.place(x=215,y=230)
    Bacep=Button(root,text="Continuar",command=partial(Continuar,Fnivelacion.get(),Sexo.get()), font=("Times", 13), height=1, )
    Bacep.place(x=260,y=280)
    root.mainloop()

def imprimir():
    global user
    parar()
    msgs.doMessageBox("Guardar tiempo: Operario"+str(user),"¿Desea guardar el tiempo registrado para el Operario {0} en la tarea {1} ?".format(user,tarea),"info",otroTiempo,noAccion)
    print(tiempo.get())

def CambioOperario():
    global user
    global tarea

    reiniciarCronometro()
    user+=1
    tarea=1
    titulo3.config(text="Tarea {1} Operario {0}:".format(user,tarea))
    habilitarBotones()
    print("No Funciona")

def noAccion():
    global user    
    reiniciarCronometro()

def deshabilitarBotones():
    btnIniciar.config(state="disabled")
    btnGuardar.config(state="disabled")
def habilitarBotones():
    btnIniciar.config(state="normal")
    btnGuardar.config(state="normal")



def guardarTiempos():
    none=0




def cambioTarea():
    global tarea
    tarea+=1
    titulo3.config(text="Tarea {1} Operario {0}:".format(user,tarea))
    if tarea>tareas:
        deshabilitarBotones()
    reiniciarCronometro()
    guardarTiempo()

def guardarTiempo():

    none=0


def otroTiempo():
    global user
    msgs.doMessageBox("Cronometrar nuevo tiempo","¿Desea registrar otro tiempo para el Operario {0} en la tarea?".format(user,tarea),"info",reiniciarCronometro,cambioTarea)
    print("Funciona")

def reiniciarCronometro():
    global proceso
    global contador
    proceso=0
    contador=0
    tiempo.config(state="normal")
    tiempo.delete(0,"end")
    tiempo.insert(0, contador)

def siguienteVentana():
    print("PASO A SIGUIENTE VENTANA")


def Continuar(Fniv,Sexo):
    print (Sexo)
    print (Fniv)
    if Fniv == 0 or Sexo=="":
        titulo="Información Incompleta"
        mensaje= "Por favor complete todas las casillas de información para continuar"
        icono="error"
        msgs.okMessageBox(titulo,mensaje,icono)
    titulo="Información Incompleta"
    mensaje= "¿Esta seguro que desea continuar?, registro los tiempos para {0} Tareas del {1} Operario".format(tarea-1,user)
    icono="info"
    msgs.doMessageBox(titulo,mensaje,icono,CambioOperario,noAccion)


cronometro(2)

