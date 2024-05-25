
import tkinter as tk

# Función para obtener el elemento 
# seleccionado y mostrarlo en la etiqueta

def mostrar_seleccion():
    seleccion = cuadro_lista.get(tk.ACTIVE)
    etiqueta.config(text = "Seleccionaste: " + seleccion)

ventana = tk.Tk()
ventana.title("Cuadro De Lista")
ventana.geometry("300x220")

# Crear un cuadro de lista y una etiqueta

cuadro_lista = tk.Listbox(ventana)
cuadro_lista.insert(1, "Opción 1")
cuadro_lista.insert(2, "Opción 2")
cuadro_lista.insert(3, "Opción 3")
cuadro_lista.pack()

button = tk.Button(ventana, text = "Mostrar selección", 
    command = mostrar_seleccion)
button.pack()

etiqueta = tk.Label(ventana)
etiqueta.pack()

ventana.mainloop()