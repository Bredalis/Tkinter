
"""
Programa para elegir un lugar para viajar
"""

import tkinter as tk

# Configuración de la ventana principal
ventana = tk.Tk()
tk.Wm.wm_title(ventana, "Lugares para viajar")
ventana.config(bg = "pink")
ventana.geometry("270x150")
ventana.resizable(False, False)
ventana.iconbitmap("../IMG/Avion.ico")

# Variables para las opciones de viaje
playa = tk.IntVar()
monte = tk.IntVar()
turismo_rural = tk.IntVar()

# Función para elegir los lugares
def elige_viaje():
	opcion = []

	if(playa.get() == 1):		
		opcion.append("Playa")

	if (monte.get() == 1):
		opcion.append("Montaña")

	if (turismo_rural.get() == 1):
		opcion.append("Turismo Rural")

	lugares.config(text = " ".join(opcion))

# Etiqueta para el título
tk.Label(ventana, text = "Elige tu destino:", width = 20, bg = "pink").pack(pady = 10)

def crear_boton(texto, variable):
	tk.Checkbutton(
		ventana, text = texto, variable = variable, onvalue = 1, 
		offvalue = 0, bg = "pink", command = elige_viaje).pack()

# Crear botones para las opciones
crear_boton("Playa", playa)
crear_boton("Motaña", monte)
crear_boton("Turismo Rural", turismo_rural)

# Etiqueta que muestra el lugar elegido
lugares = tk.Label(ventana, bg = "pink", pady = 10)
lugares.pack(side = "bottom")

ventana.mainloop()