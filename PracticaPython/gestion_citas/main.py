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
    while True:
        menu()

        opcion = input("Ingrese su opcion: ")
        if opcion == "0":
            print("Salir")
            break


if __name__ == "__main__":
    main()