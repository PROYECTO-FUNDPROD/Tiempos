# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:04:13 2021

@author: valen
"""

import config


from App.Model import proceso
import networkx as nx
#import graphviz

#from Model import proceso as proceso




list_procesos=[]
tiempos={}

def nueva_tarea(nombre, descripcion, frecuencia):
    objeto = proceso(nombre, descripcion, frecuencia)
    list_procesos.append(objeto)
    return objeto

def eliminarProceso(object):
    list_procesos.remove(object)

def getTareasNombres():
    list_nombres=[]
    for cada_objeto in list_procesos:
        list_nombres.append(cada_objeto.nombre)
    return list_nombres

def addPredecesor(tarea,predecesor):
    tarea.add_predecesor(predecesor)

def eliminarPredecesor(tarea, predecesor):
    tarea.delete_predecesor(predecesor)

def eliminarTodosPredecesores(object):
    del object.predecesores[:]

def BorrarTodo():
    del list_procesos[:]

def getObjectbyName(name):
    objeto=None
    for cada_objeto in list_procesos:
        if cada_objeto.nombre== name:
            objeto=cada_objeto
    return objeto

def getSucesores(object):
    lista_Sucesores=[]
    for cada_objeto in list_procesos:
        if object in cada_objeto.predecesores:
            lista_Sucesores.append(cada_objeto.nombre)
    return lista_Sucesores

def dibujarGrafo():
    G = nx.DiGraph() # crear un grafo
    for cada_objeto in list_procesos:
        G.add_node(cada_objeto.nombre)
 
    for cada_objeto in list_procesos:
        for predecesor in cada_objeto.predecesores:
            G.add_edge(predecesor.nombre,cada_objeto.nombre)
    A = nx.nx_agraph.to_agraph(G)
    A.layout()
    ruta="Salida.png"
    A.draw(ruta)
    return ruta
    
    #graphviz.Source(A.to_string()) 
def agregarTiempo(tarea,operario,tiempo):
    if tarea in tiempos:
        if operario in tiempos[tarea]:
            veces= tiempos[tarea][operario]["cant"]
            suma= tiempos[tarea][operario]["Promedio"]*veces
            promedio= (suma+tiempo)/(veces+1)
            tiempos[tarea][operario]["Promedio"]=promedio
            tiempos[tarea][operario]["cant"]+=1
        else:
            tiempos[tarea][operario]={"Promedio":tiempo, "cant":1}

    else:
        tiempos[tarea]={}
        tiempos[tarea][operario]={"Promedio":tiempo, "cant":1}
def encontrarParalelos():
    comun=[]
    paralelos=[]
    for object in list_procesos:
        for cada_objeto in list_procesos:
            if object in cada_objeto.predecesores:
                comun.append(cada_objeto)
        if len(comun)>1:
            sucesores=[]
            for paralelo in comun:
                list=[]
                list.append(paralelo)
                paralelos.append(list)
                sucesores.append(getSucesores(paralelo))
            for paralelo2 in comun:
                none=""


        
