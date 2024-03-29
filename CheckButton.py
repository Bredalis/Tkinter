
# Interfaz para elegir 
# un lugar para viajar

import tkinter as tk

interfaz = tk.Tk()
tk.Wm.wm_title(interfaz, 'Lugares Para Viajar')
interfaz.config(bg = 'pink')
interfaz.geometry('270x120')
interfaz.resizable(0, 0)

icono = 'C:/Users/Bradalis/Desktop/LenguajesDeProgramacion/Icon/Imagenes/Avion.ico'
interfaz.iconbitmap(icono)

playa = tk.IntVar()
monte = tk.IntVar()
turismo_rural = tk.IntVar()

# Funcion que muestra 
# los lugares para elegir

def Elige_Viaje():

	opcion = ''

	if(playa.get() == 1):		
		opcion += 'Playa'

	if (monte.get() == 1):
		opcion += ' Montaña'

	if (turismo_rural.get() == 1):
		opcion += ' Turismo Rural'

	lugares.config(text = opcion)

# Multimedia de la interfaz

rosado = 'pink'

tk.Label(interfaz, text = 'Elige Destino', width = 20, bg = rosado).pack()

tk.Checkbutton(
	interfaz, text = 'Playa', variable = playa, onvalue = 1, 
	offvalue = 0, bg = rosado, command = Elige_Viaje).pack()

tk.Checkbutton(
	interfaz, text = 'Motaña', variable = monte, onvalue = 1, 
	offvalue = 0, bg = rosado, command = Elige_Viaje).pack()

tk.Checkbutton(
	interfaz, text = 'Turismo Rural', variable = turismo_rural, onvalue = 1, 
	offvalue = 0, bg = rosado, command = Elige_Viaje).pack()

# Etiqueta que contiene el lugar elegido

lugares = tk.Label(interfaz, bg = rosado, pady = 10)
lugares.pack(side = 'bottom')

interfaz.mainloop()