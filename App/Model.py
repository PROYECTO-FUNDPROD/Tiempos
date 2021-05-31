# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:03:58 2021

@author: valen
"""
from typing_extensions import Concatenate


class mujer:
    def __init__(self, trabajo_pie, postura, peso_levantado,iluminacion, humedad, concentracion, ruido, tension, monotonia,tedio):
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

        self.holgura= holgura

class hombre:
    def __init__(self, trabajo_pie, postura, peso_levantado,iluminacion, humedad, concentracion, ruido, tension, monotonia,tedio):
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

        self.holgura= holgura








