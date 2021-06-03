# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:04:04 2021

@author: valen
"""

import config
import App.Controller as cont

#import Controller as cont

def nueva_tarea(nombre,descripcion, frecuencia):
    tarea= cont.nueva_tarea(nombre,descripcion,frecuencia)
    return tarea

def getTareasNombres():
    tareas=cont.getTareasNombres()
    return tareas

def agregarPredecesor(tarea,predecesor):
    pre=getObjectbyName(predecesor)
    cont.addPredecesor(tarea,pre)

def getObjectbyName(name):
    object= cont.getObjectbyName(name)
    return object

def getSucesores(name):
    object=getObjectbyName(name)
    sucesores=cont.getSucesores(object)
    return sucesores

def eliminarProceso(name):
    object=getObjectbyName(name)
    cont.eliminarProceso(object)

def eliminarPredecesor(name, predecesor):
    object=getObjectbyName(name)
    predecesor=getObjectbyName(predecesor)
    cont.eliminarPredecesor(object, predecesor)

def eliminarTodosPredecesores(name):
    object=getObjectbyName(name)
    cont.eliminarTodosPredecesores(object)

def BorrarTodo():
    cont.BorrarTodo()
    print(getTareasNombres())
def dibujarGrafo():
    return cont.dibujarGrafo()

def nuevoOperario(name):
    cont.nuevoOperario(name)

def validarOperario(name):
    cont.validarOperario(name)

def getObjectOperariobyName(name):
    object= cont.getObjectOperariobyName(name)
    return object

def agregarTiempo(tarea,operario,tiempo):
    tarea=getObjectbyName(tarea)
    validarOperario(operario)
    operario=getObjectOperariobyName(operario)
    cont.agregarTiempo(tarea,operario,tiempo)

def agregarFNivelacion(tarea,operario, Fnivelacion):
    tarea=getObjectbyName(tarea)
    operario=getObjectOperariobyName(operario)
    cont.agregarFNivelacion(tarea,operario,Fnivelacion)

def guardarCondiciones(trabajo_pie, postura, peso_levantado,iluminacion, humedad, concentracion, ruido, tension, monotonia,tedio):
    cont.guardarCondiciones(trabajo_pie, postura, peso_levantado,iluminacion, humedad, concentracion, ruido, tension, monotonia,tedio)

def agregarSexo(sexo,user):
    object=getObjectOperariobyName(user)
    cont.agregarSexo(sexo,object)

def definirHolguras():
    cont.definirHolguras()

def calcularTB_TE_Promedios():
    dic= cont.calcularTB_TE_Promedios()
    return dic



"""
print(nueva_tarea("Prueba test tarea","AUTO","2").nombre,nueva_tarea("B","AUTO","2").nombre,nueva_tarea("C","AUTO","2").nombre )
agregarPredecesor(getObjectbyName("B"),"Prueba test tarea")
    cont.dibujarGrafo()
"""
print(nueva_tarea("A","AUTO","2").nombre,nueva_tarea("B","AUTO","2").nombre,nueva_tarea("C","AUTO","2").nombre )
agregarPredecesor(getObjectbyName("C"),"A")
agregarPredecesor(getObjectbyName("C"),"B")
print(getTareasNombres())
print(getObjectbyName("C").nombre)
print(getObjectbyName("C").predecesores)
#print(getSucesores("A"))
#dibujarGrafo()




