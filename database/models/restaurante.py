"""
Modelo de Restaurante
"""

import uuid
from typing import Any

from database.config import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Restaurante(Base):
    __tablename__ = "restaurantes"

    id_restaurante = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )
    nombre = Column(String(200), nullable=False)
    direccion = Column(Text, nullable=False)
    telefono = Column(String(20), nullable=True)
    email = Column(String(255), nullable=True)
    capacidad_maxima = Column(Integer, default=50)
    horario_apertura = Column(String(10), nullable=False)  # "12:00"
    horario_cierre = Column(String(10), nullable=False)    # "22:00"
    activo = Column(Boolean, default=True)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())

    usuario_admin_id = Column(
        UUID(as_uuid=True), ForeignKey("usuarios.id_usuario"), nullable=False
    )

    usuario_admin = relationship("Usuario", back_populates="restaurantes")
    mesas = relationship("Mesa", back_populates="restaurante")
    reservas = relationship("Reserva", back_populates="restaurante")
    menus = relationship("Menu", back_populates="restaurante")

    def __repr__(self):
        return f"<Restaurante(id_restaurante={self.id_restaurante}, nombre='{self.nombre}', capacidad={self.capacidad_maxima})>"
