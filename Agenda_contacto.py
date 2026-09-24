# Agenda de contactos usando un diccionario (nombre -> teléfono)

contactos = {}


def agregar_contacto():
    nombre = input("Nombre del contacto: ").strip().title()
    telefono = input("Número telefónico: ").strip()

    if nombre == "" or telefono == "":
        print("El nombre y el teléfono no pueden estar vacíos.")
        return

    if nombre in contactos:
        print(f"'{nombre}' ya existía; se actualizó su número.")
    else:
        print(f"Contacto '{nombre}' agregado correctamente.")

    contactos[nombre] = telefono


def mostrar_contactos():
    if len(contactos) == 0:
        print("La agenda está vacía.")
        return

    print("\n--- AGENDA DE CONTACTOS ---")
    numero = 1
    for nombre, telefono in contactos.items():
        print(f"{numero}. {nombre} -> {telefono}")
        numero += 1
    print(f"Total de contactos: {len(contactos)}")


def buscar_contacto():
    nombre = input("Nombre a buscar: ").strip().title()

    if nombre in contactos:
        print(f"Encontrado: {nombre} -> {contactos[nombre]}")
    else:
        print(f"No se encontró a '{nombre}' en la agenda.")


def eliminar_contacto():
    nombre = input("Nombre a eliminar: ").strip().title()

    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto '{nombre}' eliminado.")
    else:
        print(f"No se encontró a '{nombre}' en la agenda.")


def menu():
    opcion = ""
    while opcion != "5":
        print("\n===== AGENDA =====")
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "3":
            buscar_contacto()
        elif opcion == "4":
            eliminar_contacto()
        elif opcion == "5":
            print("¡Hasta pronto!")
        else:
            print("Opción no válida, intenta de nuevo.")


menu()