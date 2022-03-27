from Empleado import Empleado
from Cliente import Cliente

emp = Empleado('Guadalupe', 'Costa', '123123', '234234234', 1000)
cli = Cliente('Valentin', 'Costa', '456456', '567567567', 'VIP')


def cargar():
    respuesta = input("Va a agregar un empleado? ")
    nombre = input("Ingrese el nombre ")
    apellido = input("Ingrese el apellido ")
    dni = input("Ingrese el DNI ")
    telefono = input("Ingrese el teléfono ")

    if (respuesta == "si"):
        sueldo = input("Ingrese el sueldo ")
        emp = Empleado(nombre, apellido, dni, telefono, int(sueldo))
        personas.append(emp)
    else:
        categoria = input("Ingrese la categoria del cliente ")
        cli = Cliente(nombre, apellido, dni, telefono, categoria)
        personas.append(cli)

personas = []
cargar()
cargar()
for persona in personas:
    print(persona)