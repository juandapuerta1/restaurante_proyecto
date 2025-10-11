"""
Schemas de Pydantic para Restaurante
"""

from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field, EmailStr


class RestauranteBase(BaseModel):
    """Schema base para Restaurante"""

    nombre: str = Field(..., min_length=1, max_length=200)
    direccion: str
    telefono: Optional[str] = Field(None, max_length=20)
    email: Optional[EmailStr] = None
    capacidad_maxima: int = Field(..., ge=1)
    horario_apertura: str = Field(..., pattern=r"^\d{2}:\d{2}$")
    horario_cierre: str = Field(..., pattern=r"^\d{2}:\d{2}$")
    activo: bool = True
    usuario_admin_id: UUID


class RestauranteCreate(RestauranteBase):
    """Schema para crear restaurante"""

    pass


class RestauranteUpdate(BaseModel):
    """Schema para actualizar restaurante"""

    nombre: Optional[str] = Field(None, min_length=1, max_length=200)
    direccion: Optional[str] = None
    telefono: Optional[str] = Field(None, max_length=20)
    email: Optional[EmailStr] = None
    capacidad_maxima: Optional[int] = Field(None, ge=1)
    horario_apertura: Optional[str] = Field(None, pattern=r"^\d{2}:\d{2}$")
    horario_cierre: Optional[str] = Field(None, pattern=r"^\d{2}:\d{2}$")
    activo: Optional[bool] = None
    usuario_admin_id: Optional[UUID] = None


class RestauranteResponse(RestauranteBase):
    """Schema de respuesta para restaurante"""

    id_restaurante: UUID
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None

    class Config:
        from_attributes = True
