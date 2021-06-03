# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:04:13 2021

@author: valen
"""

from os import name
import config
import shutil as s
from App.Model import proceso
from App.Model import operario
import networkx as nx
#import graphviz

#from Model import proceso as proceso




list_procesos=[]
list_operarios=[]
tiempos={}
lineas=[]
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

def nuevoOperario(nombre):
    objeto = operario(nombre)
    list_operarios.append(objeto)
    return objeto
    
def validarOperario(name):
    operario=getObjectOperariobyName(name)
    if operario==None:
        nuevoOperario(name)

def getObjectOperariobyName(name):
    objeto=None
    for cada_objeto in list_operarios:
        if cada_objeto.nombre== name:
            objeto=cada_objeto
    return objeto   

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



def guardarCondiciones(trabajo_pie1, postural, peso_levantador,iluminacione, humedadi, concentracione, ruidos, tensione, monotoniai,tedios):
    global trabajo_pie
    trabajo_pie=trabajo_pie1

    global postura
    postura=postural

    global peso_levantado
    peso_levantado= peso_levantador
    
    global iluminacion
    iluminacion= iluminacione
    
    global humedad
    humedad=humedadi
    
    global concentracion
    concentracion=concentracione

    global ruido
    ruido=ruidos

    global tension
    tension=tensione

    global monotonia
    monotonia=monotoniai

    global tedio
    tedio=tedios


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



def agregarFNivelacion(tarea,operario,Fnivelacion):
    tiempos[tarea][operario]["Fnivelacion"]=int(Fnivelacion)  

def agregarSexo(sexo,object):
    object.agregarSexo(sexo)

def definirHolguras():
    for cada_operario in list_operarios:
        asignarHolgura(cada_operario)
    print(list_operarios[0].holgura)

def asignarHolgura(operario):
    if operario.sexo=="Mujer":
        Holgura=CalcularHolguraMujer()
        
    else:
        Holgura=CalcularHolguraHombre()
    operario.asigHolgura(Holgura)

def CalcularHolguraHombre():
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
def CalcularHolguraMujer():
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

def calcularTB_TE_Promedios():
    for cada_tarea in tiempos:
        sum_general=0
        cant=0
        for cada_operario in tiempos[cada_tarea]:
            print(tiempos[cada_tarea][cada_operario])
            basico = tiempos[cada_tarea][cada_operario]["Promedio"]*tiempos[cada_tarea][cada_operario]["Fnivelacion"]/100
            estandar = basico*(1 + (cada_operario.holgura/100))
            tiempos[cada_tarea][cada_operario]["Basico"]=basico
            tiempos[cada_tarea][cada_operario]["Estandar"]=estandar
            sum_general+=estandar
            cant+=1
        prom=sum_general/cant
        tiempos[cada_tarea]["Promedio"]=prom
    
    return tiempos

def traerTiempos():
    return tiempos

def abrir_reporte(nombre):
    global reporte
    reporte=open(nombre,"w+")
    reporte.write ("Resultados Estudio de Tiempos\n")
    reporte.write("----------------------------------------------------\n")

def escribir_reporte (mensaje):
    reporte.write(mensaje)

def escribir_linea():
    reporte.write("----------------------------------------------------\n")
    
    
def cerrar_reporte():
    reporte.close()

def guardarResultados(path):
    print(lineas)
    with open(path,"w") as f1:
        for linea in lineas:
            f1.write(linea)
    f1.close()
def guardarlineas(linea):
    lineas.append(linea)
