"""
Schemas de Pydantic para Usuario
"""

from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field, field_validator
import re


class UsuarioBase(BaseModel):
    """Schema base para Usuario"""

    nombre: str = Field(..., min_length=1, max_length=100)
    apellido: str = Field(..., min_length=1, max_length=100)
    nombre_usuario: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., min_length=1, max_length=255)
    telefono: Optional[str] = Field(None, max_length=20)
    es_admin: bool = False

    @field_validator("email")
    @classmethod
    def validate_email(cls, v):
        """Validar formato de email"""
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, v):
            raise ValueError("Email invalido")
        return v.lower()

    @field_validator("nombre_usuario")
    @classmethod
    def validate_username(cls, v):
        """Validar nombre de usuario"""
        pattern = r"^[a-zA-Z0-9_]{3,20}$"
        if not re.match(pattern, v):
            raise ValueError(
                "Nombre de usuario debe tener 3-20 caracteres alfanumericos"
            )
        return v.lower()


class UsuarioCreate(UsuarioBase):
    """Schema para crear un usuario"""

    contrasena: str = Field(..., min_length=8, max_length=128)


class UsuarioUpdate(BaseModel):
    """Schema para actualizar un usuario"""

    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    apellido: Optional[str] = Field(None, min_length=1, max_length=100)
    nombre_usuario: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[str] = Field(None, min_length=1, max_length=255)
    telefono: Optional[str] = Field(None, max_length=20)
    contrasena: Optional[str] = Field(None, min_length=8, max_length=128)
    es_admin: Optional[bool] = None
    activo: Optional[bool] = None


class UsuarioResponse(UsuarioBase):
    """Schema para respuesta de usuario (sin contrasena)"""

    id_usuario: UUID
    activo: bool
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None

    class Config:
        from_attributes = True


class UsuarioLogin(BaseModel):
    """Schema para login"""

    nombre_usuario: str
    contrasena: str
