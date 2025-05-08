import os

RUTA_NOTAS = "notas"

def crear_directorio():
    if not os.path.exists(RUTA_NOTAS):
        os.makedirs(RUTA_NOTAS)

def listar_nombres():
    return sorted(f.replace(".txt", "") for f in os.listdir(RUTA_NOTAS) if f.endswith(".txt"))

def guardar(titulo, contenido):
    if not titulo.strip():
        raise ValueError("Título vacío")
    with open(os.path.join(RUTA_NOTAS, f"{titulo}.txt"), "w", encoding="utf-8") as f:
        f.write(contenido)

def cargar(titulo):
    ruta = os.path.join(RUTA_NOTAS, f"{titulo}.txt")
    if not os.path.exists(ruta):
        raise FileNotFoundError
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read()