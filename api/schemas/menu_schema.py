"""
Schemas de Pydantic para Menu
"""

from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field


class MenuBase(BaseModel):
    """Schema base para Menú"""

    nombre: str = Field(..., min_length=1, max_length=200)
    descripcion: Optional[str] = None
    precio: float = Field(..., gt=0)
    disponible: bool = True
    tiempo_preparacion: Optional[int] = Field(
        None, ge=1, description="Tiempo en minutos"
    )
    ingredientes: Optional[str] = None
    alergenos: Optional[str] = None
    categoria_id: UUID
    restaurante_id: UUID


class MenuCreate(MenuBase):
    """Schema para crear menú"""

    pass


class MenuUpdate(BaseModel):
    """Schema para actualizar menú"""

    nombre: Optional[str] = Field(None, min_length=1, max_length=200)
    descripcion: Optional[str] = None
    precio: Optional[float] = Field(None, gt=0)
    disponible: Optional[bool] = None
    tiempo_preparacion: Optional[int] = Field(None, ge=1)
    ingredientes: Optional[str] = None
    alergenos: Optional[str] = None
    categoria_id: Optional[UUID] = None
    restaurante_id: Optional[UUID] = None


class MenuResponse(MenuBase):
    """Schema de respuesta para menú"""

    id_menu: UUID
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None

    class Config:
        from_attributes = True
