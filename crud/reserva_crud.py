"""
Operaciones CRUD para Reserva
"""

from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from database.models.reserva import Reserva


class ReservaCRUD:
    def __init__(self, db: Session):
        self.db = db

    # ---------- CREAR ----------
    def crear_reserva(
        self,
        nombre_completo: str,
        telefono: Optional[str],
        email: Optional[str],
        fecha_reserva,
        hora_reserva: str,
        numero_personas: int,
        metodo_pago: str,
        estado: str,
        observaciones: Optional[str],
        usuario_id: Optional[UUID],
        restaurante_id: UUID,
        mesa_id: Optional[UUID],
    ) -> Reserva:
        if numero_personas <= 0:
            raise ValueError("El número de personas debe ser mayor que 0")

        reserva = Reserva(
            nombre_completo=nombre_completo.strip(),
            telefono=telefono,
            email=email,
            fecha_reserva=fecha_reserva,
            hora_reserva=hora_reserva,
            numero_personas=numero_personas,
            metodo_pago=metodo_pago.lower().strip(),
            estado=estado,
            observaciones=observaciones,
            usuario_id=usuario_id,
            restaurante_id=restaurante_id,
            mesa_id=mesa_id,
        )

        self.db.add(reserva)
        self.db.commit()
        self.db.refresh(reserva)
        return reserva

    # ---------- OBTENER ----------
    def obtener_reserva(self, reserva_id: UUID) -> Optional[Reserva]:
        return self.db.query(Reserva).filter(Reserva.id_reserva == reserva_id).first()

    def obtener_reservas(self, skip: int = 0, limit: int = 100) -> List[Reserva]:
        return self.db.query(Reserva).offset(skip).limit(limit).all()

    def obtener_reservas_por_restaurante(self, restaurante_id: UUID) -> List[Reserva]:
        return (
            self.db.query(Reserva)
            .filter(Reserva.restaurante_id == restaurante_id)
            .order_by(Reserva.fecha_reserva.desc())
            .all()
        )

    # ---------- ACTUALIZAR ----------
    def actualizar_reserva(self, reserva_id: UUID, **kwargs) -> Optional[Reserva]:
        reserva = self.obtener_reserva(reserva_id)
        if not reserva:
            return None

        for key, value in kwargs.items():
            if hasattr(reserva, key):
                setattr(reserva, key, value)

        self.db.commit()
        self.db.refresh(reserva)
        return reserva

    # ---------- ELIMINAR ----------
    def eliminar_reserva(self, reserva_id: UUID) -> bool:
        reserva = self.obtener_reserva(reserva_id)
        if reserva:
            self.db.delete(reserva)
            self.db.commit()
            return True
        return False
