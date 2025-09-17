"""
Modelo de Reserva
"""

import uuid
from typing import Any

from database.config import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Reserva(Base):
    __tablename__ = "reservas"

    id_reserva = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )
    nombre_completo = Column(String(200), nullable=False)
    telefono = Column(String(20), nullable=True)
    email = Column(String(255), nullable=True)
    fecha_reserva = Column(DateTime(timezone=True), nullable=False)
    hora_reserva = Column(String(10), nullable=False)  # "19:30"
    numero_personas = Column(Integer, nullable=False, default=1)
    metodo_pago = Column(String(50), nullable=False)  # "efectivo", "transferencia", "tarjeta credito"
    estado = Column(String(20), default="pendiente")  # "pendiente", "confirmada", "cancelada", "completada"
    observaciones = Column(Text, nullable=True)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())

    # Claves foráneas
    usuario_id = Column(
        UUID(as_uuid=True), ForeignKey("usuarios.id_usuario"), nullable=True
    )
    restaurante_id = Column(
        UUID(as_uuid=True), ForeignKey("restaurantes.id_restaurante"), nullable=False
    )
    mesa_id = Column(
        UUID(as_uuid=True), ForeignKey("mesas.id_mesa"), nullable=True
    )

    # Relaciones
    usuario = relationship("Usuario", back_populates="reservas")
    restaurante = relationship("Restaurante", back_populates="reservas")
    mesa = relationship("Mesa", back_populates="reservas")

    def __repr__(self):
        return f"<Reserva(id_reserva={self.id_reserva}, nombre='{self.nombre_completo}', fecha={self.fecha_reserva}, hora={self.hora_reserva})>"
