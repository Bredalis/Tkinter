
import tkinter as tk

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Saludo")
ventana.resizable(False, False)
ventana.iconbitmap("../IMG/Python.ico")

# Etiqueta de saludo
tk.Label(
	ventana, 
	text = "Hola Mundo De La Programación", 
	fg = "#884EA0",
	font = ("Arial", 25), 
	bg = "pink", 
	padx = 10, 
	pady = 10
).pack()

ventana.mainloop()