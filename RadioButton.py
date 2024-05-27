
# Elegir un genero

import tkinter as tk

interfaz = tk.Tk()
interfaz.config(bg = "pink")
interfaz.resizable(0, 0)
interfaz.title("Eleccion De Genero")
interfaz.geometry("270x125")
interfaz.iconbitmap("Genero.ico")

# Muestra el resultado de la eleccion un genero

opcion = tk.IntVar()

def eleccion_genero():

	complemento = "Has Elegido"
	
	if opcion.get() == 1:			
		genero.config(text = f"{complemento} Masculino")

	elif opcion.get() == 2:
	    genero.config(text = f"{complemento} Femenina")

	else:		
		genero.config(text = f"{complemento} Otros")

# Multimedia de la interfaz

rosado = "pink"
azul_cielo = "skyblue"

tk.Label(interfaz, text = "Genero :", bg = rosado, pady = 5).pack()

def radio_boton(texto, valor):

	tk.Radiobutton(
		interfaz, text = texto, bg = rosado, activebackground = azul_cielo, 
		variable = opcion, value = valor, command = eleccion_genero).pack()

radio_boton("Masculino", 1)
radio_boton("Femenino", 2)
radio_boton("Otras opciones", 3)

# Etiqueta que contiene el resultado

genero = tk.Label(interfaz, bg = rosado)
genero.pack()

interfaz.mainloop()