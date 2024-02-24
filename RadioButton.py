
# Interfaz para 
# elegir un genero

import tkinter as tk

interfaz = tk.Tk()
interfaz.config(bg = 'pink')
interfaz.resizable(0, 0)
interfaz.title('Eleccion De Genero')
interfaz.geometry('270x125')

icono = 'C:/Users/Bradalis/Desktop/LenguajesDeProgramacion/Icon/Imagenes/Genero.ico'
interfaz.iconbitmap(icono)

# Funcion que muestra el 
# resultado de haber elegido un genero

opcion = tk.IntVar()

def eleccion_genero():

	complemento = 'Has Elegido'
	
	if opcion.get() == 1:			
		genero.config(text = f'{complemento} Masculino')

	elif opcion.get() == 2:
	    genero.config(text = f'{complemento} Femenina')

	else:		
		genero.config(text = f'{complemento} Otros')

# Multimedia de la interfaz

rosado = 'pink'
azul_cielo = 'skyblue'

tk.Label(interfaz, text = 'Genero :', bg = rosado, pady = 5).pack()

tk.Radiobutton(
	interfaz, text = 'Masculino', bg = rosado, activebackground = azul_cielo, 
	variable = opcion, value = 1, command = eleccion_genero).pack()

tk.Radiobutton(
	interfaz, text = 'Femenino', bg = rosado, activebackground = azul_cielo,
	variable = opcion, value = 2, command = eleccion_genero).pack()

tk.Radiobutton(
	interfaz, text = 'Otras opciones', bg = rosado, activebackground = azul_cielo,
	variable = opcion, value = 3, command = eleccion_genero).pack()

# Etiqueta que contiene el resultado

genero = tk.Label(interfaz, bg = rosado)
genero.pack()

interfaz.mainloop()