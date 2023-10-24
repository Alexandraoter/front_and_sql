
from tkinter import *
import datetime
from types import NoneType

#la raiz
app=Tk()
app.title("MODULOS")
app.config(bg="white")
#app.resizable(0,0)
app.geometry("800x500")


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#el frame
Ventana_principal=Frame(app)
Ventana_principal.config(bg='peach puff')
Ventana_principal.config(width="800", height="500")
Ventana_principal.config(cursor="hand2")
Ventana_principal.pack(fill="both", expand="true")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#codigo como tal 
class Estudiante:
    def __init__(self):
        self.Nombre
        self.Apellido
        self.DocumentoIdentidad
        self.Semestre
        self.Jornada





#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        

#Creacion de widgets textos



NOM_text = Label(Ventana_principal, text="Ingrese el nombre:", font="arial 8 bold", bg="linen")
NOM_text.grid(column=0, row=6, sticky=(N, W))
APE_text = Label(Ventana_principal, text="Ingrese el apellido:", font="arial 8 bold", bg="linen")
APE_text.grid(column=0, row=7, sticky=(N, W))
DOCMID_text = Label(Ventana_principal, text="Ingrese el documento de identidad:", font="arial 8 bold", bg="linen")
DOCMID_text.grid(column=0, row=8, sticky=(N, W))
PROG_text = Label(Ventana_principal, text="Ingrese el programa:", font="arial 8 bold", bg="linen")
PROG_text.grid(column=0, row=9, sticky=(N, W))
SEMES_text = Label(Ventana_principal, text="Ingrese el semestre:", font="arial 8 bold", bg="linen")
SEMES_text.grid(column=0, row=10, sticky=(N, W))
JOR_text = Label(Ventana_principal, text="Ingrese la jornada:", font="arial 8 bold", bg="linen")
JOR_text.grid(column=0, row=11, sticky=(N, W))


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Creacion de las entradas de texto
NOM = ""
entrada_NOM = Entry(Ventana_principal, width=10, textvariable=NOM)
entrada_NOM.grid(column=5, row=6, sticky="nw")
APE = ""
entrada_APE = Entry(Ventana_principal, width=10, textvariable=APE)
entrada_APE.grid(column=5, row=7, sticky="nw")
DOCMID = ""
entrada_DOCMID = Entry(Ventana_principal, width=10, textvariable=DOCMID)
entrada_DOCMID.grid(column=5, row=8, sticky="nw")
PROG = ""
entrada_PROG = Entry(Ventana_principal, width=10, textvariable=PROG)
entrada_PROG.grid(column=5, row=9, sticky="nw")
SEMES= ""
entrada_SEMES= Entry(Ventana_principal, width=10, textvariable=SEMES)
entrada_SEMES.grid(column=5, row=10, sticky="nw")
JOR = ""
entrada_JOR = Entry(Ventana_principal, width=10, textvariable=JOR)
entrada_JOR.grid(column=5, row=11, sticky="nw")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def Ingrese_numsala(Ingrese_numsala_entry):
    Ingrese_numsala = Ingrese_numsala()
    Ingrese_numsala = Ingrese_numsala.get()

def Ingrese_numequipo(Ingrese_numequip_entry):
    Ingrese_numequip = Ingrese_numequip.get() or None
    Ingrese_numequip = Ingrese_numequip.get() or None
        

class Sala:
    def __init__(self):
        self.Ingrese_numsala = ""
        self.Ingrese_numequipo = ""
        
Ingrese_numsala =Label(Ventana_principal, text="Ingrese el numero de la sala:", font="arial 8 bold", bg="linen")
Ingrese_numsala.grid(row=13, column=9, sticky="nw")

Ingrese_numsala =Entry(Ventana_principal)
Ingrese_numsala.grid(row=13, column=10, sticky="nw")

Ingrese_numequipo =Label(Ventana_principal, text="Ingrese el numero del equipo:", font="arial 8 bold", bg="linen")
Ingrese_numequipo.grid(row=14, column=11, sticky="nw")

Ingrese_numequipo =Entry(Ventana_principal)
Ingrese_numequipo.grid(row=14, column=12, sticky="nw")





#creacion de botones


    


























































































































































































app.mainloop()


