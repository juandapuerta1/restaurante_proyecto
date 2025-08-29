class Reserva:
    def __init__(self, id_reserva, nombre_completo, hora, metodo_pago):
        self.id_reserva = id_reserva
        self.nombre_completo = nombre_completo
        self.hora = hora
        self.metodo_pago = metodo_pago
    
    def __str__(self):
        return f"ID: {self.id_reserva} | Nombre: {self.nombre_completo} | Hora: {self.hora} | Método de pago: {self.metodo_pago}"
    
    def modificar_reserva(self, nombre_completo=None, hora=None, metodo_pago=None):
        if nombre_completo is not None:
            self.nombre_completo = nombre_completo
        if hora is not None:
            self.hora = hora
        if metodo_pago is not None:
            self.metodo_pago = metodo_pago
