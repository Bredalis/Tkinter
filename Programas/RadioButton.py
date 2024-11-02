
"""
Programa para elegir un género
"""

import tkinter as tk

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.config(bg = "pink")
ventana.resizable(False, False)
ventana.title("Elección de género")
ventana.geometry("270x125")
ventana.iconbitmap("../IMG/Genero.ico")

# Variables y opciones de género
opcion = tk.IntVar()
generos = ["Masculino", "Femenino", "Otros"]

# Función para mostrar el género seleccionado
def eleccion_genero():
	seleccion = generos[opcion.get() - 1]
	genero.config(text = f"Has elegido {seleccion.lower()}")

# Etiqueta para el título
tk.Label(ventana, text = "Genero:", bg = "pink", pady = 5).pack()

# Función para crear los botones de opciones de género
def crear_boton(texto, valor):
	tk.Radiobutton(
		ventana, text = texto, bg = "pink", activebackground = "skyblue", 
		variable = opcion, value = valor, command = eleccion_genero).pack()

# Crear botones de selección de género
for i, texto in enumerate(generos, start = 1):
	crear_boton(texto, i)

# Etiqueta para mostrar el género seleccionado
genero = tk.Label(ventana, bg = "pink")
genero.pack()

ventana.mainloop()