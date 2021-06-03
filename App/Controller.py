# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:04:13 2021

@author: valen
"""

import config


from App.Model import proceso
from App.Model import operario
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

def agregarFNivelacion(tarea,operario,Fnivelacion):
    tiempos[tarea][operario]["Fnivelacion"]=Fnivelacion     

def asignarHolgura(operario,trabajo_pie, postura, peso_levantado,iluminacion, humedad, concentracion, ruido, tension, monotonia,tedio):
    if operario.sexo=="Mujer":
        Holgura=CalcularHolguraMujer(trabajo_pie, postura, peso_levantado,iluminacion, humedad, concentracion, ruido, tension, monotonia,tedio)
        
    else:
        Holgura=CalcularHolguraHombre(trabajo_pie, postura, peso_levantado,iluminacion, humedad, concentracion, ruido, tension, monotonia,tedio)
    operario.asigHolgura(Holgura)

def CalcularHolguraHombre(trabajo_pie, postura, peso_levantado,iluminacion, humedad, concentracion, ruido, tension, monotonia,tedio):
    holgura= 5+4
    if trabajo_pie == "Sí":
        holgura+=2

    if postura == 'Incómoda':
        holgura+=2
    elif postura == 'Muy incómoda':
        holgura+=7
    

    if peso_levantado >= 32.5:
        holgura+=22
    if peso_levantado >= 30:
        holgura+=17
    elif peso_levantado >= 25:
        holgura+=13
    elif peso_levantado >= 22.5:
        holgura+=11
    elif peso_levantado >= 20:
        holgura+=9
    elif peso_levantado >= 17.5:
        holgura+=7
    elif peso_levantado >= 15:
        holgura+=5
    elif peso_levantado >= 12.5:
        holgura+=4
    elif peso_levantado >= 10:
        holgura+=3
    elif peso_levantado >= 7.5:
        holgura+=2
    elif peso_levantado >= 5:
        holgura+=1


    if iluminacion == 'Bastante baja':
        holgura+= 2
    elif iluminacion =='Absol. insuficiente':
        holgura+=5
    
    if humedad<=2:
        holgura+=100
    elif humedad<=3:
        holgura+=64
    elif humedad<=4:
        holgura+=45
    elif humedad<=5:
        holgura+=31
    elif humedad<=6:
        holgura+=21
    elif humedad<=8:
        holgura+=10
    elif humedad<=10:
        holgura+=3

    if concentracion== 'Precisión' or concentracion== 'Fatigoso':
        holgura+=2
    if concentracion== 'Gran precisión' or concentracion== 'Muy fatigoso':
        holgura+=5

    if ruido=="Intermitente y fuerte":
        holgura+=2
    elif ruido=="Intermitente y muy fuerte" or ruido=="Estridente y fuerte":
        holgura+=5

    if tension== 'Complejo':
        holgura=+ 1
    elif 'Bastante complejo':
        holgura+=4
    elif tension=='Muy complejo':
        holgura+=8
    
    if monotonia=='Bastante monótono':
        holgura+= 1
    elif monotonia=='Muy monótono':
        holgura+=4
    
    if tedio=='Bastante aburrido':
        holgura+= 2
    elif tedio=='Muy aburrido':
        holgura+=5
    return holgura
def CalcularHolguraMujer(trabajo_pie, postura, peso_levantado,iluminacion, humedad, concentracion, ruido, tension, monotonia,tedio):
    holgura= 7+4
    if trabajo_pie == "Sí":
        holgura+=4
    if postura=='Ligeramente incómoda':
        holgura+=1
    elif postura == 'Incómoda':
        holgura+=3
    elif postura == 'Muy incómoda':
        holgura+=7
    
    if peso_levantado >= 25:
        holgura+=20
    elif peso_levantado >= 22.5:
        holgura+=16
    elif peso_levantado >= 20:
        holgura+=13
    elif peso_levantado >= 17.5:
        holgura+=10
    elif peso_levantado >= 15:
        holgura+=8
    elif peso_levantado >= 12.5:
        holgura+=6
    elif peso_levantado >= 10:
        holgura+=4
    elif peso_levantado >= 7.5:
        holgura+=3
    elif peso_levantado >= 5:
        holgura+=2
    elif peso_levantado >= 2.5:
        holgura+=1

    if iluminacion == 'Bastante baja':
        holgura+= 2
    elif iluminacion =='Absol. insuficiente':
        holgura+=5
    
    if humedad<=2:
        holgura+=100
    elif humedad<=3:
        holgura+=64
    elif humedad<=4:
        holgura+=45
    elif humedad<=5:
        holgura+=31
    elif humedad<=6:
        holgura+=21
    elif humedad<=8:
        holgura+=10
    elif humedad<=10:
        holgura+=3

    if concentracion== 'Precisión' or concentracion== 'Fatigoso':
        holgura+=2
    if concentracion== 'Gran precisión' or concentracion== 'Muy fatigoso':
        holgura+=5

    if ruido=="Intermitente y fuerte":
        holgura+=2
    elif ruido=="Intermitente y muy fuerte" or ruido=="Estridente y fuerte":
        holgura+=5

    if tension== 'Complejo':
        holgura=+ 1
    elif 'Bastante complejo':
        holgura+=4
    elif tension=='Muy complejo':
        holgura+=8
    
    if monotonia=='Bastante monótono':
        holgura+= 1
    elif monotonia=='Muy monótono':
        holgura+=4
    
    if tedio=='Bastante aburrido':
        holgura+= 1
    elif tedio=='Muy aburrido':
        holgura+=2
    return holgura