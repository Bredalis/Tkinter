
import tkinter as tk
from tkinter import ttk

def agregar_elemento():
    arbol.insert("", tk.END, values = (entrada.get()))

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Lista con Treeview")
ventana.geometry("280x330")
ventana.resizable(False, False)

# Entry para ingresar el elemento
entrada = ttk.Entry(ventana, width = 30)
entrada.pack(pady = 10)

# Botón para agregar elementos
boton_agregar = ttk.Button(ventana, text = "Agregar elemento", 
    command = agregar_elemento)
boton_agregar.pack(pady = 5)

# Crear Treeview para mostrar elementos
arbol = ttk.Treeview(ventana, columns = ("Elemento"), show = "headings")
arbol.heading("Elemento", text = "Elemento")
arbol.pack()

ventana.mainloop()