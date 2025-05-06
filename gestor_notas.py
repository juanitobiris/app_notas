#gestor_notas.py
import json
import os
from datetime import datetime

ARCHIVO_NOTAS = "notas.json"

def cargar_notas():
    if not os.path.exists(ARCHIVO_NOTAS):
        return []
    with open(ARCHIVO_NOTAS, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_notas(notas):
    with open(ARCHIVO_NOTAS, "w", encoding="utf-8") as f:
        json.dump(notas, f, indent=4, ensure_ascii=False)

def agregar_nota(titulo, contenido):
    notas = cargar_notas()
    nueva_nota = {
        "titulo": titulo,
        "contenido": contenido,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    notas.append(nueva_nota)
    guardar_notas(notas)

def buscar_notas(palabra_clave):
    notas = cargar_notas()
    return [nota for nota in notas if palabra_clave.lower() in nota["titulo"].lower() or palabra_clave.lower() in nota["contenido"].lower()]

def listar_notas():
    return cargar_notas()