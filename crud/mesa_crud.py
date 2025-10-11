"""
Operaciones CRUD para Mesa
"""

from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from database.models.mesa import Mesa


class MesaCRUD:
    def __init__(self, db: Session):
        self.db = db

    # ---------- CREAR ----------
    def crear_mesa(
        self,
        numero_mesa: int,
        capacidad: int,
        ubicacion: Optional[str],
        activa: bool,
        restaurante_id: UUID,
    ) -> Mesa:
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor a 0")

        mesa = Mesa(
            numero_mesa=numero_mesa,
            capacidad=capacidad,
            ubicacion=ubicacion,
            activa=activa,
            restaurante_id=restaurante_id,
        )
        self.db.add(mesa)
        self.db.commit()
        self.db.refresh(mesa)
        return mesa

    # ---------- OBTENER ----------
    def obtener_mesa(self, mesa_id: UUID) -> Optional[Mesa]:
        return self.db.query(Mesa).filter(Mesa.id_mesa == mesa_id).first()

    def obtener_mesas(self, skip: int = 0, limit: int = 100) -> List[Mesa]:
        return self.db.query(Mesa).offset(skip).limit(limit).all()

    # ---------- ACTUALIZAR ----------
    def actualizar_mesa(self, mesa_id: UUID, **kwargs) -> Optional[Mesa]:
        mesa = self.obtener_mesa(mesa_id)
        if not mesa:
            return None

        for key, value in kwargs.items():
            if hasattr(mesa, key):
                setattr(mesa, key, value)

        self.db.commit()
        self.db.refresh(mesa)
        return mesa

    # ---------- ELIMINAR ----------
    def eliminar_mesa(self, mesa_id: UUID) -> bool:
        mesa = self.obtener_mesa(mesa_id)
        if mesa:
            self.db.delete(mesa)
            self.db.commit()
            return True
        return False
