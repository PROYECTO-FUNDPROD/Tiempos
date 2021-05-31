from tkinter import messagebox as mb

def doMessageBox(titulo,mensaje, icono , accionsi,accionno):
    MsgBox = mb.askquestion (titulo,mensaje,icon =icono)
    if MsgBox == 'yes':
       accionsi()
    else:
       accionno()

def okMessageBox (titulo, mensaje, icono):
   mb.showinfo(titulo,mensaje, icon=  icono)
