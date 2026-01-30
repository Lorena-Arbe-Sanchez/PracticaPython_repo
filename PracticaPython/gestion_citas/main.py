# TODO : Poner según errores de abajo
"""
from gestion_citas.models.cliente import Cliente
from gestion_citas.models.empleado import Empleado
from gestion_citas.repositories.citas_repository import CitasRepository
from gestion_citas.services.gestor_citas import GestorCitas
from gestion_citas.exceptions.errores import (
    UsuarioInactivoError,
    CitaSolapadaError,
    EstadoCitaError
)
"""
from gestion_citas.models import Cliente, Empleado, Cita
from gestion_citas.repositories import CitasRepository
from gestion_citas.services import GestorCitas
from gestion_citas.exceptions import UsuarioInactivoError, CitaSolapadaError, EstadoCitaError


def menu():
    print(
        "1. Crear cliente\n"
        "2. Crear empleado\n"
        "3. Crear cita\n"
        "4. Confirmar cita\n"
        "5. Cancelar cita\n"
        "6. Ver citas de un empleado\n"
        "7. Ver citas de un cliente\n"
        "0. Salir")

def main():
    repositorio = CitasRepository()
    gestor = GestorCitas(repositorio)

    clientes = []
    empleados = []
    citas = []

    while True:
        menu()

        opcion = input("Teclea el número de la opción que quieras ejecutar: ")

        try:
            if opcion == "0":
                print("Saliendo del programa...")
                break

            elif opcion == "1":
                id = input("ID cliente: ")
                nombre = input("Nombre: ")
                email = input("Email: ")
                telefono = input("Teléfono: ")

                cliente = Cliente(id, nombre, email, telefono)
                clientes.append(cliente)
                print("✅ Cliente creado correctamente.")

            elif opcion == "2":
                id = input("ID empleado: ")
                nombre = input("Nombre: ")
                email = input("Email: ")
                especialidad = input("Especialidad: ")

                empleado = Empleado(id, nombre, email, especialidad)
                empleados.append(empleado)
                print("✅ Empleado creado correctamente.")

            elif opcion == "3":
                id = input("ID cita: ")

                print("Clientes disponibles:")
                for i, c in enumerate(clientes):
                    print(f"{i} - {c.nombre}")

                cliente = clientes[int(input("Seleccione cliente: "))]

                print("Empleados disponibles:")
                for i, e in enumerate(empleados):
                    print(f"{i} - {e.nombre}")

                empleado = empleados[int(input("Seleccione empleado: "))]

                fecha = input("Fecha (YYYY-MM-DD): ")
                hora = input("Hora (HH:MM): ")

                cita = gestor.crear_cita(id, cliente, empleado, fecha, hora)
                citas.append(cita)
                print("✅ Cita creada correctamente.")

            elif opcion == "4":
                for i, c in enumerate(citas):
                    print(f"{i} - {c.fecha} {c.hora} ({c.estado})")

                cita = citas[int(input("Seleccione cita: "))]
                gestor.confirmar_cita(cita)
                print("✅ Cita confirmada.")

            elif opcion == "5":
                for i, c in enumerate(citas):
                    print(f"{i} - {c.fecha} {c.hora} ({c.estado})")

                cita = citas[int(input("Seleccione cita: "))]
                gestor.cancelar_cita(cita)
                print("✅ Cita cancelada.")

            elif opcion == "6":
                for i, e in enumerate(empleados):
                    print(f"{i} - {e.nombre}")

                empleado = empleados[int(input("Seleccione empleado: "))]
                citas_emp = repositorio.obtener_citas_por_empleado(empleado)

                for c in citas_emp:
                    print(c.to_dict())

            elif opcion == "7":
                for i, c in enumerate(clientes):
                    print(f"{i} - {c.nombre}")

                    cliente = clientes[int(input("Seleccione cliente: "))]
                    citas_cli = repositorio.obtener_citas_por_cliente(cliente)

                    for c in citas_cli:
                        print(c.to_dict())

            else:
                print("❌ La opción debe ser un número entre el 0 y el 7.")

        except (UsuarioInactivoError, CitaSolapadaError, EstadoCitaError, ValueError) as e:
            print(f"⚠️ Error: {e}")

        except IndexError:
            print("⚠️ Selección inválida")

if __name__ == "__main__":
    main()