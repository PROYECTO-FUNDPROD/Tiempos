from tkinter import Tk,Label,Button,Frame
from tkinter import *
from functools import partial
from tkinter import ttk
import Msgbox as msgs
import config
import App.View as vw
from tkinter.simpledialog import askinteger, askstring
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
    try:
        tiempo.after_cancel(proceso)
    except:
        print("No se inicio el cronometro")


def cronometro(tasks):
    global tareas
    global tiempo
    global titulo3
    global btnIniciar
    global btnGuardar
    global tareasNombres
    tareasNombres=vw.getTareasNombres()
    tareas=len(tareasNombres)
    root = Tk()
    root.title('Ingresar Tiempos de Ejecución')
    root.resizable(0,0)
    root.geometry("400x350")
    root.config(bg="white")
    titulo= Label(root,text="Estudio de Tiempos",foreground="black", background="white", font=("Times", 12, "italic") )
    titulo.place(x=265,y=3)
    titulo2= Label(root,text="Ingresar Tiempo de Ejecución por Operario",foreground="black", background="white", font=("Times", 12, 'bold') )
    titulo2.pack(pady=35)
    titulo3= Label(root,text="Tarea {1} Operario {0}:".format(user,tareasNombres[tarea-1]),foreground="black", background="white", font=("Times", 12) )
    titulo3.place(x=35,y=70)
    
    tiempo = Entry(root, fg='black', width=20, font=("Times", 18) )    
    tiempo.pack(pady=4)
    tiempo.insert(0, 0)
    
# si queremos que se autoejecuta al iniciar el programa hay que desomentar
# esta linea y comentar los botones
#iniciar()
 
# Generamos un frame para poner los botones de iniciar y parar

    btnIniciar=Button(root, fg='black',bg="white", text='Iniciar', command=iniciar,font=("Times", 12) )
    btnIniciar.place(x=35,y=145)

    btnGuardar=Button(root, fg='black',bg="white", text='Guardar',command= guardarGIU,font=("Times", 12) )
    btnGuardar.place(x=135,y=145)
    Sexolabel=Label(root,text="Sexo:",foreground="black", background="white", font=("Times", 11),)
    Sexolabel.place(x=35,y=245)

    Sexo= ttk.Combobox(root,values=['Hombre','Mujer'],width= 18)
    Sexo.place(x=215,y=245)
    global infolabel
    infolabel=Label(root,text="",foreground="black", background="white", font=("Times", 11),)
    infolabel.place(x=80,y=180)

    
    Bacep=Button(root,text="Continuar",command=partial(Continuar,Sexo), font=("Times", 13), height=1, )
    Bacep.place(x=260,y=280)
    root.mainloop()

def guardarGIU():
    
    global user
    

    parar()
    print(tiempo.get())
    msgs.doMessageBox("Guardar tiempo: Operario"+str(user),"¿Desea guardar el tiempo registrado para el Operario {0} en la tarea {1} ?".format(user,tareasNombres[tarea-1]),"info",otroTiempo,noAccion)
    

def CambioOperario():
    global user
    global tarea

    reiniciarCronometro()
    user+=1
    tarea=1
    titulo3.config(text="Tarea {1} Operario {0}:".format(user,tareasNombres[tarea-1]))
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








def cambioTarea():
    global tarea
    askinteger('Factor Nivelación', "Cual es el factor de nivelacion del operario {0} en la tarea {1}?".format(user,tareasNombres[tarea-1]),minvalue=0.0,maxvalue=150,initialvalue=100)
    tarea+=1
    try:
        titulo3.config(text="Tarea {1} Operario {0}:".format(user,tareasNombres[tarea-1]))
    except :
        print("No hay mas tareas")
    if tarea>tareas:
        infolabel.config(text="A continuación seleccione el sexo\ndel operario {0} y de click en continuar para\nguardar todos los tiempos del operario".format(user))
        deshabilitarBotones()
    reiniciarCronometro()
    

def guardarTiempo():
    vw.agregarTiempo(tareasNombres[tarea-1],user,tiempo.get())
    print("La tarea es {0} del usuario {1} con tiempo {2}".format(tareasNombres[tarea-1],user,tiempo.get()))


def otroTiempo():
    global user
    guardarTiempo()
    msgs.doMessageBox("Cronometrar nuevo tiempo","¿Desea registrar otro tiempo para el Operario {0} en la tarea {1}?".format(user,tareasNombres[tarea-1]),"info",reiniciarCronometro,cambioTarea)
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


def Continuar(Sexo):
    Sex=Sexo.get()
    if Sex=="" :
        titulo="Información Incompleta"
        mensaje= "Por favor complete todas las casillas de información para continuar"
        icono="error"
        msgs.okMessageBox(titulo,mensaje,icono)
    else:
        if tarea+1<tareas:
            titulo="Información Incompleta"
            mensaje= "Por favor complete al menos 1 tiempo para todas las tareas con este operario"
            icono="error"
            msgs.okMessageBox(titulo,mensaje,icono)
        else:
            titulo="Información Incompleta"
            mensaje= "Registró los tiempos para {0} Tareas del Operario {1} ¿Desea tomar tiempos para otro operario?".format(tarea-1,user)
            icono="info"
            msgs.doMessageBox(titulo,mensaje,icono,CambioOperario,siguienteVentana)


cronometro(2)

