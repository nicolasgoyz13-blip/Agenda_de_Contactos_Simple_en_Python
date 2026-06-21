contactos = []


def mostrar_contacto():
    for i, contacto in enumerate(contactos, start=1):
        print(f"\nContacto {i}")
        print(f"Nombre: {contacto['Nombre']}")
        print(f"Apellido: {contacto['Apellido']}")
        print(f"Telefono: {contacto['Telefono']}")

def agregar_contacto():
    nombre = input("Ingrese Nombre: ")
    apellido = input("Ingrese Apellido: ")
    numerotelefono = input("Ingrese Telefono: ")
    contacto = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Telefono": numerotelefono
    }
    contactos.append(contacto)



while True:
    print("""
    1.Agregar Contactos
    2.Mostrar Contactos
    3.Salir""")
    opcion = input("Ingrese opcion: ")
    if opcion =="1":
        agregar_contacto()
    elif opcion =="2":
        mostrar_contacto()
    elif opcion =="3":
        break

