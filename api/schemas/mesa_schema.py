"""
Schemas de Pydantic para Mesa
"""

from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field


class MesaBase(BaseModel):
    """Schema base para Mesa"""

    numero_mesa: int = Field(..., ge=1)
    capacidad: int = Field(..., ge=1)
    ubicacion: Optional[str] = Field(None, max_length=100)
    activa: bool = True
    restaurante_id: UUID


class MesaCreate(MesaBase):
    """Schema para crear mesa"""

    pass


class MesaUpdate(BaseModel):
    """Schema para actualizar mesa"""

    numero_mesa: Optional[int] = Field(None, ge=1)
    capacidad: Optional[int] = Field(None, ge=1)
    ubicacion: Optional[str] = Field(None, max_length=100)
    activa: Optional[bool] = None
    restaurante_id: Optional[UUID] = None


class MesaResponse(MesaBase):
    """Schema de respuesta para mesa"""

    id_mesa: UUID
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None

    class Config:
        from_attributes = True
