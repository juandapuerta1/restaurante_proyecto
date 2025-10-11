"""
Operaciones CRUD para Restaurante
"""

from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from database.models.restaurante import Restaurante


class RestauranteCRUD:
    def __init__(self, db: Session):
        self.db = db

    # ---------- CREAR ----------
    def crear_restaurante(
        self,
        nombre: str,
        direccion: str,
        telefono: Optional[str],
        email: Optional[str],
        capacidad_maxima: int,
        horario_apertura: str,
        horario_cierre: str,
        activo: bool,
        usuario_admin_id: UUID,
    ) -> Restaurante:
        if capacidad_maxima <= 0:
            raise ValueError("La capacidad máxima debe ser mayor a 0")

        restaurante = Restaurante(
            nombre=nombre.strip(),
            direccion=direccion.strip(),
            telefono=telefono,
            email=email,
            capacidad_maxima=capacidad_maxima,
            horario_apertura=horario_apertura,
            horario_cierre=horario_cierre,
            activo=activo,
            usuario_admin_id=usuario_admin_id,
        )
        self.db.add(restaurante)
        self.db.commit()
        self.db.refresh(restaurante)
        return restaurante

    # ---------- OBTENER ----------
    def obtener_restaurante(self, restaurante_id: UUID) -> Optional[Restaurante]:
        return (
            self.db.query(Restaurante)
            .filter(Restaurante.id_restaurante == restaurante_id)
            .first()
        )

    def obtener_restaurantes(
        self, skip: int = 0, limit: int = 100
    ) -> List[Restaurante]:
        return self.db.query(Restaurante).offset(skip).limit(limit).all()

    # ---------- ACTUALIZAR ----------
    def actualizar_restaurante(
        self, restaurante_id: UUID, **kwargs
    ) -> Optional[Restaurante]:
        restaurante = self.obtener_restaurante(restaurante_id)
        if not restaurante:
            return None

        for key, value in kwargs.items():
            if hasattr(restaurante, key):
                setattr(restaurante, key, value)

        self.db.commit()
        self.db.refresh(restaurante)
        return restaurante

    # ---------- ELIMINAR ----------
    def eliminar_restaurante(self, restaurante_id: UUID) -> bool:
        restaurante = self.obtener_restaurante(restaurante_id)
        if restaurante:
            self.db.delete(restaurante)
            self.db.commit()
            return True
        return False
