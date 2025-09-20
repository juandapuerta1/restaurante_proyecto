from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from database.models.reserva import Reserva


class ReservaCRUD:
    def __init__(self, db: Session):
        """
        Clase para manejar operaciones CRUD de la entidad Reserva.
        """
        self.db = db

    def crear_reserva(self, nombre_completo: str, fecha_reserva, hora_reserva: str,
                      numero_personas: int, metodo_pago: str, restaurante_id: UUID,
                      telefono: str = None, email: str = None,
                      observaciones: str = None, usuario_id: UUID = None,
                      mesa_id: UUID = None) -> Reserva:
        """
        Crear una nueva reserva con validaciones.
        """
        if not nombre_completo or len(nombre_completo.strip()) == 0:
            raise ValueError("El nombre completo es obligatorio")

        if numero_personas <= 0:
            raise ValueError("El número de personas debe ser mayor que 0")

        if metodo_pago not in ["efectivo", "transferencia", "tarjeta credito"]:
            raise ValueError("Método de pago inválido")

        reserva = Reserva(
            nombre_completo=nombre_completo.strip(),
            fecha_reserva=fecha_reserva,
            hora_reserva=hora_reserva.strip(),
            numero_personas=numero_personas,
            metodo_pago=metodo_pago,
            restaurante_id=restaurante_id,
            telefono=telefono.strip() if telefono else None,
            email=email.strip() if email else None,
            observaciones=observaciones.strip() if observaciones else None,
            usuario_id=usuario_id,
            mesa_id=mesa_id,
        )
        self.db.add(reserva)
        self.db.commit()
        self.db.refresh(reserva)
        return reserva

    def obtener_reserva(self, reserva_id: UUID) -> Optional[Reserva]:
        """
        Obtener una reserva por su ID.
        """
        return self.db.query(Reserva).filter(Reserva.id_reserva == reserva_id).first()

    def obtener_reservas(self, skip: int = 0, limit: int = 100) -> List[Reserva]:
        """
        Obtener lista de reservas con paginación.
        """
        return self.db.query(Reserva).offset(skip).limit(limit).all()

    def actualizar_reserva(self, reserva_id: UUID, **kwargs) -> Optional[Reserva]:
        """
        Actualizar los datos de una reserva existente con validaciones.
        """
        reserva = self.obtener_reserva(reserva_id)
        if not reserva:
            return None

        if "numero_personas" in kwargs and kwargs["numero_personas"] <= 0:
            raise ValueError("El número de personas debe ser mayor que 0")

        if "metodo_pago" in kwargs and kwargs["metodo_pago"] not in ["efectivo", "transferencia", "tarjeta credito"]:
            raise ValueError("Método de pago inválido")

        for key, value in kwargs.items():
            if hasattr(reserva, key):
                setattr(reserva, key, value)

        self.db.commit()
        self.db.refresh(reserva)
        return reserva

    def eliminar_reserva(self, reserva_id: UUID, soft_delete: bool = False) -> bool:
        """
        Eliminar una reserva.
        Si `soft_delete=True`, se cambia el estado a 'cancelada'.
        Si es False, se borra físicamente.
        """
        reserva = self.obtener_reserva(reserva_id)
        if not reserva:
            return False

        if soft_delete:
            reserva.estado = "cancelada"
            self.db.commit()
        else:
            self.db.delete(reserva)
            self.db.commit()

        return True
