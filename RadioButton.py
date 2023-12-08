
"""
Interfaz para 
elegir un genero
"""

import tkinter as tk

interfaz = tk.Tk()
interfaz.config(bg = 'pink')
interfaz.resizable(0,0)
interfaz.title("Elecciones")
interfaz.geometry("225x125")

# Icono

interfaz.iconbitmap("C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Icon/Imagenes/Genero.ico")

"""
Funcion que muestra 
el resultado de 
haber elegido un genero
"""

opcion = tk.IntVar()

def Eleccion():
	
	if opcion.get() == 1:			
		genero.config(text = "Has Elegido Masculino")

	elif opcion.get() == 2:
	    genero.config(text = "Has Elegido Femenina")

	else:		
		genero.config(text = "Has Elegido Otros")

# Multimedia de la interfaz

rosado = 'pink'
azul_cielo = 'skyblue'

tk.Label(interfaz, text = "Genero :", bg = rosado).pack()

tk.Radiobutton(interfaz, text = "Masculino", bg = rosado, activebackground = azul_cielo, variable = opcion, value = 1, command = Eleccion).pack()
tk.Radiobutton(interfaz, text = "Femenino" , bg = rosado, activebackground = azul_cielo, variable = opcion, value = 2, command = Eleccion).pack()
tk.Radiobutton(interfaz, text = "Otras opciones", bg = rosado, activebackground = azul_cielo, variable = opcion, value = 3, command = Eleccion).pack()

# Etiqueta que contiene el resultado

genero = tk.Label(interfaz, bg = rosado)
genero.pack()

interfaz.mainloop()