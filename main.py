import tkinter as tk
from tkinter import messagebox
import gestor_notas

# Inicializar carpeta de notas
gestor_notas.crear_directorio()

def actualizar_lista():
    lista_notas.delete(0, tk.END)
    for nota in gestor_notas.listar_nombres():
        lista_notas.insert(tk.END, nota)

def guardar_nota():
    titulo = entrada_titulo.get().strip()
    contenido = area_texto.get("1.0", tk.END).strip()
    if not contenido:
        messagebox.showwarning("Vacío", "No puedes guardar una nota vacía.")
        return
    try:
        gestor_notas.guardar(titulo, contenido)
        messagebox.showinfo("Guardado", "Nota guardada correctamente.")
        actualizar_lista()
    except ValueError:
        messagebox.showerror("Error", "Título inválido.")

def cargar_nota(event):
    seleccion = lista_notas.curselection()
    if seleccion:
        titulo = lista_notas.get(seleccion[0])
        try:
            contenido = gestor_notas.cargar(titulo)
            area_texto.delete("1.0", tk.END)
            area_texto.insert(tk.END, contenido)
            entrada_titulo.delete(0, tk.END)
            entrada_titulo.insert(0, titulo)
        except FileNotFoundError:
            messagebox.showerror("Error", "La nota no se encuentra.")

# Ventana principal
ventana = tk.Tk()
ventana.title("App de Notas")
ventana.geometry("700x500")
ventana.resizable(False, False)

# Frame principal
frame = tk.Frame(ventana)
frame.pack(fill=tk.BOTH, expand=True)

# Lado izquierdo: lista
frame_izq = tk.Frame(frame, width=200, bg="#f0f0f0")
frame_izq.pack(side=tk.LEFT, fill=tk.Y)

lista_notas = tk.Listbox(frame_izq)
lista_notas.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
lista_notas.bind("<<ListboxSelect>>", cargar_nota)

btn_actualizar = tk.Button(frame_izq, text="Actualizar lista", command=actualizar_lista)
btn_actualizar.pack(pady=5)

# Parte derecha dividida en 3 secciones

frame_der = tk.Frame(frame)
frame_der.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
frame_titulo = tk.Frame(frame_der)
frame_titulo.pack(fill=tk.X, padx=10, pady=5)

entrada_titulo = tk.Entry(frame_titulo, width=40)
entrada_titulo.pack(fill=tk.X)

frame_texto = tk.Frame(frame_der, height=250)
frame_texto.pack(fill=tk.BOTH, expand=True, padx=10)

area_texto = tk.Text(frame_texto, wrap=tk.WORD)
area_texto.pack(fill=tk.BOTH, expand=True)

frame_botones = tk.Frame(frame_der)
frame_botones.pack(fill=tk.X, pady=10)

btn_guardar = tk.Button(frame_botones, text="Guardar Nota", command=guardar_nota)
btn_guardar.pack(side=tk.RIGHT, padx=10)

# Mostrar lista inicial
actualizar_lista()
ventana.mainloop()