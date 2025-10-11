"""
Schemas de Pydantic para Reserva
"""

from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field, EmailStr


class ReservaBase(BaseModel):
    """Schema base para Reserva"""

    nombre_completo: str = Field(..., min_length=1, max_length=200)
    telefono: Optional[str] = Field(None, max_length=20)
    email: Optional[EmailStr] = None
    fecha_reserva: datetime
    hora_reserva: str = Field(..., pattern=r"^\d{2}:\d{2}$")
    numero_personas: int = Field(..., ge=1)
    metodo_pago: str = Field(..., max_length=50)
    estado: Optional[str] = Field(
        "pendiente", pattern=r"^(pendiente|confirmada|cancelada|completada)$"
    )
    observaciones: Optional[str] = None
    usuario_id: Optional[UUID] = None
    restaurante_id: UUID
    mesa_id: Optional[UUID] = None


class ReservaCreate(ReservaBase):
    """Schema para crear una reserva"""

    pass


class ReservaUpdate(BaseModel):
    """Schema para actualizar una reserva"""

    nombre_completo: Optional[str] = Field(None, max_length=200)
    telefono: Optional[str] = Field(None, max_length=20)
    email: Optional[EmailStr] = None
    fecha_reserva: Optional[datetime] = None
    hora_reserva: Optional[str] = Field(None, pattern=r"^\d{2}:\d{2}$")
    numero_personas: Optional[int] = Field(None, ge=1)
    metodo_pago: Optional[str] = Field(None, max_length=50)
    estado: Optional[str] = Field(
        None, pattern=r"^(pendiente|confirmada|cancelada|completada)$"
    )
    observaciones: Optional[str] = None
    usuario_id: Optional[UUID] = None
    restaurante_id: Optional[UUID] = None
    mesa_id: Optional[UUID] = None


class ReservaResponse(ReservaBase):
    """Schema de respuesta para reserva"""

    id_reserva: UUID
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None

    class Config:
        from_attributes = True
