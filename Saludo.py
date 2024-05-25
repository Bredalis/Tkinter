
# Programa que muestra una 
# interfaz con un saludo

import tkinter as tk

interfaz = tk.Tk()
tk.Wm.wm_title(interfaz, "Saludo")
interfaz.resizable(0, 0)

icono = "Python.ico"
interfaz.iconbitmap(icono)

tk.Label(
	interfaz, text = "Hola Mundo De La Programacion", fg = "#884EA0",
	font = (25), bg = "pink", padx = 10, pady = 10).pack()

interfaz.mainloop()