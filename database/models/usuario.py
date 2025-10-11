"""
Modelo de Usuario
"""

import uuid
from database.config import Base
from sqlalchemy import Column, DateTime, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    nombre_usuario = Column(String(50), nullable=False, unique=True, index=True)
    email = Column(String(255), nullable=False, unique=True, index=True)
    telefono = Column(String(20), nullable=True)
    contrasena = Column(String(255), nullable=False)
    es_admin = Column(Boolean, default=False)
    activo = Column(Boolean, default=True)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())

    # Relaciones
    reservas = relationship("Reserva", back_populates="usuario")
    restaurantes = relationship("Restaurante", back_populates="usuario_admin")

    def __repr__(self):
        return (
            f"<Usuario(id_usuario={self.id_usuario}, "
            f"nombre='{self.nombre} {self.apellido}', "
            f"usuario='{self.nombre_usuario}', email='{self.email}')>"
        )
