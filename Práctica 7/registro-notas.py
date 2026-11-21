MAX_NOTAS = 5
NOTA_MIN = 0.0
NOTA_MAX = 10.0


def normalizar(nombre):
    """Quita espacios sobrantes del nombre."""
    return " ".join(nombre.split())


def buscar_clave(registro, nombre):
    """Busca el nombre sin distinguir mayúsculas/minúsculas.
    Devuelve la clave real del diccionario o None si no existe."""
    for clave in registro:
        if clave.lower() == nombre.lower():
            return clave
    return None


def agregar_estudiante(registro, nombre):
    nombre = normalizar(nombre)
    if not nombre:
        print("El nombre no puede estar vacío.")
        return
    if buscar_clave(registro, nombre) is not None:
        print(f"El estudiante {nombre} ya existe en el registro.")
        return
    registro[nombre] = []
    print(f"Estudiante {nombre} agregado correctamente.")


def agregar_nota(registro, nombre, nota):
    clave = buscar_clave(registro, normalizar(nombre))
    if clave is None:
        print("El estudiante no existe en el registro.")
        return
    if len(registro[clave]) >= MAX_NOTAS:
        print(f"{clave} ya tiene el máximo de {MAX_NOTAS} notas.")
        return
    registro[clave].append(nota)
    print(f"Nota {nota:g} agregada a {clave}.")


def mostrar_registro(registro):
    if not registro:
        print("El registro está vacío.")
        return
    for nombre, notas in registro.items():
        print(f"{nombre}: {[round(n, 2) for n in notas]}")


def calcular_promedio(registro, nombre):
    clave = buscar_clave(registro, normalizar(nombre))
    if clave is None:
        print("El estudiante no existe en el registro.")
        return
    notas = registro[clave]
    if not notas:
        print(f"{clave} aún no tiene notas registradas.")
        return
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {clave}: {promedio:.2f}")


def leer_nota():
    """Lee una nota válida (número entre 0 y 10). Devuelve None si es inválida."""
    texto = input("Ingrese la nota: ").strip().replace(",", ".")
    try:
        nota = float(texto)
    except ValueError:
        print("Entrada inválida: debe ingresar un número.")
        return None
    if not NOTA_MIN <= nota <= NOTA_MAX:
        print(f"La nota debe estar entre {NOTA_MIN:g} y {NOTA_MAX:g}.")
        return None
    return nota


def mostrar_menu():
    print("--- MENÚ ---")
    print("1. Agregar estudiante")
    print("2. Agregar nota a estudiante")
    print("3. Mostrar registro completo")
    print("4. Mostrar promedio de un estudiante")
    print("5. Salir")


def main():
    registro = {}
    mostrar_menu()
    while True:
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            agregar_estudiante(registro, input("Nombre del estudiante: "))
        elif opcion == "2":
            nombre = input("Nombre del estudiante: ")
            if buscar_clave(registro, normalizar(nombre)) is None:
                print("El estudiante no existe en el registro.")
            else:
                nota = leer_nota()
                if nota is not None:
                    agregar_nota(registro, nombre, nota)
        elif opcion == "3":
            mostrar_registro(registro)
        elif opcion == "4":
            calcular_promedio(registro, input("Nombre del estudiante: "))
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Elige un número del 1 al 5.")
        print()


if __name__ == "__main__":
    main()