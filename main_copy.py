from src.sistema_reservas import SistemaReservas


def mostrar_menu_principal():
    """Función para mostrar el menú principal"""
    print("\n" + "=" * 50)
    print("    SISTEMA DE RESERVAS - RESTAURANTE")
    print("=" * 50)
    print("1. Realizar Reserva")
    print("2. Validar Reservas")
    print("3. Eliminar Reserva")
    print("4. Modificar Reserva")
    print("5. Mostrar Horarios Disponibles")
    print("6. Ver Disponibilidad por Hora")
    print("7. Ver Estadísticas de Reservas")
    print("0. Salir")
    print("=" * 50)


def realizar_reserva(sistema):
    """Función para realizar una nueva reserva"""
    print("\n--- REALIZAR RESERVA ---")

    # Solicitar nombre completo
    nombre = input("Ingrese el nombre completo: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    # Solicitar hora
    hora_input = input("Ingrese la hora (12-22): ").strip()
    if not hora_input.isdigit():
        print("Por favor ingrese un número válido para la hora.")
        return

    hora = int(hora_input)
    if hora < 12 or hora > 22:
        print("La hora debe estar entre 12 y 22 (12 PM a 10 PM).")
        return

    # Solicitar método de pago
    print("\nMétodos de pago disponibles:")
    print("1. efectivo")
    print("2. transferencia")
    print("3. tarjeta credito")

    metodo_numero = input("Ingrese el número del método de pago (1, 2 o 3): ").strip()

    if metodo_numero == "1":
        metodo = "efectivo"
    elif metodo_numero == "2":
        metodo = "transferencia"
    elif metodo_numero == "3":
        metodo = "tarjeta credito"
    else:
        print("Número de método de pago no válido. Debe ser 1, 2 o 3.")
        return

    # Crear la reserva
    if sistema.agregar_reserva(nombre, hora, metodo):
        print(f"\n¡Reserva creada exitosamente!")
        print(f"ID de reserva: {sistema.contador_id - 1}")
    else:
        print(
            "No se pudo crear la reserva por falta de espacio en el horario seleccionado."
        )


def validar_reservas(sistema):
    """Función para mostrar todas las reservas"""
    print("\n--- VALIDAR RESERVAS ---")
    sistema.validar_reservas()


def eliminar_reserva(sistema):
    """Función para eliminar una reserva"""
    print("\n--- ELIMINAR RESERVA ---")

    if not sistema.reservas:
        print("No hay reservas para eliminar.")
        return

    # Mostrar reservas existentes
    sistema.validar_reservas()

    id_input = input("\nIngrese el ID de la reserva a eliminar: ").strip()
    if not id_input.isdigit():
        print("Por favor ingrese un número válido para el ID.")
        return

    id_reserva = int(id_input)
    sistema.eliminar_reserva_por_id(id_reserva)


def modificar_reserva(sistema):
    """Función para modificar una reserva"""
    print("\n--- MODIFICAR RESERVA ---")

    if not sistema.reservas:
        print("No hay reservas para modificar.")
        return

    # Mostrar reservas existentes
    sistema.validar_reservas()

    posicion_input = input("\nIngrese la posición de la reserva a modificar: ").strip()
    if not posicion_input.isdigit():
        print("Por favor ingrese un número válido para la posición.")
        return

    posicion = int(posicion_input)
    sistema.modificar_reserva(posicion)


def main():
    """Función principal del programa"""
    # Crear instancia del sistema de reservas
    sistema = SistemaReservas("Mi Restaurante")

    print("¡Bienvenido al Sistema de Reservas!")

    while True:
        mostrar_menu_principal()

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            realizar_reserva(sistema)
        elif opcion == "2":
            validar_reservas(sistema)
        elif opcion == "3":
            eliminar_reserva(sistema)
        elif opcion == "4":
            modificar_reserva(sistema)
        elif opcion == "5":
            sistema.mostrar_horarios_disponibles()
        elif opcion == "6":
            sistema.mostrar_disponibilidad_por_hora()
        elif opcion == "7":
            sistema.estadisticas_reservas()
        elif opcion == "0":
            print("\n¡Gracias por usar el Sistema de Reservas!")
            break
        else:
            print("Opción no válida. Por favor seleccione una opción del menú.")

        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()
