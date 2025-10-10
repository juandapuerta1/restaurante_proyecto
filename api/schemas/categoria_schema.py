"""
Schemas de Pydantic para Categoria
"""

from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field


class CategoriaBase(BaseModel):
    """Schema base para Categoria"""

    nombre: str = Field(..., min_length=1, max_length=100)
    descripcion: Optional[str] = None


class CategoriaCreate(CategoriaBase):
    """Schema para crear una categoría"""

    pass


class CategoriaUpdate(BaseModel):
    """Schema para actualizar una categoría"""

    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    descripcion: Optional[str] = None
    activa: Optional[bool] = None


class CategoriaResponse(CategoriaBase):
    """Schema para respuesta de categoría"""

    id_categoria: UUID
    activa: bool
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None

    class Config:
        from_attributes = True
