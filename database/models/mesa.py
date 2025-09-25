"""
Modelo de Mesa
"""

import uuid
from typing import Any

from database.config import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Mesa(Base):
    __tablename__ = "mesas"

    id_mesa = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )
    numero_mesa = Column(Integer, nullable=False)
    capacidad = Column(Integer, nullable=False)
    ubicacion = Column(String(100), nullable=True)  # "Ventana", "Centro", "Terraza"
    activa = Column(Boolean, default=True)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())

    restaurante_id = Column(
        UUID(as_uuid=True), ForeignKey("restaurantes.id_restaurante"), nullable=False
    )

    restaurante = relationship("Restaurante", back_populates="mesas")
    reservas = relationship("Reserva", back_populates="mesa")

    def __repr__(self):
        return f"<Mesa(id_mesa={self.id_mesa}, numero={self.numero_mesa}, capacidad={self.capacidad})>"
