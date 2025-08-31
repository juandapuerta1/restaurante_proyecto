from src.restaurante import Restaurante

class SistemaReservas(Restaurante):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.horarios_disponibles = list(range(12, 23))  # 12 PM a 10 PM
    
    def agregar_reserva(self, nombre_completo, hora, metodo_pago):
        """Sobrescribe el método de la clase padre con validaciones adicionales"""
        if self._verificar_disponibilidad_hora(hora):
            return super().agregar_reserva(nombre_completo, hora, metodo_pago)
        else:
            print(f"La hora {hora} no está disponible para reservas.")
            return False
    
    def _verificar_disponibilidad_hora(self, hora):
        """Método específico de esta clase para verificar disponibilidad"""
        # Primero verificar que la hora esté en el rango disponible
        if hora not in self.horarios_disponibles:
            return False
        
        # Contar cuántas reservas ya existen para esa hora específica
        reservas_por_hora = sum(1 for reserva in self.reservas if reserva.hora == hora)
        
        # Definir capacidad máxima por hora (5 reservas)
        capacidad_maxima = 5
        
        # Retornar True si hay espacio disponible
        return reservas_por_hora < capacidad_maxima
    
    def mostrar_disponibilidad_por_hora(self):
        """Método para mostrar cuántas reservas hay por cada hora"""
        print(f"\n=== DISPONIBILIDAD POR HORA ===")
        for hora in self.horarios_disponibles:
            reservas_por_hora = sum(1 for reserva in self.reservas if reserva.hora == hora)
            espacios_disponibles = 5 - reservas_por_hora
            estado = "COMPLETO" if espacios_disponibles == 0 else f"{espacios_disponibles} espacios"
            print(f"Hora {hora}:00 - {estado}")
    
    def mostrar_horarios_disponibles(self):
        """Método específico de esta clase"""
        print(f"Horarios disponibles: {self.horarios_disponibles}")
    
    def validar_reservas(self):
        """Sobrescribe el método de la clase padre con información adicional"""
        if not self.reservas:
            print("No hay reservas registradas.")
            return
        
        print(f"\n=== RESERVAS EXISTENTES EN {self.nombre.upper()} ===")
        print(f"Total de reservas: {len(self.reservas)}")
        for i, reserva in enumerate(self.reservas):
            print(f"Posición {i}: {reserva}")
    
    def estadisticas_reservas(self):
        """Método específico de esta clase para mostrar estadísticas"""
        if not self.reservas:
            print("No hay reservas para mostrar estadísticas.")
            return
        
        print(f"\n=== ESTADÍSTICAS DE RESERVAS ===")
        print(f"Total de reservas: {len(self.reservas)}")
        
        # Contar métodos de pago
        metodos_count = {}
        for reserva in self.reservas:
            metodo = reserva.metodo_pago
            metodos_count[metodo] = metodos_count.get(metodo, 0) + 1
        
        print("Métodos de pago utilizados:")
        for metodo, cantidad in metodos_count.items():
            print(f"  {metodo}: {cantidad} reservas")