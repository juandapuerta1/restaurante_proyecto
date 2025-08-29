from reserva import Reserva

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
        
        print("\n=== RESERVAS EXISTENTES ===")
        for i, reserva in enumerate(self.reservas):
            print(f"Posición {i}: {reserva}")
    
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
