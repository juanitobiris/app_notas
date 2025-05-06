#main.py
from gestor_notas import agregar_nota, buscar_notas, listar_notas

def mostrar_menu():
    print("\n=== APP DE NOTAS ===")
    print("1. Agregar nota")
    print("2. Buscar notas")
    print("3. Ver todas las notas")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        titulo = input("Título de la nota: ")
        contenido = input("Contenido: ")
        agregar_nota(titulo, contenido)
        print("✅ Nota guardada.")
    elif opcion == "2":
        palabra = input("Buscar por palabra clave: ")
        resultados = buscar_notas(palabra)
        if resultados:
            for nota in resultados:
                print(f"\n📌 {nota['titulo']} ({nota['fecha']})\n{nota['contenido']}")
        else:
            print("🔍 No se encontraron notas.")
    elif opcion == "3":
        notas = listar_notas()
        if notas:
            for nota in notas:
                print(f"\n📝 {nota['titulo']} ({nota['fecha']})\n{nota['contenido']}")
        else:
            print("📂 No hay notas aún.")
    elif opcion == "4":
        print("👋 Hasta luego.")
        break
    else:
        print("❌ Opción no válida.")