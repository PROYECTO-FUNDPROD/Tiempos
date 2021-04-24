from tkinter import messagebox as mb

def doMessageBox(titulo,mensaje,icono, accionsi,accionno):
    MsgBox = mb.askquestion (titulo,mensaje,icon =icono)
    if MsgBox == 'yes':
       accionsi()
    else:
       accionno()