from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from database.models.categoria import Categoria


class CategoriaCRUD:
    def __init__(self, db: Session):
        self.db = db

    def crear_categoria(self, nombre: str, descripcion: str = None) -> Categoria:
        """
        Crear una nueva categoría con validaciones.
        """
        if not nombre or len(nombre.strip()) == 0:
            raise ValueError("El nombre de la categoría es obligatorio")

        if len(nombre) > 100:
            raise ValueError("El nombre no puede exceder 100 caracteres")

        if self.obtener_categoria_por_nombre(nombre):
            raise ValueError("Ya existe una categoría con ese nombre")

        categoria = Categoria(
            nombre=nombre.strip(),
            descripcion=descripcion.strip() if descripcion else None,
        )
        self.db.add(categoria)
        self.db.commit()
        self.db.refresh(categoria)
        return categoria

    def obtener_categoria(self, categoria_id: UUID) -> Optional[Categoria]:
        """
        Obtener una categoría por ID.
        """
        return (
            self.db.query(Categoria)
            .filter(Categoria.id_categoria == categoria_id, Categoria.activa == True)
            .first()
        )

    def obtener_categoria_por_nombre(self, nombre: str) -> Optional[Categoria]:
        """
        Obtener una categoría por nombre.
        """
        return (
            self.db.query(Categoria)
            .filter(Categoria.nombre == nombre.strip(), Categoria.activa == True)
            .first()
        )

    def obtener_categorias(self, skip: int = 0, limit: int = 100) -> List[Categoria]:
        """
        Obtener lista de categorías activas con paginación.
        """
        return (
            self.db.query(Categoria)
            .filter(Categoria.activa == True)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def actualizar_categoria(self, categoria_id: UUID, **kwargs) -> Optional[Categoria]:
        """
        Actualizar una categoría con validaciones.
        """
        categoria = self.obtener_categoria(categoria_id)
        if not categoria:
            return None

        if "nombre" in kwargs:
            nombre = kwargs["nombre"]
            if not nombre or len(nombre.strip()) == 0:
                raise ValueError("El nombre de la categoría es obligatorio")
            if len(nombre) > 100:
                raise ValueError("El nombre no puede exceder 100 caracteres")
            existente = self.obtener_categoria_por_nombre(nombre)
            if existente and existente.id_categoria != categoria_id:
                raise ValueError("Ya existe una categoría con ese nombre")
            kwargs["nombre"] = nombre.strip()

        if "descripcion" in kwargs and kwargs["descripcion"]:
            kwargs["descripcion"] = kwargs["descripcion"].strip()

        for key, value in kwargs.items():
            if hasattr(categoria, key):
                setattr(categoria, key, value)

        self.db.commit()
        self.db.refresh(categoria)
        return categoria

    def eliminar_categoria(self, categoria_id: UUID, soft_delete: bool = True) -> bool:
        """
        Eliminar una categoría.
        Por defecto hace un soft delete (activa=False).
        """
        categoria = self.obtener_categoria(categoria_id)
        if not categoria:
            return False

        if soft_delete:
            categoria.activa = False
            self.db.commit()
        else:
            self.db.delete(categoria)
            self.db.commit()

        return True
