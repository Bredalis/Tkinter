
import tkinter as tk

# Función para mostrar el elemento 
# seleccionado en la etiqueta
def mostrar_seleccion():
    seleccion = cuadro_lista.get(tk.ACTIVE)
    etiqueta.config(text = f"Seleccionaste: {seleccion}")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Cuadro de lista")
ventana.geometry("300x220")

# Crear cuadro de lista
cuadro_lista = tk.Listbox(ventana)

for i in range(1, 4):
    cuadro_lista.insert(i, f"Opción {i}")
cuadro_lista.pack()

# Botón para mostrar la selección
boton_mostrar = tk.Button(ventana, text = "Mostrar selección", 
    command = mostrar_seleccion)
boton_mostrar.pack()

# Etiqueta para mostrar la selección
etiqueta = tk.Label(ventana)
etiqueta.pack()

ventana.mainloop()