"""
Modelo de Menu
"""

import uuid
from typing import Any

from database.config import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String, Text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Menu(Base):
    __tablename__ = "menus"

    id_menu = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )
    nombre = Column(String(200), nullable=False)
    descripcion = Column(Text, nullable=True)
    precio = Column(Numeric(10, 2), nullable=False)
    disponible = Column(Boolean, default=True)
    tiempo_preparacion = Column(Integer, nullable=True)  # en minutos
    ingredientes = Column(Text, nullable=True)
    alergenos = Column(Text, nullable=True)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())

    # Claves foráneas
    categoria_id = Column(
        UUID(as_uuid=True), ForeignKey("categorias.id_categoria"), nullable=False
    )
    restaurante_id = Column(
        UUID(as_uuid=True), ForeignKey("restaurantes.id_restaurante"), nullable=False
    )

    # Relaciones
    categoria = relationship("Categoria", back_populates="menus")
    restaurante = relationship("Restaurante", back_populates="menus")

    def __repr__(self):
        return f"<Menu(id_menu={self.id_menu}, nombre='{self.nombre}', precio={self.precio})>"
