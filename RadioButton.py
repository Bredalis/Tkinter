
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
generos = ["Masculino", "Femenino", "Otros"]

def eleccion_genero():

	for i in range(1, 4):

		if opcion.get() == i:			
			genero.config(text = f"Has Elegido {generos[i - 1]}")

# Multimedia de la interfaz

rosado = "pink"

tk.Label(interfaz, text = "Genero :", bg = rosado, pady = 5).pack()

def radio_boton(texto, valor):

	tk.Radiobutton(
		interfaz, text = texto, bg = rosado, activebackground = "skyblue", 
		variable = opcion, value = valor, command = eleccion_genero).pack()

radio_boton(generos[0], 1)
radio_boton(generos[1], 2)
radio_boton("Otras opciones", 3)

# Etiqueta que contiene el resultado

genero = tk.Label(interfaz, bg = rosado)
genero.pack()

interfaz.mainloop()