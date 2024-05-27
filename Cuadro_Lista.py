
import tkinter as tk

# Obtener y mostrar en la etiqueta 
# el elemento seleccionado 

def mostrar_seleccion():
    seleccion = cuadro_lista.get(tk.ACTIVE)
    etiqueta.config(text = "Seleccionaste: " + seleccion)

ventana = tk.Tk()
ventana.title("Cuadro De Lista")
ventana.geometry("300x220")

# Crear un cuadro de lista y una etiqueta

cuadro_lista = tk.Listbox(ventana)

for i in range(1, 4):
    cuadro_lista.insert(i, f"Opción {i}")
cuadro_lista.pack()

button = tk.Button(ventana, text = "Mostrar selección", 
    command = mostrar_seleccion)
button.pack()

etiqueta = tk.Label(ventana)
etiqueta.pack()

ventana.mainloop()