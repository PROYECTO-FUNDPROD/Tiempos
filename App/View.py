# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:04:04 2021

@author: valen
"""

import config
import App.Controller as cont

"""
import Controller as cont
"""
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

def dibujarGrafo():
    cont.dibujarGrafo()


