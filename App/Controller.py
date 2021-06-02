# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:04:13 2021

@author: valen
""""""
import config
from App.Model import proceso"""
from Model import proceso as proceso

list_procesos=[]

def nueva_tarea(nombre, descripcion, frecuencia):
    objeto = proceso(nombre, descripcion, frecuencia)
    list_procesos.append(objeto)
    return objeto

def getTareasNombres():
    list_nombres=[]
    for cada_objeto in list_procesos:
        list_nombres.append(cada_objeto.nombre)
    return list_nombres

def getObjectbyName(name):
    objeto=None
    for cada_objeto in list_procesos:
        if cada_objeto.nombre== name:
            objeto=cada_objeto
    return objeto

