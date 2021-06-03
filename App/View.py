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

def traerTiempos():
    return cont.traerTiempos()

def abrir_reporte(nombre):
    cont.abrir_reporte(nombre)

def escribir_reporte (mensaje):
    cont.escribir_reporte(mensaje)

def escribir_linea():
    cont.escribir_linea()
    
def cerrar_reporte():
    cont.cerrar_reporte()

def guardarResultados(path):
    cont.guardarResultados(path)

def guardarlineas(linea):
    cont.guardarlineas(linea)

"""
print(nueva_tarea("Prueba test tarea","AUTO","2").nombre,nueva_tarea("B","AUTO","2").nombre,nueva_tarea("C","AUTO","2").nombre )
agregarPredecesor(getObjectbyName("B"),"Prueba test tarea")
    cont.dibujarGrafo()
"""
print(nueva_tarea("A","AUTO","2").nombre,nueva_tarea("C","AUTO","2").nombre)
#nueva_tarea("C","AUTO","2").nombre,nueva_tarea("D","AUTO","2").nombre 
agregarPredecesor(getObjectbyName("C"),"A")
#agregarPredecesor(getObjectbyName("C"),"B")
print(getTareasNombres())
print(getObjectbyName("C").nombre)
print(getObjectbyName("C").predecesores)
#print(getSucesores("A"))
#dibujarGrafo()
"""
agregarTiempo("A",1,5)
agregarTiempo("B",1,10)
agregarTiempo("C",1,15)
agregarTiempo("D",1,15)
agregarTiempo("B","Pedro",5)
agregarTiempo("A","Pedro",10)
agregarTiempo("D","Pedro",10)

agregarTiempo("A","Valentina",15)
agregarTiempo("B","Valentina",5)
agregarTiempo("B","Valentina",15)
agregarTiempo("C","Valentina",15)
agregarTiempo("D","Valentina",15)

agregarTiempo("A","Juan",5)
agregarTiempo("B","Juan",15)
agregarTiempo("B","Juan",5)
agregarTiempo("B","Juan",10)
agregarTiempo("D","Juan",10)
agregarTiempo("C","Juan",5)
agregarTiempo("C","Juan",10)
agregarTiempo("C","Pedro",5)
agregarTiempo("C","Pedro",10)
agregarSexo("Hombre","Pedro")

agregarSexo("Mujer","Valentina")
agregarSexo("Hombre","Juan")
agregarSexo("Mujer",1)

agregarFNivelacion("A","Valentina", 100)
agregarFNivelacion("B","Juan", 105)
agregarFNivelacion("C","Pedro", 80)
agregarFNivelacion("B","Pedro", 80)
agregarFNivelacion("D","Pedro", 80)
agregarFNivelacion("A","Pedro", 80)
agregarFNivelacion("A",1, 100)
agregarFNivelacion("B",1, 100)
agregarFNivelacion("C",1, 100)
agregarFNivelacion("D",1, 100)
agregarFNivelacion("A","Juan", 105)
agregarFNivelacion("C","Juan", 80)
agregarFNivelacion("D","Juan", 100)

agregarFNivelacion("B","Valentina", 105)
agregarFNivelacion("C","Valentina", 105)
agregarFNivelacion("D","Valentina", 105)
"""