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

def agregarTiempo(tarea,operario,tiempo):
    tarea=getObjectbyName(tarea)
    cont.agregarTiempo(tarea,operario,tiempo)

def agregarFNivelacion(tarea,operario, Fnivelacion):
    tarea=getObjectbyName(tarea)
    cont.agregarFNivelacion(tarea,operario,Fnivelacion)
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




