
"""
Interfaz para 
elegir un lugar 
para viajar
"""

import tkinter as tk

interfaz = tk.Tk()
tk.Wm.wm_title(interfaz, "Lugares Para Viajar")
interfaz.config(bg = 'pink')
interfaz.geometry("270x120")
interfaz.resizable(0,0)

interfaz.iconbitmap("C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Icon/Imagenes/Viaje.ico")

"""
Funcion que muestra 
los lugares para elegir
"""

playa = tk.IntVar()
monte = tk.IntVar()
turismo_rural = tk.IntVar()

def Elige_Viaje():

	opcion = ""

	if(playa.get() == 1):		
		opcion += "Playa  "

	if (monte.get() == 1):
		opcion += "Montaña  "

	if (turismo_rural.get() == 1):
		opcion += "Turismo Rural"

	lugares.config(text = opcion)

# Multimedia de la interfaz

rosado = 'pink'

tk.Label(interfaz, text = "Elige Destino", width = 20, bg = rosado).pack()

tk.Checkbutton(interfaz, text = "Playa", variable = playa, onvalue = 1, offvalue = 0, bg = rosado, command = Elige_Viaje).pack()
tk.Checkbutton(interfaz, text = "Motaña", variable = monte, onvalue = 1, offvalue = 0, bg = rosado, command = Elige_Viaje).pack()
tk.Checkbutton(interfaz, text = "Turismo Rural", variable = turismo_rural, onvalue = 1, offvalue = 0, bg = rosado, command = Elige_Viaje).pack()

# Etiqueta que contiene el lugar elegido

lugares = tk.Label(interfaz, bg = rosado)
lugares.pack(side = 'bottom')

interfaz.mainloop()