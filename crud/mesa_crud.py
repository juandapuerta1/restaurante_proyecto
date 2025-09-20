from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from database.models.mesa import Mesa


class MesaCRUD:
    def __init__(self, db: Session):
        """
        Clase para manejar operaciones CRUD de la entidad Mesa.
        """
        self.db = db

    def crear_mesa(
        self,
        numero_mesa: int,
        capacidad: int,
        restaurante_id: UUID,
        ubicacion: Optional[str] = None,
        activa: bool = True,
    ) -> Mesa:
        """
        Crear una nueva mesa con validaciones.
        """
        if numero_mesa <= 0:
            raise ValueError("El número de la mesa debe ser mayor que 0")

        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor que 0")

        if ubicacion and len(ubicacion.strip()) > 100:
            raise ValueError("La ubicación no puede exceder 100 caracteres")

        if self.obtener_mesa_por_numero(numero_mesa, restaurante_id):
            raise ValueError("Ya existe una mesa con ese número en este restaurante")

        mesa = Mesa(
            numero_mesa=numero_mesa,
            capacidad=capacidad,
            ubicacion=ubicacion.strip() if ubicacion else None,
            activa=activa,
            restaurante_id=restaurante_id,
        )
        self.db.add(mesa)
        self.db.commit()
        self.db.refresh(mesa)
        return mesa

    def obtener_mesa(self, mesa_id: UUID) -> Optional[Mesa]:
        """
        Obtener una mesa por su ID (solo si está activa).
        """
        return (
            self.db.query(Mesa)
            .filter(Mesa.id_mesa == mesa_id, Mesa.activa == True)
            .first()
        )

    def obtener_mesa_por_numero(
        self, numero_mesa: int, restaurante_id: UUID
    ) -> Optional[Mesa]:
        """
        Obtener una mesa por su número en un restaurante (solo si está activa).
        """
        return (
            self.db.query(Mesa)
            .filter(
                Mesa.numero_mesa == numero_mesa,
                Mesa.restaurante_id == restaurante_id,
                Mesa.activa == True,
            )
            .first()
        )

    def obtener_mesas(self, skip: int = 0, limit: int = 100) -> List[Mesa]:
        """
        Obtener lista de mesas activas con paginación.
        """
        return (
            self.db.query(Mesa)
            .filter(Mesa.activa == True)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def actualizar_mesa(self, mesa_id: UUID, **kwargs) -> Optional[Mesa]:
        """
        Actualizar los datos de una mesa existente con validaciones.
        """
        mesa = self.obtener_mesa(mesa_id)
        if not mesa:
            return None

        if "numero_mesa" in kwargs:
            nuevo_numero = kwargs["numero_mesa"]
            if nuevo_numero <= 0:
                raise ValueError("El número de la mesa debe ser mayor que 0")
            existente = self.obtener_mesa_por_numero(nuevo_numero, mesa.restaurante_id)
            if existente and existente.id_mesa != mesa_id:
                raise ValueError("Ya existe una mesa con ese número en este restaurante")

        if "capacidad" in kwargs and kwargs["capacidad"] <= 0:
            raise ValueError("La capacidad debe ser mayor que 0")

        if "ubicacion" in kwargs and kwargs["ubicacion"]:
            ubicacion = kwargs["ubicacion"].strip()
            if len(ubicacion) > 100:
                raise ValueError("La ubicación no puede exceder 100 caracteres")
            kwargs["ubicacion"] = ubicacion

        for key, value in kwargs.items():
            if hasattr(mesa, key):
                setattr(mesa, key, value)

        self.db.commit()
        self.db.refresh(mesa)
        return mesa

    def eliminar_mesa(self, mesa_id: UUID, soft_delete: bool = True) -> bool:
        """
        Eliminar una mesa.
        Por defecto hace un soft delete (activa=False).
        """
        mesa = self.obtener_mesa(mesa_id)
        if not mesa:
            return False

        if soft_delete:
            mesa.activa = False
            self.db.commit()
        else:
            self.db.delete(mesa)
            self.db.commit()

        return True
