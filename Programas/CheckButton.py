
# Elegir un lugar para viajar

import tkinter as tk

interfaz = tk.Tk()
tk.Wm.wm_title(interfaz, "Lugares Para Viajar")
interfaz.config(bg = "pink")
interfaz.geometry("270x150")
interfaz.resizable(0, 0)
interfaz.iconbitmap("../IMG/Avion.ico")

playa = tk.IntVar()
monte = tk.IntVar()
turismo_rural = tk.IntVar()

# Funcion para elegir los lugares

def Elige_Viaje():

	opcion = ""

	if(playa.get() == 1):		
		opcion += "Playa"

	if (monte.get() == 1):
		opcion += " Montaña"

	if (turismo_rural.get() == 1):
		opcion += " Turismo Rural"

	lugares.config(text = opcion)

# Multimedia de la interfaz

rosado = "pink"
tk.Label(interfaz, text = "Elige Destino", width = 20, bg = rosado).pack(pady = 10)

def botones(texto, variable):

	tk.Checkbutton(
		interfaz, text = texto, variable = variable, onvalue = 1, 
		offvalue = 0, bg = rosado, command = Elige_Viaje).pack()

botones("Playa", playa)
botones("Motaña", monte)
botones("Turismo Rural", turismo_rural)

# Etiqueta que contiene el lugar elegido

lugares = tk.Label(interfaz, bg = rosado, pady = 10)
lugares.pack(side = "bottom")

interfaz.mainloop()