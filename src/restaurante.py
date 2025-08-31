from src.reserva import Reserva  # Cambia la ruta de importación para reflejar la nueva ubicación

class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.reservas = []
        self.contador_id = 1

    def agregar_reserva(self, nombre_completo, hora, metodo_pago):
        """Método para agregar una nueva reserva"""
        if self._validar_datos_reserva(nombre_completo, hora, metodo_pago):
            nueva_reserva = Reserva(self.contador_id, nombre_completo, hora, metodo_pago)
            self.reservas.append(nueva_reserva)
            self.contador_id += 1
            return True
        return False

    def _validar_datos_reserva(self, nombre_completo, hora, metodo_pago):
        """Método privado para validar los datos de la reserva"""
        if not nombre_completo or not isinstance(nombre_completo, str):
            return False

        if not isinstance(hora, int) or hora < 12 or hora > 22:
            return False

        metodos_validos = ["efectivo", "transferencia", "tarjeta credito"]
        if metodo_pago not in metodos_validos:
            return False

        return True

    def validar_reservas(self):
        """Método para mostrar todas las reservas existentes"""
        if not self.reservas:
            print("No hay reservas registradas.")
            return

        print("\n=== RESERVAS EXISTENTES EN MI RESTAURANTE ===")
        print(f"Total de reservas: {len(self.reservas)}")
        for i, reserva in enumerate(self.reservas):
            print(f"Posición {i}: ID: {reserva.id_reserva} | Nombre: {reserva.nombre_completo} | Hora: {reserva.hora} | Método de pago: {reserva.metodo_pago}")

    def eliminar_reserva(self, posicion):
        """Método para eliminar una reserva por posición"""
        if 0 <= posicion < len(self.reservas):
            reserva_eliminada = self.reservas.pop(posicion)
            print(f"Reserva eliminada: {reserva_eliminada}")
            return True
        else:
            print("Posición inválida. No se pudo eliminar la reserva.")
            return False

    def eliminar_reserva_por_id(self, id_reserva):
        """Método para eliminar una reserva por ID"""
        for i, reserva in enumerate(self.reservas):
            if reserva.id_reserva == id_reserva:
                reserva_eliminada = self.reservas.pop(i)
                print(f"Reserva eliminada: {reserva_eliminada}")
                return True

        print(f"No se encontró una reserva con ID {id_reserva}.")
        return False

    def modificar_reserva(self, posicion):
        """Método para modificar una reserva existente"""
        if 0 <= posicion < len(self.reservas):
            reserva = self.reservas[posicion]
            print(f"\nModificando reserva: {reserva}")

            # Solicitar nuevos datos
            nuevo_nombre = input("Nuevo nombre completo (Enter para mantener el actual): ").strip()
            nueva_hora = input("Nueva hora (12-22, Enter para mantener la actual): ").strip()
            nuevo_metodo = input("Nuevo método de pago (efectivo/transferencia/tarjeta credito, Enter para mantener el actual): ").strip()

            # Aplicar cambios solo si se proporcionan nuevos valores
            if nuevo_nombre:
                reserva.nombre_completo = nuevo_nombre

            if nueva_hora and nueva_hora.isdigit():
                hora_int = int(nueva_hora)
                if 12 <= hora_int <= 22:
                    reserva.hora = hora_int

            if nuevo_metodo in ["efectivo", "transferencia", "tarjeta credito"]:
                reserva.metodo_pago = nuevo_metodo

            print("Reserva modificada exitosamente.")
            return True
        else:
            print("Posición inválida. No se pudo modificar la reserva.")
            return False

    def modificar_reserva_por_id(self, id_reserva):
        """Método para modificar una reserva existente por ID"""
        reserva = self.obtener_reserva_por_id(id_reserva)
        if reserva:
            print(f"\nModificando reserva: {reserva}")

            # Solicitar nuevos datos
            nuevo_nombre = input("Nuevo nombre completo (Enter para mantener el actual): ").strip()

            # Validar y solicitar la nueva hora en un bucle
            while True:
                nueva_hora = input("Nueva hora (12-22, Enter para mantener la actual): ").strip()
                if not nueva_hora:
                    break  # Mantener la hora actual si se presiona Enter
                if not nueva_hora.isdigit():
                    print("Por favor ingrese un número válido para la hora.")
                    continue
                hora_int = int(nueva_hora)
                if 12 <= hora_int <= 22:
                    reserva.hora = hora_int
                    break
                else:
                    print("La hora debe estar entre 12 y 22 (12 PM a 10 PM).")

            # Validar y solicitar el nuevo método de pago en un bucle
            while True:
                print("\nMétodos de pago disponibles:")
                print("1. efectivo")
                print("2. transferencia")
                print("3. tarjeta credito")
                nuevo_metodo_numero = input("Ingrese el número del nuevo método de pago (1, 2 o 3, Enter para mantener el actual): ").strip()

                if not nuevo_metodo_numero:  # Mantener el método de pago actual si se presiona Enter
                    break
                if nuevo_metodo_numero == "1":
                    reserva.metodo_pago = "efectivo"
                    break
                elif nuevo_metodo_numero == "2":
                    reserva.metodo_pago = "transferencia"
                    break
                elif nuevo_metodo_numero == "3":
                    reserva.metodo_pago = "tarjeta credito"
                    break
                else:
                    print("Por favor ingrese una opción válida (1, 2 o 3).")

            # Aplicar cambios solo si se proporcionan nuevos valores
            if nuevo_nombre:
                reserva.nombre_completo = nuevo_nombre

            print("Reserva modificada exitosamente.")
            return True
        else:
            print(f"No se encontró una reserva con ID {id_reserva}.")
            return False

    def obtener_reserva_por_id(self, id_reserva):
        """Método para buscar una reserva por ID"""
        for reserva in self.reservas:
            if reserva.id_reserva == id_reserva:
                return reserva
        return None

    def obtener_reserva_por_posicion(self, posicion):
        """Método para obtener una reserva por posición"""
        if 0 <= posicion < len(self.reservas):
            return self.reservas[posicion]
        return None