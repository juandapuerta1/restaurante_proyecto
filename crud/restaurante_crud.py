from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from database.models.restaurante import Restaurante


class RestauranteCRUD:
    def __init__(self, db: Session):
        """
        Clase para manejar operaciones CRUD de la entidad Restaurante.
        """
        self.db = db

    def crear_restaurante(
        self,
        nombre: str,
        direccion: str,
        horario_apertura: str,
        horario_cierre: str,
        usuario_admin_id: UUID,
        telefono: Optional[str] = None,
        email: Optional[str] = None,
        capacidad_maxima: int = 50,
        activo: bool = True,
    ) -> Restaurante:
        """
        Crear un nuevo restaurante con validaciones.
        """
        if not nombre or len(nombre.strip()) == 0:
            raise ValueError("El nombre del restaurante es obligatorio")
        if len(nombre) > 200:
            raise ValueError("El nombre no puede exceder 200 caracteres")

        if not direccion or len(direccion.strip()) == 0:
            raise ValueError("La dirección es obligatoria")

        if capacidad_maxima <= 0:
            raise ValueError("La capacidad máxima debe ser mayor que 0")

        restaurante = Restaurante(
            nombre=nombre.strip(),
            direccion=direccion.strip(),
            horario_apertura=horario_apertura.strip(),
            horario_cierre=horario_cierre.strip(),
            usuario_admin_id=usuario_admin_id,
            telefono=telefono.strip() if telefono else None,
            email=email.strip() if email else None,
            capacidad_maxima=capacidad_maxima,
            activo=activo,
        )
        self.db.add(restaurante)
        self.db.commit()
        self.db.refresh(restaurante)
        return restaurante

    def obtener_restaurante(self, restaurante_id: UUID) -> Optional[Restaurante]:
        """
        Obtener un restaurante por ID (solo si está activo).
        """
        return (
            self.db.query(Restaurante)
            .filter(Restaurante.id_restaurante == restaurante_id, Restaurante.activo == True)
            .first()
        )

    def obtener_restaurantes(self, skip: int = 0, limit: int = 100) -> List[Restaurante]:
        """
        Obtener lista de restaurantes activos con paginación.
        """
        return (
            self.db.query(Restaurante)
            .filter(Restaurante.activo == True)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def actualizar_restaurante(self, restaurante_id: UUID, **kwargs) -> Optional[Restaurante]:
        """
        Actualizar los datos de un restaurante existente con validaciones.
        """
        restaurante = self.obtener_restaurante(restaurante_id)
        if not restaurante:
            return None

        if "nombre" in kwargs and kwargs["nombre"]:
            nombre = kwargs["nombre"].strip()
            if len(nombre) == 0:
                raise ValueError("El nombre del restaurante es obligatorio")
            if len(nombre) > 200:
                raise ValueError("El nombre no puede exceder 200 caracteres")
            kwargs["nombre"] = nombre

        if "direccion" in kwargs and kwargs["direccion"]:
            direccion = kwargs["direccion"].strip()
            if len(direccion) == 0:
                raise ValueError("La dirección es obligatoria")
            kwargs["direccion"] = direccion

        if "capacidad_maxima" in kwargs and kwargs["capacidad_maxima"] <= 0:
            raise ValueError("La capacidad máxima debe ser mayor que 0")

        if "telefono" in kwargs and kwargs["telefono"]:
            kwargs["telefono"] = kwargs["telefono"].strip()

        if "email" in kwargs and kwargs["email"]:
            kwargs["email"] = kwargs["email"].strip()

        for key, value in kwargs.items():
            if hasattr(restaurante, key):
                setattr(restaurante, key, value)

        self.db.commit()
        self.db.refresh(restaurante)
        return restaurante

    def eliminar_restaurante(self, restaurante_id: UUID, soft_delete: bool = True) -> bool:
        """
        Eliminar un restaurante.
        Por defecto hace un soft delete (activo=False).
        """
        restaurante = self.obtener_restaurante(restaurante_id)
        if not restaurante:
            return False

        if soft_delete:
            restaurante.activo = False
            self.db.commit()
        else:
            self.db.delete(restaurante)
            self.db.commit()

        return True
